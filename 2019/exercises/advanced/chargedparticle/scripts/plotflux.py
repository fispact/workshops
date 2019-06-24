import os
import pypact as pp
import matplotlib.pyplot as plt


fluxes1 = 'fluxes.162'
fluxes2 = 'fluxes.162.convert'
fluxes3 = 'fluxes.616'

ff1 = pp.FluxesFile()
ff2 = pp.FluxesFile()
ff3 = pp.FluxesFile()

pp.from_file(ff1, fluxes1)
pp.from_file(ff2, fluxes2)
pp.from_file(ff3, fluxes3)

ff1.values = [f/sum(ff1.values) for f in ff1.values]
ff2.values = [f/sum(ff2.values) for f in ff2.values]
ff3.values = [f/sum(ff3.values) for f in ff3.values]

plt.plot(ff1.midPointEnergies, ff1.values, 'k', alpha=0.7, label='162 original')
plt.plot(ff2.midPointEnergies, ff2.values, 'r', alpha=0.5, label='162 group convert')
plt.plot(ff3.midPointEnergies, ff3.values, 'g', alpha=0.6, label='616 original')

plt.xlim([0,3e6])
plt.xlabel("Energy (eV)", fontsize=18)
plt.ylabel("Normalised units", fontsize=18)
plt.grid()
plt.legend()
plt.show()
