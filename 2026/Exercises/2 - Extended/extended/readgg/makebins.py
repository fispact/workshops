import numpy as np

bounds = np.linspace(1e-5, 5e6, 20000, endpoint=True)


with open('ggbins', 'wt') as f:
    f.write("{}\n".format(len(bounds)-1))
    for b in bounds:
        f.write("{:.8e}\n".format(b))
