import matplotlib.pyplot as plt

def readtab4(tab4file):
    with open(tab4file, 'r') as f:
        data = f.readlines()
    bins = []
    spec = []
    for line in data:
        if "[" in line:
            linelist = line.strip().split()
            # read lower bounds and spectrum
            bins.append(float(linelist[1].replace(",","")))
            spec.append(float(linelist[4]))
        # add final upper bound
        if data.index(line) == len(data)-1:
            bins.append(float(linelist[2].replace("]","")))
    return bins, spec
    
# =====================

tab24file = "default/defaultspec.tab4"
bins24group, spectrum24group = readtab4(tab24file)

tabhigh = "highres/gammaspec.tab4"
binshighgroup, spectrumhighgroup = readtab4(tabhigh)

plt.hist(bins24group[:-1], bins=bins24group, weights=spectrum24group, histtype='step', color="orange", label="24 group bins")
plt.hist(binshighgroup[:-1], bins=binshighgroup, weights=spectrumhighgroup, color="blue", label="0.01MeV bins")

plt.yscale('log')
plt.ylabel("Gamma Intensity (MeV/s)")
plt.xlabel("Energy (MeV)")
plt.xscale('log')
plt.xlim(1E-1, 1E1)
plt.legend(loc='best')
plt.show()