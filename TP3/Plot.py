from pyexpat.model import XML_CTYPE_EMPTY
import matplotlib.pyplot as plt
import numpy as np
import json

f = open('config.json')
config = json.load(f)
v = config['max_speed']
n = config['quantity']

def plot(x,y,side):
    plt.style.use('default')
    # plot
    fig, ax = plt.subplots()
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.title('Recorrido del centro de la esfera mayor con V: {v} y {n} esferas chicas'.format(v=v, n=n))
    ax.plot(x, y, linewidth=2.0)
    ax.set(xlim=(0, side), xticks=np.arange(0, side, 50),
        ylim=(0, side), yticks=np.arange(0, side, 50))
    ax.plot(x[0], y[0], marker="o", markersize=5, markeredgecolor="red", markerfacecolor="white")
    ax.plot(x[-1], y[-1], marker="o", markersize=5, markeredgecolor="red", markerfacecolor="red")
    plt.savefig('plot.png')
    plt.show()