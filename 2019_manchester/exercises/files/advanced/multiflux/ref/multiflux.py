import pypact as pp


YEAR_IN_SECS = 3.15576e+07

def makeinput(inventory=[], irradschedule=[], density=1.0, group=709, usemass=False):
    ipt = pp.InputData()

    # options
    ipt.enableSystemMonitor()
    ipt.overwriteExisting()
    ipt.enableJSON()
    ipt.readXSData(group=group)
    ipt.readDecayData()
    ipt.approxGammaSpectrum()
    ipt.setDensity(density)

    # use fuel to add nuclides
    if usemass:
        ipt.setMass(1.0e-3)
        for e, p in inventory:
            ipt.addElement(e, percentage=p)
    else:
        ipt.setFuel()
        for n, a in inventory:
            ipt.addIsotope(n, a)

    # irradiation schedule
    for dt, fa in irradschedule:
        ipt.addIrradiation(dt, fa)

    ipt.validate()

    return ipt

def getinventory(output):
    fuel = []
    # get the last entry only
    for n in output[-1].nuclides:
        fuel.append(("{}{}{}".format(n.element, n.isotope, n.state), n.atoms))
    return fuel

ipt1 = makeinput(inventory=[("W", 100.0)], usemass=True, 
    irradschedule=[(0.0, 1.1e14), (300., 1.1e14)])

fluxes = pp.FluxesFile()
files = pp.FilesFile()

pp.from_file(fluxes, 'fluxes.1')
pp.from_file(files, 'files.1')
opt1 = pp.compute(ipt1, files, fluxes, cleanup=False)
print(opt1.run_data.run_name)

irradschedule = [(0.0, 1.3e14), (600.0, 1.3e14)]
for i in range(10):
    irradschedule.extend((1.0*YEAR_IN_SECS, 0.0))

ipt2 = makeinput(inventory=getinventory(opt1), irradschedule=irradschedule)
pp.from_file(fluxes, 'fluxes.1')
pp.from_file(files, 'files.1')
opt2 = pp.compute(ipt2, files, fluxes)
