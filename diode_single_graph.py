#format of read file: .txt
"""
x_axis_data y_axis_data
"""

import numpy as np
import matplotlib.pyplot as plt

def plotFile(path, colourchar,plotlabel):
    with open(path) as f:
        lines = f.readlines()
        x = [float(line.split()[0]) for line in lines]
        y = [float(line.split()[1]) for line in lines]
        
        plt.plot(x, y, c=colourchar, label=plotlabel)


path1 = '/home/leo/Downloads/30l.txt' 
path2 = '/home/leo/Downloads/60l.txt'
path3 = '/home/leo/Downloads/90l.txt' 

plotFile(path1, 'b', '30°C')
plotFile(path2, 'r', '60°C')
plotFile(path3, 'g', '90°C')

plt.legend()
plt.grid(True)
plt.title("I(u)")
plt.xlabel("voltage (V)")
plt.ylabel("current (I)")

plt.show()
