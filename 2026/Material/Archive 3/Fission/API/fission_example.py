import os
import sys
import pyfispact as pf 

import matplotlib.pyplot as plt

# initialise fispact and define Monitor object
m = pf.Monitor()
pf.initialise(m)

# callback for nuclear data loader
def loadfunc(k, p, index, total):
    print(" [{}/{}]  Reading {}: {}".format(index, total, k, p), end="\r")
    sys.stdout.write("\033[K")

# callback for compute
def computefunc(p, index, total):
    print(" [{}/{}]  processing {}".format(index, total, p))


def load_nuclear_data():
    # load nuclear data
    nd_base_path = "/opt/fispact/nuclear_data"
    nd = pf.NuclearData(m)
    ndr = pf.io.NuclearDataReader(m) 
    ndr.setpath(pf.io.ND_IND_NUC_KEY(),  os.path.join(nd_base_path, 'ENDFB80data', 'endfb80_index'))
    ndr.setpath(pf.io.ND_XS_ENDF_KEY(),  os.path.join(nd_base_path, 'ENDFB80data', 'endfb80-n', 'gxs-709'))
    ndr.setpath(pf.io.ND_FY_ENDF_KEY(),  os.path.join(nd_base_path, 'ENDFB80data', 'endfb80-n', 'endfb80nfy'))
    ndr.setpath(pf.io.ND_SF_ENDF_KEY(),  os.path.join(nd_base_path, 'ENDFB80data', 'endfb80-n', 'endfb80sfy'))
    ndr.setpath(pf.io.ND_DK_ENDF_KEY(),  os.path.join(nd_base_path, 'ENDFB80data', 'decay'))
    ndr.setpath(pf.io.ND_HAZARDS_KEY(),  os.path.join(nd_base_path, 'decay', 'hazards_2012'))
    ndr.setpath(pf.io.ND_CLEAR_KEY(),    os.path.join(nd_base_path, 'decay', 'clear_2012'))
    ndr.setpath(pf.io.ND_A2DATA_KEY(),   os.path.join(nd_base_path, 'decay', 'a2_2012'))
    ndr.setpath(pf.io.ND_ABSORP_KEY(),   os.path.join(nd_base_path, 'decay', 'abs_2012'))
    ndr.load(nd, op=loadfunc)
    return nd

