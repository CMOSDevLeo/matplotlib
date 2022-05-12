"""
TODO: 
- add data of "right diode"
- label all the x and y axis 
- add overall title


Format of read file: .txt

x_axis_data y_axis_data
"""

import numpy as np
import matplotlib.pyplot as plt

def plotFile(path, ax, colourchar, plotlabel):
    with open(path) as f:
        lines = f.readlines()
        x = [float(line.split()[0]) for line in lines]
        y = [float(line.split()[1]) for line in lines]
        
        ax.plot(x, y, c=colourchar, label=plotlabel)

fig, (ax1, ax2) = plt.subplots(2) # for two graphs over each other

path1 = '/home/leo/Downloads/30l.txt' 
path2 = '/home/leo/Downloads/60l.txt'
path3 = '/home/leo/Downloads/90l.txt' 

plotFile(path1, ax1, 'b', '30°C')
plotFile(path2, ax1, 'r', '60°C')
plotFile(path3, ax2, 'g', '90°C')

plt.legend()
ax1.grid(True) # there must be a way to add a grid to both of the graphs at the same time
ax2.grid(True)
plt.title("I(u)")
plt.xlabel("voltage (V)")
plt.ylabel("current (I)")

plt.show()
