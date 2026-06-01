import pyfispact as pf 
import sys
import os
import argparse

m = pf.Monitor()
pf.initialise(m)

# read commandline args
def readargs():
    parser = argparse.ArgumentParser(description='Process file arguments.')
    parser.add_argument("-n", "--nucleardata", type=str, default="./", help='Point to base nuclear data library path')
    parser.add_argument("-i", "--matfluxfile", type=str, default="./", help='Point to file containing material and flux data')
    args = parser.parse_args()
    nd_base_path = args.nucleardata
    infilepath = args.matfluxfile
    return nd_base_path, infilepath

# progress output for ND load
def loadfunc(k, p, index, total):
    print(" [{}/{}]  Reading {}: {}".format(index, total, k, p), end="\r")
    sys.stdout.write("\033[K")

def load_TENDL17(ndpath):
    # create NuclearDataReader
    ndr = pf.io.NuclearDataReader(m)
    # set paths o Nuclear data files
    ndr.setpath(pf.io.ND_IND_NUC_KEY(),  os.path.join(ndpath,"decay/decay_2012_index_2012"))
    ndr.setpath(pf.io.ND_XS_ENDF_KEY(), os.path.join(ndpath,"TENDL2017data/tal2017-n/gxs-709"))
    ndr.setpath(pf.io.ND_PROB_TAB_KEY(), os.path.join(ndpath,"TENDL2017/tal2017-n/tp-709-294"))
    ndr.setpath(pf.io.ND_FY_ENDF_KEY(), os.path.join(ndpath,"ENDFB71data/endfb71-n/endfb71nfy"))
    ndr.setpath(pf.io.ND_SF_ENDF_KEY(), os.path.join(ndpath,"ENDFB71data/endfb71-n/endfb71sfy"))
    ndr.setpath(pf.io.ND_DK_ENDF_KEY(), os.path.join(ndpath,"decay/decay_2012"))
    ndr.setpath(pf.io.ND_HAZARDS_KEY(), os.path.join(ndpath,"decay/hazards_2012"))
    ndr.setpath(pf.io.ND_CLEAR_KEY(), os.path.join(ndpath,"decay/clear_2012"))
    ndr.setpath(pf.io.ND_A2DATA_KEY(), os.path.join(ndpath,"decay/a2_2012"))
    ndr.setpath(pf.io.ND_ABSORP_KEY(), os.path.join(ndpath,"decay/abs_2012"))
    # create Nucleardata object 
    nd = pf.NuclearData(m)
    # load nuclear data
    ndr.load(nd, op=loadfunc)
    return nd

# extract material and flux data
# this file reader could be improved with the use of 
# regular expressions
def getcelldata(cell, matfluxfile):
    with open( matfluxfile, 'r' ) as f:
        data = f.readlines()

    matflag = False
    cellflag = False
    fluxflag = False
    flux = []
    elements = []
    percentages = []
    mass = 0

    for line in data:
        # extract material infomation
        if matflag and cellflag:
            linelist = line.strip().split()
            if len(linelist) > 0:
                if "mass" in linelist[0]:
                    mass = float(linelist[-1])
                else:
                    elements.append( linelist[0]  )
                    percentages.append( float(linelist[-1])  )
            else:
                matflag = False
                cellflag = False

        # extract flux infomation
        if fluxflag and cellflag:
            linelist = line.strip().split()
            if len(linelist) > 0:
                flux.append( float(linelist[0]) )
            else:
                fluxflag = False
                cellflag = False

        if "Materials" in line:
            matflag = True
        
        if cell in line and len(line.strip())==len(cell):
            cellflag = True
        
        if "Flux" in line:
            fluxflag = True

    return mass, elements, percentages, flux

