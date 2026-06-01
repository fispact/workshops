import os
import pypact as pp

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

import matplotlib.pyplot as plt

plt.loglog(ff1.midPointEnergies, ff1.values, 'k', alpha=0.7, label='fluxes1 - thermal neutron')
plt.loglog(ff2.midPointEnergies, ff2.values, 'r', alpha=0.6, label='fluxes2 - FNS')
plt.xlabel("Energy (eV)", fontsize=18)
plt.ylabel("Normalised units", fontsize=18)
plt.grid()
plt.legend()
plt.show()
