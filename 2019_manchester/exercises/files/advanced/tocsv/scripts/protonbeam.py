import os
import pypact as pp
import numpy as np

mean_energy = 80e6 #eV
values = np.random.normal(mean_energy, 0.2*mean_energy, 100000)

GROUP = list(reversed(pp.ALL_GROUPS[162]))

def findbin(energy, group):
    for j in range(len(group)):
        if energy < group[j]:
            return j
    return -1

Y = [0]*(len(GROUP)-1)
for i in range(len(values)):
    indx = findbin(values[i], GROUP)
    Y[indx] +=1

ff = pp.FluxesFile()
ff.values = Y
filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'fluxes')
pp.to_file(ff, filename)

