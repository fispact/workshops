import pyfispact as pf 
import os
import argparse
import sys
import matplotlib.pyplot as plt

# initialse api monior and global data
m=pf.Monitor()
pf.initialise(m)

# read commandline args
def readargs():
    parser = argparse.ArgumentParser(description='Process file arguments.')
    parser.add_argument("-n", "--nucleardata", type=str, default="./", help='Point to base nuclear data library path')
    args = parser.parse_args()
    nd_base_path = args.nucleardata
    return nd_base_path

# progress output for ND load
def loadfunc(k, p, index, total):
    print(" [{}/{}]  Reading {}: {}".format(index, total, k, p), end="\r")
    sys.stdout.write("\033[K")

# progress output for fispact calculation
def computefunc(p, index, total):
    print(" [{}/{}]  processing {}".format(index, total, p))

def load_TENDL21(ndpath):
    # create NuclearDataReader
    ndr = pf.io.NuclearDataReader(m)
    # set paths o Nuclear data files
    ndr.setpath(pf.io.ND_IND_NUC_KEY(),  os.path.join(ndpath,"decay/decay_2012_index_2012"))
    ndr.setpath(pf.io.ND_XS_ENDF_KEY(), os.path.join(ndpath,"TENDL2021data/n-tendl2021/gendf-1102"))
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


# def load_TENDL17(ndpath):
#     # create NuclearDataReader
#     ndr = pf.io.NuclearDataReader(m)
#     # set paths o Nuclear data files
#     ndr.setpath(pf.io.ND_IND_NUC_KEY(),  os.path.join(ndpath,"decay/decay_2012_index_2012"))
#     ndr.setpath(pf.io.ND_XS_ENDF_KEY(), os.path.join(ndpath,"TENDL2017data/tal2017-n/gxs-709"))
#     ndr.setpath(pf.io.ND_FY_ENDF_KEY(), os.path.join(ndpath,"ENDFB71data/endfb71-n/endfb71nfy"))
#     ndr.setpath(pf.io.ND_SF_ENDF_KEY(), os.path.join(ndpath,"ENDFB71data/endfb71-n/endfb71sfy"))
#     ndr.setpath(pf.io.ND_DK_ENDF_KEY(), os.path.join(ndpath,"decay/decay_2012"))
#     ndr.setpath(pf.io.ND_HAZARDS_KEY(), os.path.join(ndpath,"decay/hazards_2012"))
#     ndr.setpath(pf.io.ND_CLEAR_KEY(), os.path.join(ndpath,"decay/clear_2012"))
#     ndr.setpath(pf.io.ND_A2DATA_KEY(), os.path.join(ndpath,"decay/a2_2012"))
#     ndr.setpath(pf.io.ND_ABSORP_KEY(), os.path.join(ndpath,"decay/abs_2012"))
#     # create Nucleardata object 
#     nd = pf.NuclearData(m)
#     # load nuclear data
#     ndr.load(nd, op=loadfunc)
#     return nd

def load_JEFF(ndpath):
    # create NuclearDataReader
    ndr = pf.io.NuclearDataReader(m)
    # set paths o Nuclear data files
    ndr.setpath(pf.io.ND_IND_NUC_KEY(),  os.path.join(ndpath,"JEFF33data/jeff33_index"))
    ndr.setpath(pf.io.ND_XS_ENDF_KEY(), os.path.join(ndpath,"JEFF33data/jeff33-n/gxs-709"))
    ndr.setpath(pf.io.ND_FY_ENDF_KEY(), os.path.join(ndpath,"JEFF33data/jeff33-n/jeff33nfy"))
    ndr.setpath(pf.io.ND_SF_ENDF_KEY(), os.path.join(ndpath,"JEFF33data/jeff33-n/jeff33nsfy"))
    ndr.setpath(pf.io.ND_DK_ENDF_KEY(), os.path.join(ndpath,"JEFF33data/decay"))
    ndr.setpath(pf.io.ND_HAZARDS_KEY(), os.path.join(ndpath,"decay/hazards_2012"))
    ndr.setpath(pf.io.ND_CLEAR_KEY(), os.path.join(ndpath,"decay/clear_2012"))
    ndr.setpath(pf.io.ND_A2DATA_KEY(), os.path.join(ndpath,"decay/a2_2012"))
    ndr.setpath(pf.io.ND_ABSORP_KEY(), os.path.join(ndpath,"decay/abs_2012"))
    # create Nucleardata object 
    nd = pf.NuclearData(m)
    # load nuclear data
    ndr.load(nd, op=loadfunc)
    return nd

def load_ENDF(ndpath):
    # create NuclearDataReader
    ndr = pf.io.NuclearDataReader(m)
    # set paths o Nuclear data files
    ndr.setpath(pf.io.ND_IND_NUC_KEY(),  os.path.join(ndpath,"ENDFB80data/endfb80_index"))
    ndr.setpath(pf.io.ND_XS_ENDF_KEY(), os.path.join(ndpath,"ENDFB80data/endfb80-n/gxs-709"))
    ndr.setpath(pf.io.ND_FY_ENDF_KEY(), os.path.join(ndpath,"ENDFB80data/endfb80-n/endfb80nfy"))
    ndr.setpath(pf.io.ND_SF_ENDF_KEY(), os.path.join(ndpath,"ENDFB80data/endfb80-n/endfb80sfy"))
    ndr.setpath(pf.io.ND_DK_ENDF_KEY(), os.path.join(ndpath,"ENDFB80data/decay"))
    ndr.setpath(pf.io.ND_HAZARDS_KEY(), os.path.join(ndpath,"decay/hazards_2012"))
    ndr.setpath(pf.io.ND_CLEAR_KEY(), os.path.join(ndpath,"decay/clear_2012"))
    ndr.setpath(pf.io.ND_A2DATA_KEY(), os.path.join(ndpath,"decay/a2_2012"))
    ndr.setpath(pf.io.ND_ABSORP_KEY(), os.path.join(ndpath,"decay/abs_2012"))
    # create Nucleardata object 
    nd = pf.NuclearData(m)
    # load nuclear data
    ndr.load(nd, op=loadfunc)
    return nd

