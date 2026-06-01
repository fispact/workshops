import os
import sys
import pypact as pp
import pyfispact as pf
import matplotlib.pyplot as plt

fluxes1file = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'fluxes1')
fluxes2file = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'fluxes2')

ff1 = pp.FluxesFile()
ff2 = pp.FluxesFile()
pp.from_file(ff1, fluxes1file)
pp.from_file(ff2, fluxes2file)

# normalise values
sum1 = sum(ff1.values)
sum2 = sum(ff2.values)
ff1.values = [v/sum1 for v in ff1.values]
ff2.values = [v/sum2 for v in ff2.values]

# create nuclear data objects and initialise global data
m = pf.Monitor()
pf.initialise(m)
ndr = pf.io.NuclearDataReader(m)
nd  = pf.NuclearData(m)

MT_NAMES = {
    1: 'total',
    2: 'E    ',
    3: 'nonel',
    4: 'n    ',
    5: 'O    ',
    11: '2nd  ',
    16: '2n   ',
    17: '3n   ',
    18: 'F    ',
    22: 'na   ',
    23: 'n3a  ',
    24: '2na  ',
    25: '3na  ',
    28: 'np   ',
    29: 'n2a  ',
    30: '2n2a ',
    32: 'nd   ',
    33: 'nt   ',
    34: 'nh   ',
    35: 'nd2a ',
    36: 'nt2a ',
    37: '4n   ',
    41: '2np  ',
    42: '3np  ',
    44: 'n2p  ',
    45: 'npa  ',
    102: 'g    ',
    103: 'p    ',
    104: 'd    ',
    105: 't    ',
    106: 'h    ',
    107: 'a    ',
    108: '2a   ',
    109: '3a   ',
    111: '2p   ',
    112: 'pa   ',
    113: 't2a  ',
    114: 'd2a  ',
    115: 'pd   ',
    116: 'pt   ',
    117: 'da   ',
    152: '5n   ',
    153: '6n   ',
    154: '2nt  ',
    155: 'ta   ',
    156: '4np  ',
    157: '3nd  ',
    158: 'nda  ',
    159: '2npa ',
    160: '7n   ',
    161: '8n   ',
    162: '5np  ',
    163: '6np  ',
    164: '7np  ',
    165: '4na  ',
    166: '5na  ',
    167: '6na  ',
    168: '7na  ',
    169: '4nd  ',
    170: '5nd  ',
    171: '6nd  ',
    172: '3nt  ',
    173: '4nt  ',
    174: '5nt  ',
    175: '6nt  ',
    176: '2nh  ',
    177: '3nh  ',
    178: '4nh  ',
    179: '3n2p ',
    180: '3n2a ',
    181: '3npa ',
    182: 'dt   ',
    183: 'npd  ',
    184: 'npt  ',
    185: 'ndt  ',
    186: 'nph  ',
    187: 'ndh  ',
    188: 'nth  ',
    189: 'nta  ',
    190: '2n2p ',
    191: 'ph   ',
    192: 'dh   ',
    193: 'ha   ',
    194: '4n2p ',
    195: '4n2a ',
    196: '4npa ',
    197: '3p   ',
    198: 'n3p  ',
    199: '3n2pa',
    200: '5n2p ',
    201: 'Xn   ',
    202: 'Xg   ',
    203: 'Xp   ',
    204: 'Xd   ',
    205: 'Xt   ',
    206: 'Xh   ',
    207: 'Xa   ',
    301: 'Ktot ',
    302: 'Kel  ',
    303: 'Knone',
    304: 'Kinel',
    318: 'Kfiss',
    401: 'Kdiss',
    402: 'Kradc',
    403: 'Kprot',
    407: 'Kalph',
    442: 'Kphot',
    443: 'Kktot',
    444: 'Dtot ',
    445: 'Del  ',
    446: 'Dinel',
    447: 'Ddiss'
}

NUCLIDE = "Al24"
ZAI = pf.util.zai_from_name(m, NUCLIDE)
MT  = 103
GROUP = pf.groups.G709()
PARTICLE = 'n'

# set cross section file paths
nuclear_data_base = os.getenv('NUCLEAR_DATA', "./")
nd.setnuclidezais([ZAI])
ndr.setpath(pf.io.ND_XS_ENDF_KEY(),  os.path.join(nuclear_data_base, 'TENDL2015data', 'tal2015-{}'.format(PARTICLE), 'gxs-{}'.format(len(GROUP)-1)))
ndr.load(nd)

# get the number loaded
zais = nd.getnuclidezais()
zindx = zais.index(ZAI)
mts = [nd.getreactionMT(zindx, j) for j in range(0, nd.getreactionnrofchannels(zindx)-1)]
print("Available MTs: {}".format(mts))
mtindx = mts.index(MT)

xs_values = nd.getreactionxs(zindx, mtindx)
# some reactions do not have all data, i.e. threshold reactions
if len(xs_values) != len(GROUP)-1:
    diffsize = len(GROUP) - 1 - len(xs_values)
    xs_values = [0.0]*diffsize + xs_values

# cleanup
pf.finalise(m)

# pf.io.to_file(m, "temp.log")
plt.loglog(GROUP[1:], xs_values, 'k', alpha=0.8, label='{} - (n,{})'.format(NUCLIDE, MT_NAMES[MT].strip()))
plt.loglog(ff1.midPointEnergies, ff1.values, 'b--', alpha=0.6, label='fluxes1 - thermal neutron')
plt.loglog(ff2.midPointEnergies, ff2.values, 'r--', alpha=0.5, label='fluxes2 - FNS')
plt.xlabel("Energy (eV)", fontsize=18)
plt.ylabel("Cross section (Barns)", fontsize=18)
plt.title('{} - (n,{})'.format(NUCLIDE, MT_NAMES[MT].strip()))
#plt.grid()
plt.legend()

collapsed1 = sum([xs_values[i]*ff1.values[i] for i in range(len(xs_values))])
collapsed2 = sum([xs_values[i]*ff2.values[i] for i in range(len(xs_values))])

print("Collapsed 1: {:.5e}".format(collapsed1))
print("Collapsed 2: {:.5e}".format(collapsed2))
plt.show()

