import matplotlib.pyplot as plt
import pypact as pp


def plotdata(group):
    x, y = [], []
    value = 1.0
    for g in reversed(pp.ALL_GROUPS[group]):
        x.append(g)
        y.append(-value)
        x.append(g)
        y.append(value)
        value = -value
    return x, y

plt.semilogx(*plotdata(66), 'k', label="66", alpha=0.7)
plt.semilogx(*plotdata(709), 'r', label="709", alpha=0.4)
plt.xlabel("Energy (eV)", fontsize=18)
plt.legend()
plt.show()
