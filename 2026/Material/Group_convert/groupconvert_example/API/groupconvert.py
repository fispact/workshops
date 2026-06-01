import pyfispact as pf 
import matplotlib.pyplot as plt
import numpy as np

# initilise api data
m = pf.Monitor()
pf.initialise(m)

# the flux to be converted
influx = [0.00000E+00,  0.00000E+00, 0.00000E+00,  0.00000E+00,  0.11928E+09,  0.17608E+09, 
0.62853E+08,  0.58480E+07,  0.16908E+07,  0.17753E+07,  0.64655E+06,  0.46320E+06,  
0.57011E+06,  0.50139E+06,  0.43369E+06,  0.40740E+06,  0.41138E+06,  0.40775E+06,  
0.39009E+06,  0.42391E+06,  0.43776E+06,  0.46747E+06,  0.48909E+06,  0.49538E+06,  
0.16593E+06,  0.33064E+06,  0.48575E+06,  0.49383E+06,  0.48773E+06,  0.46773E+06,  
0.46689E+06,  0.47122E+06,  0.47231E+06,  0.97966E+06,  0.10084E+07,  0.10309E+07,  
0.53031E+06,  0.53848E+06,  0.55074E+06,  0.55215E+06,  0.54645E+06,  0.55819E+06,  
0.37582E+06,  0.57623E+06,  0.57569E+06,  0.67050E+06,  0.37966E+06,  0.57469E+06,  
0.57558E+06,  0.57653E+06,  0.57568E+06,  0.57485E+06,  0.57192E+06,  0.56916E+06,  
0.56636E+06,  0.13397E+07,  0.55874E+06,  0.55649E+06,  0.14265E+07,  0.54122E+06,  
0.14528E+07,  0.10168E+07,  0.41081E+06,  0.56528E+06,  0.47650E+06,  0.46635E+06,  
0.44994E+06,  0.43135E+06,  0.41329E+06,  0.39456E+06,  0.37521E+06,  0.35626E+06,  
0.33835E+06,  0.32184E+06,  0.30724E+06,  0.29263E+06,  0.53636E+06,  0.48487E+06,  
0.22788E+06,  0.21958E+06,  0.41170E+06,  0.36288E+06,  0.38675E+05,  0.23495E+06,  
0.25023E+06,  0.30073E+06,  0.15320E+06,  0.28590E+06,  0.13255E+06,  0.12415E+06,  
0.11636E+06,  0.10974E+06,  0.10407E+06,  0.99085E+05,  0.94401E+05,  0.89664E+05,  
0.85481E+05,  0.80940E+05,  0.15443E+06,  0.70859E+05,  0.65789E+05,  0.61013E+05,  
0.56458E+05,  0.52890E+05,  0.12350E+06,  0.11199E+06,  0.38656E+05,  0.28673E+05,  
0.70869E+05,  0.42813E+05,  0.97397E+05,  0.36826E+05,  0.56511E+05,  0.51796E+05,  
0.64923E+05,  0.23554E+05,  0.28579E+05,  0.12483E+05,  0.92001E+04,  0.14476E+05,  
0.25488E+05,  0.74573E+04,  0.20596E+05,  0.29513E+05,  0.50249E+05,  0.42313E+05,  
0.14366E+05,  0.19371E+05,  0.30584E+05,  0.26151E+05,  0.23859E+05,  0.11160E+05,  
0.69794E+04,  0.66378E+04,  0.62833E+04,  0.30231E+04,  0.29258E+04,  0.55909E+04,  
0.52855E+04,  0.12799E+05,  0.10958E+05,  0.61309E+04,  0.79923E+04,  0.56241E+04,  
0.56522E+04,  0.44334E+04,  0.44357E+04,  0.44696E+04,  0.39133E+04,  0.23890E+04,  
0.22461E+04,  0.23493E+04,  0.20685E+04,  0.24265E+04,  0.17892E+04,  0.16793E+04,  
0.24464E+04,  0.21679E+04,  0.15035E+04,  0.11690E+04,  0.10122E+04,  0.14887E+04,  
0.12091E+04,  0.14246E+04,  0.10522E+04,  0.30769E+03,  0.42404E+03,  0.61543E+03,  
0.66738E+03,  0.38218E+03,  0.66876E+03,  0.61486E+03,  0.44706E+03,  0.28804E+04,  
0.81434E+04]
# flux taken directky from FISPACT so is in decending energy
# api takes fluxes in accending energy so reverse
influx.reverse()
# perfom group convert
outflux = pf.groupconvert.bylethargy(m, pf.groups.G175(), influx, pf.groups.G709() )
# find flux per unit lethargy
influxleth = []
for i in range(len(influx)):
    influxleth.append( influx[i] / np.log( pf.groups.G175()[i+1]/pf.groups.G175()[i] ))

outfluxleth = []
for i in range(len(outflux)):
    outfluxleth.append( outflux[i] / np.log( pf.groups.G709()[i+1]/pf.groups.G709()[i] ))

# plot fluxes
plt.hist(pf.groups.G175()[:-1], bins=pf.groups.G175(), weights=influxleth, histtype='step', color="orange", label="175 groups original")
plt.hist(pf.groups.G709()[:-1], bins=pf.groups.G709(), weights=outfluxleth, histtype='step', color="green", ls="dashed", label="709 groups converted")

plt.yscale('log')
plt.ylabel("Nuetron Flux per unit lethargy (n/cm2/s)")
plt.xlabel("Energy (eV)")
plt.xscale('log')
plt.legend(loc='upper left')
plt.show()

pf.finalise(m)