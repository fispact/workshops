import os
import pypact as pp

fluxes = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'fluxes')

ff1 = pp.FluxesFile()
pp.from_file(ff1, fluxes)

# normalise values
sum1 = sum(ff1.values)
ff1.values = [v/sum1 for v in ff1.values]

import matplotlib.pyplot as plt

plt.loglog(ff1.midPointEnergies, ff1.values, 'k', alpha=0.7, label='80 MeV proton beam')
plt.xlabel("Energy (eV)", fontsize=18)
plt.ylabel("Normalised units", fontsize=18)
plt.grid()
plt.legend()
plt.show()
