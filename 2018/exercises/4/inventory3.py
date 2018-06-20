import json
from itertools import cycle


filename = "inventory.json"
doplot   = True
logaxis  = True
target_elements = ['Co']

SECS_TO_YEAR = 1.0/(60.*60.*24.*365.)

# parse the json file
with open(filename) as f:
    data = json.load(f)

def get_data(element, property='grams'):

    times = []
    entries = []
    
    for t in data['inventory_data']:
        nuclides = t['nuclides']
        cooling_time = t['cooling_time']
        
        # only take the cooling times
        if cooling_time == 0.0:
            continue

        total_grams = sum(n[property] for n in nuclides if n['element'] == element)

        times.append(cooling_time*SECS_TO_YEAR)
        entries.append(total_grams)
        
    return times, entries

cycol = cycle('bgrcmk')
def plot_data(elements, property='grams', **kwargs):
    for e in elements:
        d = get_data(e, property)
        plt.plot(d[0], d[1], **kwargs, color=next(cycol), label=e)

if doplot:
    import matplotlib.pyplot as plt
    
    d = plot_data(target_elements, marker='o', linestyle='--')
    
    if logaxis:
        plt.xscale('log')
    
    plt.title('Grams vs time', fontsize=22)
    plt.xlabel('Time after irradiation (years)', fontsize=18)
    plt.ylabel('Mass (g)', fontsize=18)
    plt.legend()
    plt.grid(True, which="both")
    plt.show()
