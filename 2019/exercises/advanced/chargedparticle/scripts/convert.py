import pypact as pp

ffin = pp.FluxesFile()
pp.from_file(ffin, 'fluxes.616')
assert ffin.boundaries == list(reversed(pp.ALL_GROUPS[616]))

ffout = pp.ArbFluxesFile("arb flux 616")
ffout.setGroup(ffin.boundaries)
ffout.values = ffin.values
pp.to_file(ffout, 'fluxes.616.arb')
