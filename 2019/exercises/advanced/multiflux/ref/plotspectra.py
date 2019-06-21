import pypact as pp
import matplotlib.pyplot as plt


ff1 = pp.FluxesFile()
ff2 = pp.FluxesFile()

pp.from_file(ff1, 'fluxes.1')
pp.from_file(ff2, 'fluxes.2')

#ff1.values = list(reversed(ff1.values))

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

FS=18
f1 = plt.figure()
plt.loglog(*getraw(ff1), 'k', label="position 1")
plt.loglog(*getraw(ff2), 'r', label="position 2")
plt.xlabel("Energy (eV)", fontsize=FS)
plt.ylabel("Normalised units", fontsize=FS)
plt.legend()
plt.show()
