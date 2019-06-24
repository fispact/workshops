import os
import pypact as pp
import numpy as np

mean_energy = 10e6 #eV
values = np.random.normal(mean_energy, 0.3*mean_energy, 1000000)

GROUP = list(reversed(pp.ALL_GROUPS[162]))

def findbin(energy, group):
    for j in range(len(group)):
        if energy <= group[j]:
            return j
    return -1

Y = [0]*(len(GROUP)-1)
for i in range(len(values)):
    indx = findbin(values[i], GROUP)
    Y[indx] +=1

ff = pp.FluxesFile()
ff.values = Y
filename = 'fluxes.{}'.format(len(GROUP)-1)
pp.to_file(ff, filename)