def set_inputdata( cell, matfluxfile ):
    # initialsie input data
    ip = pf.InputData(m)
    ip.setname(cell+" irrad")  
    # get material and flux
    mass, elements, percentages, flux = getcelldata(cell, matfluxfile)

    # set flux
    ip.setflux(pf.groups.G709(), flux)
    ip.setfluxwallloading(1.0)
    ip.setfluxname("709 flux "+cell)
    ip.setatomsthreshold(1.0e2)
    
    # set material
    ip.setmasstotal(mass)
    atomic_numbers = []
    for element in elements:
        # get atomic numbers for each element
        atomic_numbers.append( pf.util.z_from_element(m, element) )
    ip.setmass(  atomic_numbers, percentages )

    # set irradiation schedule
    # 2 year irradiation in 6 month increments
    for i in range(4):
        ip.appendschedule(6*pf.util.MONTH_TO_SEC(), 1E12)
    # 100 years of cooling
    ip.appendschedule(1, 0.0) # 1 second after irradiation
    ip.appendschedule(59, 0.0) # 1 minute after irradiation
    ip.appendschedule(4*pf.util.MIN_TO_SEC(), 0.0) # 5 minutes after irradiation
    ip.appendschedule(5*pf.util.MIN_TO_SEC(), 0.0) # 10 minutes after irradiation
    ip.appendschedule(20*pf.util.MIN_TO_SEC(), 0.0) # 30 minute after irradiation
    ip.appendschedule(30*pf.util.MIN_TO_SEC(), 0.0) # 1 hour after irradiation
    ip.appendschedule(23*pf.util.HOUR_TO_SEC(), 0.0) # 1 day after irradiation
    ip.appendschedule(6*pf.util.DAY_TO_SEC(), 0.0) # 1 week after irradiation
    ip.appendschedule(21*pf.util.DAY_TO_SEC(), 0.0) # 1 month after irradiation
    ip.appendschedule(5*pf.util.MONTH_TO_SEC(), 0.0) # 6 months after irradiation
    ip.appendschedule(6*pf.util.MONTH_TO_SEC(), 0.0) # 1 year after irradiation
    ip.appendschedule(1*pf.util.YEAR_TO_SEC(), 0.0) # 2 years after irradiation
    ip.appendschedule(2*pf.util.YEAR_TO_SEC(), 0.0) # 3 years after irradiation
    ip.appendschedule(2*pf.util.YEAR_TO_SEC(), 0.0) # 5 years after irradiation
    ip.appendschedule(5*pf.util.YEAR_TO_SEC(), 0.0) # 10 years after irradiation
    ip.appendschedule(10*pf.util.YEAR_TO_SEC(), 0.0) # 20 years after irradiation
    ip.appendschedule(10*pf.util.YEAR_TO_SEC(), 0.0) # 30 years after irradiation
    ip.appendschedule(10*pf.util.YEAR_TO_SEC(), 0.0) # 40 years after irradiation
    ip.appendschedule(10*pf.util.YEAR_TO_SEC(), 0.0) # 50 years after irradiation
    ip.appendschedule(10*pf.util.YEAR_TO_SEC(), 0.0) # 60 years after irradiation
    ip.appendschedule(10*pf.util.YEAR_TO_SEC(), 0.0) # 70 years after irradiation
    ip.appendschedule(10*pf.util.YEAR_TO_SEC(), 0.0) # 80 years after irradiation
    ip.appendschedule(10*pf.util.YEAR_TO_SEC(), 0.0) # 90 years after irradiation
    ip.appendschedule(10*pf.util.YEAR_TO_SEC(), 0.0) # 100 years after irradiation

    return ip

def run_fispact(i, nd):
    # run fispact
    o = pf.OutputData(m)
    pf.process(i, nd, o, m)    
    return o

def extractoutputs(o):
    # perform required analysis
    # co60 zai
    co60zai = pf.util.zai_from_name(m, "Co60")
    heating = []
    co60 = []
    time = []
    coolingtime = []
    # mass in kg
    mass = o.getinventoryvalue(0, pf.INVENTORY_TOTAL_MASS())
    # loop over inventories
    for i in range(o.getnrofinventoryentries()):
        # get inventory timesteps
        time.append(  (o.getinventoryvalue(i, pf.INVENTORY_IRRAD_TIME()) +
                        o.getinventoryvalue(i, pf.INVENTORY_COOL_TIME()))/pf.util.YEAR_TO_SEC() )

        if o.getinventoryvalue(i, pf.INVENTORY_COOL_TIME()) > 0:
            # get heating only during cooling
            heating.append( o.getinventoryvalue(i, pf.INVENTORY_TOTAL_HEAT()) )
            # get cooling times
            coolingtime.append(o.getinventoryvalue(i, pf.INVENTORY_COOL_TIME())/pf.util.YEAR_TO_SEC())
        # get co60 specififc activity
        if o.findinventoryexists(i, co60zai):
            # get co60 index in nuclide list
            nucindex = o.findinventoryindex(i, co60zai)
            # get co60 entry in inventory
            nuclides = o.getinventorynuclides(i)
            co60.append(  nuclides[nucindex].activity / mass )
        else:
            co60.append(0.0)

    return time, coolingtime, heating, mass, co60 

# ==============================================================

# get command line agruments and load nuclear data
ndpath, matfluxfile = readargs()
nd = load_TENDL17(ndpath)

componentcells = [ "cell1", "cell2", "cell3", "cell4", "cell5" ,"cell6", "cell7", "cell8", "cell9", "cell10" ]

# initialise outputs
co60activity = []
heating = []
totalmass = 0

# loop over cells, perform fispact calculation
for cell in componentcells:
    print( "Run for "+cell)
    # set inputs
    i = set_inputdata( cell, matfluxfile)
    # run fispact
    o = run_fispact(i, nd)
    # extract outputs
    time, coolingtime, cellheating, cellmass, co60act = extractoutputs(o)
    totalmass += cellmass
    co60activity.append(co60act)
    heating.append(cellheating)
    # prepare for next cell run
    i.reset()
    o.reset()

# analysis

# total component heating
totalheating = [0] * len(heating[0])
# sum heating
for heat in heating:
    for i in range(len(heat)):
        totalheating[i] += heat[i]

# divide by mass
totalheating = [ x/totalmass for x in totalheating ]

# print data files:
with open ( "component_heating.txt", 'w' ) as f:
    print( "{:^16} {:^16}".format( "Time (years)", "Heating (kW/kg)"), file=f )
    for i in range(len(totalheating)):
        print( "{:^16.4E} {:^16.4E}".format( coolingtime[i], totalheating[i] ), file=f)

with open( "co60_specific_activity.txt", 'w') as f:
    for i in range(len(componentcells)):
        #  only print outputs for cells whcih contian co60
        if co60activity[i].count(co60activity[i][0]) != len(co60activity[i]):
            print( componentcells[i], file=f )
            print("{:^16} {:^16}".format( "Time (years)", "Co60 Activity (Bq/kg)"), file=f )
            for j in range(len(co60activity[i])):
                print( "{:^16.4E} {:^16.4E}".format( time[j], co60activity[i][j] ), file=f)
            print("\n\n", file=f)

# clean up and tear down global data
pf.finalise(m)