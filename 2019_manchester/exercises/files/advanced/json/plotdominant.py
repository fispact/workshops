import json
import matplotlib.pyplot as plt 


property = 'activity'
limit = 0.01 # 1%


time = [] 
values = [] 
with open('inventory.json') as f: 
    data = json.loads(f.read())
    for t in data['inventory_data']: 
        if t['flux'] == 0.0: 
            for n in t['nuclides']:
                time.append(t['cooling_time']) 
                values.append(t['gamma_heat']) 

plt.loglog(time, values, 'k', alpha=0.6)
plt.xlabel("Cooling time [s]", fontsize=18) 
plt.ylabel("Gamma heat (kW)", fontsize=18) 
plt.show()

