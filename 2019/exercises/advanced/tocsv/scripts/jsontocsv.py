#!/usr/bin/env python3

import os
import json


# change the filename here
filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'proton.json')

# if you change this you must also
# change the list at the bottom!
headers = [
    'nuclides',
    'activity (Bq)',
    'grams',
    'alpha heat (kW)',
    'beta heat (kW)',
    'gamma heat (kW)',
    'irradiation time (secs)',
    'cooling time (secs)',
    'cumulative time (secs)',
    'flux amplitude (/cm2/s)'
]

def fmt(items):
    str = "{:>20}".format(items[0])
    for i in items:
        str += ", {:>20}".format(i)
    return "{}\n".format(str)

with open(filename) as file:
    data = json.loads(file.read())
    with open('proton.csv', 'wt') as f:
        f.write(fmt(headers))
        for t in data['inventory_data']:
            for n in t['nuclides']:
                currenttime = t['irradiation_time'] + t['cooling_time']
                name = '{}{}{}'.format(n['element'], n['isotope'], n['state'])
                # if you changed the headers you must change this too!!
                #
                f.write(fmt([name,
                             n['activity'],
                             n['grams'],
                             n['alpha_heat'],
                             n['beta_heat'],
                             n['gamma_heat'],
                             t['irradiation_time'],
                             t['cooling_time'],
                             currenttime,
                             t['flux']]))