def set_input(fission=True):
    input = pf.InputData(m)
    input.setname("UO2 fission")   
    flux = [  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,
            0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,
            0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,
            0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,
            0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,
            0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,
            0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,
            0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,
            0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,
            0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  8.2830E-09,
            8.3671E-09,  8.4529E-09,  8.5405E-09,  8.6299E-09,  8.7212E-09,  8.8145E-09,
            8.9098E-09,  9.0072E-09,  9.1067E-09,  9.2085E-09,  9.3125E-09,  9.4190E-09,
            1.7984E-08,  2.2576E-08,  2.7194E-08,  3.1479E-08,  3.9299E-08,  4.9503E-08,
            5.0118E-08,  5.0748E-08,  6.6106E-08,  8.7831E-08,  8.8979E-08,  9.0158E-08,
            1.1225E-07,  1.2839E-07,  1.6025E-07,  1.7260E-07,  2.2246E-07,  2.3988E-07,
            2.9160E-07,  3.5567E-07,  4.2244E-07,  4.2889E-07,  4.6982E-07,  6.1542E-07,
            7.1877E-07,  8.0673E-07,  1.0514E-06,  1.0690E-06,  1.1321E-06,  1.6084E-06,
            1.6369E-06,  1.9171E-06,  2.6724E-06,  2.7224E-06,  3.3088E-06,  3.7887E-06,
            3.8637E-06,  1.2690E-05,  1.6862E-05,  2.1487E-05,  2.7281E-05,  3.5423E-05,
            4.4694E-05,  5.4496E-05,  6.7502E-05,  8.2420E-05,  1.0576E-04,  1.1934E-04,
            1.3113E-04,  1.5107E-04,  1.7456E-04,  1.9307E-04,  2.2231E-04,  2.3776E-04,
            2.6166E-04,  2.7373E-04,  2.8154E-04,  2.9082E-04,  2.9955E-04,  3.2143E-04,
            3.2826E-04,  3.8362E-04,  4.5661E-04,  4.6031E-04,  4.9031E-04,  5.3136E-04,
            5.4347E-04,  5.5711E-04,  6.0174E-04,  5.3474E-04,  5.0684E-04,  4.9057E-04,
            4.7427E-04,  4.6126E-04,  5.3803E-04,  5.1749E-04,  4.9635E-04,  5.1538E-04,
            5.3508E-04,  5.3012E-04,  4.7201E-04,  4.8517E-04,  5.3913E-04,  5.2345E-04,
            4.7386E-04,  4.0071E-04,  4.0072E-04,  3.9171E-04,  4.5107E-04,  4.9751E-04,
            5.6289E-04,  6.1966E-04,  6.1323E-04,  5.7502E-04,  5.4506E-04,  5.2815E-04,
            5.1385E-04,  4.9955E-04,  4.8521E-04,  4.7071E-04,  4.5590E-04,  4.4015E-04,
            3.7467E-04,  3.6379E-04,  3.0517E-04,  2.7810E-04,  3.0505E-04,  3.3053E-04,
            3.4579E-04,  3.7554E-04,  3.7629E-04,  3.7995E-04,  3.7995E-04,  3.5413E-04,
            3.4407E-04,  3.2781E-04,  3.2455E-04,  3.1275E-04,  3.0160E-04,  2.9417E-04,
            2.8690E-04,  2.7932E-04,  2.7185E-04,  2.6456E-04,  2.5815E-04,  2.5201E-04,
            2.4632E-04,  2.4108E-04,  2.3571E-04,  2.3035E-04,  2.2510E-04,  2.2020E-04,
            2.1556E-04,  2.1115E-04,  2.0651E-04,  2.0204E-04,  2.0205E-04,  1.9637E-04,
            1.9209E-04,  1.9209E-04,  1.8699E-04,  1.8161E-04,  1.7978E-04,  1.7978E-04,
            1.7283E-04,  1.7066E-04,  1.6915E-04,  1.6916E-04,  1.6916E-04,  1.6427E-04,
            1.6136E-04,  1.5688E-04,  1.5687E-04,  1.5464E-04,  1.4900E-04,  1.4900E-04,
            1.4914E-04,  1.4923E-04,  1.4923E-04,  1.4923E-04,  1.4534E-04,  1.4381E-04,
            1.4161E-04,  1.4161E-04,  1.3961E-04,  1.3831E-04,  1.3766E-04,  1.3566E-04,
            1.3494E-04,  1.3549E-04,  1.3160E-04,  1.3158E-04,  1.3123E-04,  1.3037E-04,
            1.3037E-04,  1.3037E-04,  1.3037E-04,  1.3037E-04,  1.2709E-04,  1.2654E-04,
            1.2654E-04,  1.2654E-04,  1.2654E-04,  1.2581E-04,  1.2484E-04,  1.2428E-04,
            1.2267E-04,  1.2267E-04,  1.2267E-04,  1.2176E-04,  1.2176E-04,  1.2114E-04,
            1.1955E-04,  1.1955E-04,  1.2070E-04,  1.2159E-04,  1.2158E-04,  1.1886E-04,
            1.1840E-04,  1.1836E-04,  1.1813E-04,  1.1813E-04,  1.1789E-04,  1.1755E-04,
            1.1754E-04,  1.1217E-04,  1.0998E-04,  1.0998E-04,  1.2134E-04,  1.2138E-04,
            1.1974E-04,  1.1557E-04,  1.1556E-04,  1.1181E-04,  1.0896E-04,  1.0897E-04,
            1.1736E-04,  1.1881E-04,  1.1807E-04,  1.1352E-04,  1.1351E-04,  1.1332E-04,
            1.1305E-04,  1.1306E-04,  1.1201E-04,  1.1159E-04,  1.1158E-04,  1.1188E-04,
            1.1188E-04,  1.1181E-04,  1.1160E-04,  1.1160E-04,  1.1093E-04,  1.1042E-04,
            1.1042E-04,  1.1027E-04,  1.1025E-04,  1.0966E-04,  1.0609E-04,  1.0610E-04,
            1.0828E-04,  1.1122E-04,  1.1122E-04,  1.0586E-04,  1.0366E-04,  1.0366E-04,
            1.1035E-04,  1.1037E-04,  1.0880E-04,  1.0482E-04,  1.0482E-04,  1.0665E-04,
            1.0805E-04,  1.0804E-04,  1.0587E-04,  1.0550E-04,  1.0563E-04,  1.0643E-04,
            1.0643E-04,  1.0634E-04,  1.0622E-04,  1.0622E-04,  1.0340E-04,  1.0223E-04,
            1.0223E-04,  1.0265E-04,  1.0266E-04,  1.0215E-04,  1.0085E-04,  1.0085E-04,
            9.9686E-05,  9.8810E-05,  1.0020E-04,  1.0160E-04,  1.0160E-04,  1.0082E-04,
            1.0074E-04,  1.0074E-04,  1.0099E-04,  1.0115E-04,  1.0114E-04,  9.8018E-05,
            9.6760E-05,  9.6758E-05,  9.6444E-05,  9.5567E-05,  9.5568E-05,  9.5568E-05,
            9.5568E-05,  9.5152E-05,  9.4835E-05,  9.4835E-05,  9.4835E-05,  9.2917E-05,
            9.2697E-05,  9.2697E-05,  9.2697E-05,  9.2697E-05,  9.2697E-05,  9.2696E-05,
            9.2697E-05,  9.2698E-05,  9.2565E-05,  8.4842E-05,  8.4841E-05,  8.4841E-05,
            8.4841E-05,  8.4841E-05,  8.4842E-05,  8.4841E-05,  8.4841E-05,  8.4841E-05,
            8.4841E-05,  8.4841E-05,  8.4008E-05,  7.8136E-05,  7.8134E-05,  7.8133E-05,
            7.8134E-05,  7.8134E-05,  7.8135E-05,  7.8134E-05,  7.8133E-05,  7.8134E-05,
            7.8134E-05,  7.8135E-05,  7.9437E-05,  8.4460E-05,  8.4459E-05,  8.4461E-05,
            8.4459E-05,  8.4461E-05,  8.4460E-05,  8.4459E-05,  8.4461E-05,  8.4459E-05,
            8.4461E-05,  8.6705E-05,  8.2508E-05,  6.8216E-05,  7.5821E-05,  8.4352E-05,
            8.2907E-05,  7.7615E-05,  5.6237E-05,  6.7796E-06,  2.0439E-05,  5.7330E-05,
            6.8480E-05,  7.1685E-05,  7.3197E-05,  7.1573E-05,  7.3836E-05,  7.7780E-05,
            7.9197E-05,  7.9946E-05,  8.2852E-05,  8.2404E-05,  8.0754E-05,  7.8816E-05,
            8.1776E-05,  8.0197E-05,  7.8757E-05,  8.0664E-05,  8.1728E-05,  8.2409E-05,
            8.2484E-05,  8.2916E-05,  8.3268E-05,  8.3367E-05,  8.2840E-05,  8.0844E-05,
            8.2566E-05,  8.3687E-05,  8.4071E-05,  8.4295E-05,  8.4489E-05,  8.4711E-05,
            8.4809E-05,  8.4964E-05,  8.4759E-05,  8.4341E-05,  8.2707E-05,  8.0295E-05,
            7.8958E-05,  8.0164E-05,  8.1527E-05,  8.2656E-05,  8.3624E-05,  8.4053E-05,
            8.4698E-05,  8.5352E-05,  8.5661E-05,  8.5939E-05,  8.6760E-05,  8.7317E-05,
            8.7467E-05,  8.7690E-05,  8.8560E-05,  8.9187E-05,  8.9600E-05,  8.9876E-05,
            9.0553E-05,  9.1473E-05,  9.2260E-05,  9.3062E-05,  9.3880E-05,  9.5117E-05,
            9.6568E-05,  9.7730E-05,  9.9861E-05,  1.0219E-04,  1.0379E-04,  1.0927E-04,
            1.1019E-04,  1.1928E-04,  1.1958E-04,  1.3076E-04,  1.3204E-04,  1.4068E-04,
            1.4623E-04,  1.4675E-04,  1.5640E-04,  1.6189E-04,  1.6632E-04,  1.7020E-04,
            1.7349E-04,  1.7696E-04,  1.7958E-04,  1.8067E-04,  1.8170E-04,  1.8185E-04,
            1.8193E-04,  1.8008E-04,  1.7969E-04,  1.7549E-04,  1.7550E-04,  1.6819E-04,
            1.6819E-04,  1.6093E-04,  1.5800E-04,  1.5585E-04,  1.4409E-04,  1.4409E-04,
            1.3963E-04,  1.2658E-04,  1.2658E-04,  1.2658E-04,  1.0766E-04,  1.0574E-04,
            1.0573E-04,  1.0573E-04,  8.9399E-05,  8.8509E-05,  8.0277E-05,  7.6046E-05,
            7.4739E-05,  6.3354E-05,  6.3353E-05,  6.0798E-05,  5.0786E-05,  5.0786E-05,
            5.0783E-05,  4.0353E-05,  3.8596E-05,  3.8595E-05,  3.8594E-05,  2.8393E-05,
            2.7222E-05,  2.7221E-05,  2.7221E-05,  2.6701E-05,  1.7129E-05,  1.7128E-05,
            1.7128E-05,  1.7128E-05,  1.7129E-05,  1.7124E-05,  1.0474E-05,  8.8555E-06,
            8.8544E-06,  8.8546E-06,  8.8545E-06,  8.8543E-06,  8.8547E-06,  8.8544E-06,
            8.8546E-06,  3.0176E-06,  3.0176E-06,  3.0176E-06,  3.0177E-06,  3.0177E-06,
            3.0177E-06,  3.0177E-06,  3.0176E-06,  3.0177E-06,  3.0176E-06,  3.0177E-06,
            3.0177E-06,  3.0176E-06,  3.0176E-06,  3.0173E-06,  4.9145E-07,  3.5397E-07,
            3.5397E-07,  3.5397E-07,  3.5397E-07,  3.5397E-07,  3.5397E-07,  3.5397E-07,
            3.5398E-07,  3.5397E-07,  3.5397E-07,  3.5397E-07,  3.5397E-07,  3.5397E-07,
            3.5397E-07,  3.5397E-07,  3.5397E-07,  3.5398E-07,  3.5397E-07,  3.5397E-07,
            3.5397E-07,  3.5397E-07,  3.5397E-07,  3.5397E-07,  3.5397E-07,  3.5397E-07,
            3.5397E-07,  3.5397E-07,  3.5397E-07,  3.5398E-07,  3.5397E-07,  3.5397E-07,
            3.5398E-07,  3.5396E-07,  3.5320E-07,  3.6429E-13,  0.0000E+00,  0.0000E+00,
            0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,
            0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,
            0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,
            0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,
            0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,
            0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,
            0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,
            0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,
            0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,
            0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,
            0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,
            0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,
            0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,
            0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,
            0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,
            0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,  0.0000E+00,
            0.0000E+00,]
    # fispact API takes spectrum in acending energies!!!
    flux.reverse()
    input.setflux(pf.groups.G709(), flux)
    input.setfluxwallloading(1.0)
    input.setfluxname("709 PWR spectrum")
    input.setdensity(10.96)
    input.setatomsthreshold(1.0e5)
    if fission:
        input.setusefission(True)
        # list of nuclide zai's which fission should be included
        input.setfissionyieldincludes( [ pf.util.zai_from_name(m, "U235"),
                                        pf.util.zai_from_name(m, "U238") ] )
    # set initial material composition with feul
    # set my atoms for enrichment UO2 ~3% U235
    input.appendfuel(pf.util.zai_from_name(m, "U234"), 1E20)
    input.appendfuel(pf.util.zai_from_name(m, "U235"), 1.0124E23)
    input.appendfuel(pf.util.zai_from_name(m, "U236"), 4.6E20)
    input.appendfuel(pf.util.zai_from_name(m, "U238"), 3.230772E24)
    input.appendfuel(pf.util.zai_from_name(m, "O16"), 6.65047E24)
    input.appendfuel(pf.util.zai_from_name(m, "O17"), 2.53E21)
    input.appendfuel(pf.util.zai_from_name(m, "O18"), 1.367E25)
    # irradaition
    input.appendschedule(91.3*pf.util.DAY_TO_SEC(), 1E13)
    input.appendschedule(91.3*pf.util.DAY_TO_SEC(), 1E13)
    input.appendschedule(91.3*pf.util.DAY_TO_SEC(), 1E13)
    input.appendschedule(91.3*pf.util.DAY_TO_SEC(), 1E13)
    # cooling
    input.appendschedule( pf.util.HOUR_TO_SEC(), 0.0 )
    input.appendschedule( 23*pf.util.HOUR_TO_SEC(), 0.0 )
    input.appendschedule( 364*pf.util.DAY_TO_SEC(), 0.0 )
    input.appendschedule( 4*pf.util.YEAR_TO_SEC(), 0.0 )
    input.appendschedule( 5*pf.util.YEAR_TO_SEC(), 0.0 )
    input.appendschedule( 40*pf.util.YEAR_TO_SEC(), 0.0 )
    input.appendschedule( 50*pf.util.YEAR_TO_SEC(), 0.0 )
    return input

