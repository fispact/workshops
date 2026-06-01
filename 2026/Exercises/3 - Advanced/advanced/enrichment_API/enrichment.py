import os
import sys
import pyfispact as pf


# initiaise error logging and load base data
m = pf.Monitor()
pf.initialise(m)

# progress output for ND load
def loadfunc(k, p, index, total):
    print(" [{}/{}]  Reading {}: {}".format(index, total, k, p), end="\r")
    sys.stdout.write("\033[K")

# progress output for fispact calculation
def computefunc(p, index, total):
    print(" [{}/{}]  processing {}".format(index, total, p))

# load Nuclear Data
def loadNuclearData( ndpath ):
    # create NuclearDataReader
    ndr = pf.io.NuclearDataReader(m)
    # set paths o Nuclear data files
    ndr.setpath(pf.io.ND_IND_NUC_KEY(),  os.path.join(ndpath,"decay/decay_2012_index_2012"))
    ndr.setpath(pf.io.ND_XS_ENDF_KEY(), os.path.join(ndpath,"TENDL2017data/tal2017-n/gxs-709"))
    ndr.setpath(pf.io.ND_FY_ENDF_KEY(), os.path.join(ndpath,"GEFY61data/gefy61_nfy"))
    ndr.setpath(pf.io.ND_SF_ENDF_KEY(), os.path.join(ndpath,"GEFY61data/gefy61_sfy"))
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


def readfluxfile( filename ):
    with open( filename, "r") as f:
       data = f.readlines()
    flux = []
    for line in data[:-2]:
        linelist = line.strip().split()
        for ll in linelist:
           flux.append(float(ll))
    # flux files are high-to-low in energy, API expects flux in low-to-high so reverse
    flux.reverse()
    return flux

def setInputDatabyMASS( element, fluxspectrum, runlabel  ):
    # initialsie input data
    ip = pf.InputData(m)
    ip.setname(runlabel )  
    # set flux
    ip.setflux(pf.groups.G709(), fluxspectrum)
    ip.setfluxwallloading(1.0)
    ip.setfluxname("{} flux".format(runlabel))
    # set material
    ip.setmasstotal(1.0)
    # for each nuclide add atoms
    ip.setmass( [pf.util.z_from_element(m, element)], [100] )
    # set irradiation schedule - 5mins at 1.1E14 n/cm2/s
    ip.appendschedule(60*pf.util.MIN_TO_SEC(), 1.1E14)
    return ip

def runFISPACT(i, nd):
    # run fispact
    o = pf.OutputData(m)
    pf.process(i, nd, o, m, op=computefunc)    
    return o

def readfluxfile( filename ):
    with open( filename, "r") as f:
       data = f.readlines()
    flux = []
    for line in data[:-2]:
        linelist = line.strip().split()
        for ll in linelist:
           flux.append(float(ll))
    # flux files are high-to-low in energy, API expects flux in low-to-high so reverse
    flux.reverse()
    return flux

# ===================================================================

# load ND
pathtoND = "" # Add path to ND
nucleardata = loadNuclearData( pathtoND)

label = "unenriched"
flux = readfluxfile("fluxes")
input = setInputDatabyMASS( "Li", flux, label )
output = runFISPACT(input, nucleardata)
pf.io.to_file(output, m, "{}.json".format(label) )

# Perform 60% enriched run
# pf.elementaldata methods can get set abundance

pf.finalise(m)
pf.io.to_file(m, "enrichment.log")