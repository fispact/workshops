#!/usr/bin/env python3

import os
import pypact as pp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

filename = 'inventory.out'

with pp.Reader(filename) as output:
    count = len(output)
    
    if count > 0:
        maxEnergy = -1.0
        maxValue  = -1.0
        for t in output:
            if len(t.gamma_spectrum.values) > 0:
                maxValue  = max(maxValue, max(t.gamma_spectrum.values))
                maxEnergy = max(maxEnergy, max(t.gamma_spectrum.boundaries))
            
        fig, ax = plt.subplots()

        bounds = np.linspace(1e-11, 5, 20000, endpoint=True)        
        line, = ax.plot([], [])

        def animate(i):
            gs = output[i].gamma_spectrum
            # overwrite bounds with input since we know that precision causes issues here
            energy = [ (bounds[j] + bounds[j+1])/2.0 for j in range(0, len(bounds) -1) ]
            values = gs.values
            line.set_xdata(energy)  # update the data
            line.set_ydata(values)  # update the data
            return line,

        ani = animation.FuncAnimation(fig, animate, np.arange(0, count),
                                      interval=200, blit=True)
            
        plt.xlim(0, maxEnergy)
        plt.ylim(max(1e1, maxValue*1e-8), max(maxValue*1.2, 1e2))
        plt.xlabel('ENERGY (MeV)')
        plt.ylabel('GAMMA RAY POWER FROM ACTIVATION DECAY (MeV/s)')
        plt.yscale('log')
        plt.grid()
        plt.show()
