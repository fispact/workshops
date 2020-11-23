import json
import matplotlib.pyplot as plt


filename = "inventory.json"
ignore_elements = ['Cr', 'Mn', 'Fe', 'Ni']

# parse the json file
with open(filename) as f:
    data = json.load(f)

# -1 in python indicates last entry
timestep = -1
nuclides = data['inventory_data'][timestep]['nuclides']

elements = {}
k = 'element'
v = 'grams'
for n in nuclides:
    if not n[k] in ignore_elements:
        if n[k] in elements:
            elements[n[k]] += n[v]
        else:
            elements[n[k]] = n[v]

total_grams = sum([g for e, g in elements.items()])
for e, g in elements.items():
    print("{} {:.2f}%".format(e, g*100.0/total_grams))
    # we must rescale the values
    elements[e] = g/total_grams

labels, values = list(zip(*(list(elements.items()))))
plt.pie(list(values), labels=list(labels), autopct='%2.2f%%', shadow=False)
plt.savefig('piefinal.pdf')
