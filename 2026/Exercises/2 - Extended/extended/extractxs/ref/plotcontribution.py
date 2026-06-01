import matplotlib.pyplot as plt


def getXS(data_file):
    x = []
    y = []
    with open(data_file, 'rt') as f:
        for l in f.readlines()[2:]:
            data = l.split()
            assert len(data) == 8
            e_low = float(data[0])
            e_high = float(data[1])
            xs = float(data[4])
            xs_unc = float(data[5])*xs*0.1

            x.append((e_low + e_high)/2.0)
            y.append(xs)
    return x, y

xt, yt = getXS('total.out')
xc, yc = getXS('ng.out')

x = xt
y = []
assert xc == xt
for i in range(len(yt)):
    y.append(yc[i]*100/yt[i])

plt.loglog(x, y, 'k')
plt.xlabel("Energy (eV)", fontsize=18)
plt.ylabel("(n,g) contribution (%)", fontsize=18)
plt.show()