def get_nrofphotonlines(nd):
    # get decay nuclides
    decaynuclides = nd.getdecayzais()
    for i in range(len(decaynuclides)):
        # check stability
        if not nd.getdecayisstable(i):
            # get teh number of spectra for given nuclide
            nrofspectra = nd.getdecaynrofspectrumtypes(i)
            nrofgammalines = 0
            nrofxraylines = 0
            for j in range(nrofspectra):
                spectype = nd.getdecayspectrumtype(i, j)
                # check for gamma spec
                if spectype == pf.SPECTRUM_TYPE_GAMMA():
                    # get number of spectral lines 
                    nrofgammalines = nd.getdecayspectrumnroflines(i, j)
                # check for xray spec
                if spectype == pf.SPECTRUM_TYPE_X_RAY():
                    # get number of spectral lines
                    nrofxraylines = nd.getdecayspectrumnroflines(i, j)
            # if gamma or xray spec exits print to screen
            if (nrofxraylines + nrofgammalines) > 0:
                print(  "{:^16} Nr of gamma lines : {:4d}   Nr of xray lines : {:4d}"
                .format(pf.util.nuclide_from_zai(m, decaynuclides[i]),nrofgammalines,nrofxraylines))


def set_input(g1102=False):
    # initialsie input data
    ip = pf.InputData(m)
    ip.setname("Os irrad")  
    # find 10MeV bin and set to 1
    if g1102:
        groups = pf.groups.G1102()
        gps = "1102"
        # set flux to zero array    
        flux = [0.0] * 1102
    else:
        groups = pf.groups.G709()
        gps = "709"
        # set flux to zero array
        flux = [0.0] * 709

    for i in groups:
        if i >= 1E7:
            flux[groups.index(i)] = 1
            break

    # set flux
    ip.setflux(groups, flux)
    ip.setfluxwallloading(1.0)
    ip.setfluxname("{} 10MeV flux".format(gps))
    ip.setatomsthreshold(1.0e2)
    # set material
    ip.setmasstotal(1.0)
    ip.setmass(  [pf.util.z_from_element(m, "Os")], [100] )
    # set irradiation schedule
    ip.appendschedule(10*pf.util.MIN_TO_SEC(), 1E12)
    for i in range(60):
        ip.appendschedule(1*pf.util.MIN_TO_SEC(), 0.0)
    return ip

def run(i, nd):
    # run fispact
    o = pf.OutputData(m)
    pf.process(i, nd, o, m, op=computefunc)    
    return o

def getdecayheating(o):
    # get decay heating for cooling times
    heating = []
    for i in range(1,o.getnrofinventoryentries()):
        heating.append(o.getinventoryvalue(i, pf.INVENTORY_TOTAL_HEAT() ))
    return heating
# ===========================================================================
# read command line args
ndpath = readargs()


# set input data - flux, material, irradiation
# TENDL21 uses 1102 groups so needs different input data obj
i = set_input(g1102=True)
# tendl21 case
nd_t21 = load_TENDL21(ndpath)
o_t21 = run(i, nd_t21)
heating_t21 = getdecayheating(o_t21)

# set input data - flux, material, irradiation
# following all use 709 groups, can use the same input
i = set_input()

# tendl17 case
# nd_t17 = load_TENDL17(ndpath)
# o_t17 = run(i, nd_t17)
# heating_t17 = getdecayheating(o_t17)

# JEFF3.3 case
nd_jeff = load_JEFF(ndpath)
o_jeff = run(i, nd_jeff)
heating_jeff = getdecayheating(o_jeff)

# ENDFb8 case
nd_en = load_ENDF(ndpath)
o_en = run(i, nd_en)
heating_en = getdecayheating(o_en)

# get cooling time steps
time = [ ]
for i in range(1,o_en.getnrofinventoryentries()):  
    time.append( o_en.getinventoryvalue(i, pf.INVENTORY_COOL_TIME())  / 60 )      

# plot results
plt.plot( time, heating_t21, color="red", linestyle="dashdot", marker="s", markevery=3, label="TENDL2021")
# plt.plot( time, heating_t17, color="red", linestyle="solid", marker="x", markevery=3, label="TENDL2017")
plt.plot( time, heating_jeff, color="blue",linestyle="dashed", marker="o", markevery=3,  label="JEFF3.3")
plt.plot( time, heating_en, color="green", linestyle="dotted", marker="^", markevery=2, label="ENDFB8")
plt.legend(loc="best")
plt.grid(linestyle="solid", color="grey", alpha=0.5)
plt.xlabel("Cooling Time (mins)")
plt.ylabel("Deacy Heating (kW)")
plt.yscale("log")
plt.title("Os Decay Heating with different Nuclear Data using\nthe FISPACT-II API")
plt.show()
# teardown global data
pf.finalise(m)