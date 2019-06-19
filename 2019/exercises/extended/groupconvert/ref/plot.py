import os
import matplotlib.pyplot as plt
import pypact as pp

iflux = 'fluxes66.in'
oflux1 = os.path.join('ref', 'fluxes709_ref.out')
oflux2 = os.path.join('ref', 'fluxes709_2_ref.out')

iff = pp.ArbFluxesFile()
off1 = pp.FluxesFile()
off2 = pp.FluxesFile()

pp.from_file(iff, iflux)
pp.from_file(off1, oflux1)
pp.from_file(off2, oflux2)

def getraw(fluxes):
    x = []
    y = []
    norm = 1.0/sum(fluxes.values)
    for i in range(len(fluxes)):
        x.append(fluxes.boundaries[i])
        y.append(fluxes.values[i]*norm)
        x.append(fluxes.boundaries[i+1])
        y.append(fluxes.values[i]*norm)
    return x, y

# scale the values by bin width
def getscaled(fluxes):
    x = []
    y = []
    for i in range(len(fluxes)):
        scaledValue = fluxes.values[i]/(fluxes.boundaries[i+1] - fluxes.boundaries[i])
        x.append(fluxes.boundaries[i])
        y.append(scaledValue)
        x.append(fluxes.boundaries[i+1])
        y.append(scaledValue)
    return x, y

FS=18
f1 = plt.figure()
plt.loglog(*getraw(iff), 'k', label="66")
plt.loglog(*getraw(off1), 'r', label="709 (lethargy)")
plt.loglog(*getraw(off2), 'g', label="709 (energy)")
plt.xlabel("Energy (eV)", fontsize=FS)
plt.ylabel("Normalised units", fontsize=FS)
plt.legend()

f2 = plt.figure()
plt.loglog(*getscaled(iff), 'k', label="66")
plt.loglog(*getscaled(off1), 'r', label="709 (lethargy)")
plt.loglog(*getscaled(off2), 'g', label="709 (energy)")
plt.xlabel("Energy (eV)", fontsize=FS)
plt.ylabel("Normalised units per unit energy", fontsize=FS)
plt.legend()

plt.show()
