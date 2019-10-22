import json
import matplotlib.pyplot as plt
from itertools import cycle


filename = "inventory.json"
logaxis  = True
target_elements = ['Co', 'V', 'Ti']

SECS_TO_YEAR = 1.0/(60.*60.*24.*365.)

# parse the json file
with open(filename) as f:
    data = json.load(f)

def get_data(property, element=None):
    times = []
    entries = []
    
    for t in data['inventory_data']:
        nuclides = t['nuclides']
        cooling_time = t['cooling_time']
        
        # only take the cooling times
        if cooling_time == 0.0:
            continue

        if element:
            total = sum(n[property] for n in nuclides if n['element'] == element)
        else:
            total = sum(n[property] for n in nuclides)

        times.append(cooling_time*SECS_TO_YEAR)
        entries.append(total)
        
    return times, entries

cycol = cycle('kbgrcm')
def plot_data(elements, property='grams', **kwargs):
    td = get_data(property)
    plt.plot(td[0], td[1], **kwargs, color=next(cycol), label='Total')
    for e in elements:
        d = get_data(property, e)
        plt.plot(d[0], d[1], **kwargs, linestyle='--', color=next(cycol), label=e)
    
d = plot_data(target_elements, property='activity', marker='o')
    
if logaxis:
    plt.xscale('log')
    
plt.title('Activity vs time', fontsize=22)
plt.xlabel('Time after irradiation (years)', fontsize=18)
plt.ylabel('Activity (Bq)', fontsize=18)
plt.legend()
plt.grid(True, which="both")
plt.savefig('nuclideactivity.pdf')
#plt.show()
