import matplotlib.pyplot as plt


filename = 'extract.out'

x = []
y = []
y_low = []
y_high = []
with open(filename, 'rt') as f:
    for l in f.readlines()[2:]:
        data = l.split()
        assert len(data) == 8
        e_low = float(data[0])
        e_high = float(data[1])
        xs = float(data[4])
        xs_unc = float(data[5])*xs*0.1

        x.append((e_low + e_high)/2.0)
        y.append(xs)
        y_low.append(xs-xs_unc)
        y_high.append(xs+xs_unc)

plt.loglog(x, y, 'k')
#plt.loglog(x, y_low, 'y', alpha=0.6)
#plt.loglog(x, y_high, 'y', alpha=0.6)
plt.xlabel("Energy (eV)", fontsize=18)
plt.ylabel("Cross section (barns)", fontsize=18)
plt.show()

