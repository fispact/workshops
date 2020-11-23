import pypact as pp


YEAR_IN_SECS = 3.15576e+07

# read output file from first run to get fuel for second run
fuel = []
with pp.Reader('first.out') as data:
    # get the last entry only
    for n in data[-1].nuclides:
        fuel.append(("{}{}{}".format(n.element, n.isotope, n.state), n.atoms))

# write an input file for second run
ipt = pp.InputData()

# options
ipt.enableSystemMonitor()
ipt.overwriteExisting()
ipt.enableJSON()
ipt.readXSData(group=709)
ipt.readDecayData()
ipt.approxGammaSpectrum()
ipt.setDensity(1.0)

# use fuel to add nuclides
ipt.setFuel()
for n, a in fuel:
    ipt.addIsotope(n, a)

# irradiation schedule
ipt.addIrradiation(0.0, 1.3e14)
ipt.addIrradiation(600.0, 1.3e14)
for i in range(10):
    ipt.addCooling(1.0*YEAR_IN_SECS)

pp.to_file(ipt, 'second.i')
