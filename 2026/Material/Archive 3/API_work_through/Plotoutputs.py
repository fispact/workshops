import matplotlib.pyplot as plt

# read heating file
def read_heating_file( hfile ):
    heating = []
    time = []

    with open(hfile, 'r') as f:
        data = f.readlines()

    for line in data:
        if "Time" not in line:
            linelist = line.strip().split()
            heating.append( float(linelist[0]) )
            time.append( float(linelist[1]) )

    return heating, time

# read co60 file
def read_co60_file( cfile ):
    time = []
    cells = []
    cellactivity = []

    with open(cfile, 'r') as f:
        data = f.readlines()

    cellflag = False
    timeflag = False
    cellact = []
    for line in data:
        linelist = line.strip().split()

        if len(linelist) == 1:
            cells.append(linelist[0])

        if len(linelist) == 0:
            if cellflag:
                cellactivity.append(cellact)
                cellact = []
            cellflag = False
            timeflag = True


        if cellflag:
            cellact.append( float(linelist[1]) )
            if not timeflag:
                time.append(float(linelist[0]) )

        if "Time" in line:
            cellflag = True

    return time, cells, cellactivity

# plot heating
def plotheating(time, heating):
    plt.plot( time, heating, color="blue", marker="x", linestyle="solid")
    plt.xlabel("Time after irradiation (Years)")
    plt.xscale("log")
    plt.ylabel("Decay Heating (kW/kg)")
    plt.yscale("log")
    plt.grid( color="grey", alpha=0.5, linestyle="dashed")
    plt.title( "Total Component Deacy Heating")
    plt.savefig( "decayheating.png" )
    plt.close()


# plot co60
def plotco60activity(time, cells, cellactivity):
    for i in range(len(cells)):
        plt.plot( time, cellactivity[i], label=cells[i])

    plt.xlabel("Time (Years)")
    plt.xscale("log")
    plt.ylabel("Specific Activity (Bq/kg)")
    plt.yscale("log")
    plt.legend(loc="best")
    plt.grid( color="grey", alpha=0.5, linestyle="dashed")
    plt.title( "Co60 activity in each component cell")
    plt.savefig( "Co60activity.png" )
    plt.close()

# =================================

heatingfile = "component_heating.txt"
time, heating = read_heating_file( heatingfile)
plotheating(time, heating)

co60file = "co60_specific_activity.txt"
time, cells, cellactivity = read_co60_file( co60file )
plotco60activity(time, cells, cellactivity)
