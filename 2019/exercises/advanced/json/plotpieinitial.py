import json
import matplotlib.pyplot as plt


filename = "inventory.json"

# parse the json file
with open(filename) as f:
    data = json.load(f)

# we want the first time step (in our case the initial inventory)
timestep = 0
nuclides = data['inventory_data'][timestep]['nuclides']

elements = {}
k = 'element'
v = 'grams'
for n in nuclides:
    if n[k] in elements:
        elements[n[k]] += n[v]
    else:
        elements[n[k]] = n[v]

total_grams = sum([g for e, g in elements.items()])
for e, g in elements.items():
    print("{} {:.2f}%".format(e, g*100.0/total_grams))

labels, values = list(zip(*(list(elements.items()))))

plt.pie(list(values), labels=list(labels), autopct='%2.2f%%', shadow=False)
plt.savefig('pieinitial.pdf')
