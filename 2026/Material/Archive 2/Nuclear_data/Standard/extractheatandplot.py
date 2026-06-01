import matplotlib.pyplot as plt

def extaractheating(fiioutputfile):
    heating = []
    with open( fiioutputfile, 'r' ) as f:
        data = f.readlines()
    
    for line in data:
        if "TOTAL HEAT PRODUCTION" in line:
            linelist = line.strip().split()
            heating.append( float(linelist[-2]))

    return heating[1:]

# ======================================================================

# extract heating form tendl results
heating_t21 = extaractheating("TENDL2021/TENDL21.out")
# extract heating form jeff results
heating_jeff = extaractheating("JEFF/JEFF.out")
# extract heating from endfb results
heating_en = extaractheating("ENDFB/ENDFB.out")

time = [i for i in range(len(heating_en))]

plt.plot( time, heating_t21, color="red", linestyle="solid", marker="x", markevery=3, label="TENDL2021")
plt.plot( time, heating_jeff, color="blue",linestyle="dashed", marker="o", markevery=3,  label="JEFF3.3")
plt.plot( time, heating_en, color="green", linestyle="dotted", marker="^", markevery=2, label="ENDFB8")
plt.legend(loc="best")
plt.grid(linestyle="solid", color="grey", alpha=0.5)
plt.xlabel("Cooling Time (mins)")
plt.ylabel("Deacy Heating (kW)")
plt.yscale("log")
plt.title("Os Decay Heating with different Nuclear Data using\nstandard FISPACT-II")
plt.show()