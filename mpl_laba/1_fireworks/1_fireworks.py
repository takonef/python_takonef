import matplotlib.pyplot as plt
import numpy as np
import os

def ploto(filename):
    x = []
    y = []
    
    with open(filename, 'r') as f:
        lines = f.readlines()
        
        n_points = int(lines[0].strip())
        for line in lines[1:]:
            t = line.strip().split()
            if len(t) >= 2:
                x.append(float(t[0]))
                y.append(float(t[1]))

    plt.scatter(x, y, s=25)
    plt.gca().set_aspect('equal', adjustable='datalim')
    plt.title(f"Number of points: {len(x)}", fontsize=16)
    plt.grid(True, linestyle='--', alpha=0.6)
    # print((filename.split('\\')[1]).split('.')[0] + '.png')
    plt.savefig((filename.split('\\')[1]).split('.')[0] + '.png')
    plt.show()

for i in range(1, 6):
    filename = "dead_moroz\\" + "00" + str(i) + ".dat"
    ploto(filename)
    