def run_fispact(i, nd):
    # run fispact
    o = pf.OutputData(m)
    pf.process(i, nd, o, m, op=computefunc)    
    return o

# ======================================

nuclear_data_obj = load_nuclear_data()
# run with fission
input_obj_fission = set_input(fission=True)
output_obj_fission = run_fispact(input_obj_fission, nuclear_data_obj)
pf.io.to_file(output_obj_fission, m, "{}.json".format("UO2_with_fission"))
# run without fission
input_obj_nofiss = set_input(fission=False)
output_obj_nofiss = run_fispact(input_obj_nofiss, nuclear_data_obj)
pf.io.to_file(output_obj_nofiss, m, "{}.json".format("UO2_no_fission"))

# plot data

# get total activity at cooling times
fiss_activity = []
nofiss_activity = []
time = []
for i in range(output_obj_nofiss.getnrofinventoryentries() ):
    if output_obj_nofiss.getinventoryvalue( i, pf.INVENTORY_COOL_TIME()) > 0.0:
        time.append( (output_obj_nofiss.getinventoryvalue( i, pf.INVENTORY_COOL_TIME()))/ pf.util.YEAR_TO_SEC() )
        fiss_activity.append( output_obj_fission.getinventoryvalue( i, pf.INVENTORY_TOTAL_ACTIVITY()) /  
                                output_obj_fission.getinventoryvalue( i, pf.INVENTORY_TOTAL_MASS())    )
        nofiss_activity.append( output_obj_nofiss.getinventoryvalue( i, pf.INVENTORY_TOTAL_ACTIVITY()) /  
                                output_obj_nofiss.getinventoryvalue( i, pf.INVENTORY_TOTAL_MASS()) )
plt.figure(figsize=(12,7))
plt.plot(time, fiss_activity, color="tab:blue", ls="solid", label="FISSION")
plt.plot(time, nofiss_activity, color="tab:orange", ls="dashed", label="No FISSION")
plt.xlim( time[0], time[-1]+1  )
plt.ylabel( "Activity (Bq/kg)" )
plt.yscale("log")
plt.xlabel( "Time (years)" )
plt.xscale("log")
plt.grid(linestyle = "--", linewidth = 0.5, axis='both', which='both')
plt.legend(loc="lower left")
plt.savefig("FISSION_ACT", bbox_inches="tight")
plt.close()

pf.finalise(m)