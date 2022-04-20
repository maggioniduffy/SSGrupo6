from pyexpat.model import XML_CTYPE_EMPTY
from config_loader import v,n
import matplotlib.pyplot as plt
import numpy as np

def big_sphere_journey(x,y,side):
    #y.reverse()
    aux_y = []
    for yi in y:
        dif = yi - 300
        aux_y.append(300-dif)
    plt.style.use('default')
    # plot
    fig, ax = plt.subplots()
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.title('Recorrido del centro de la esfera mayor con V: {v} y {n} esferas chicas'.format(v=v, n=n))
    ax.plot(x, aux_y, linewidth=2.0)
    ax.set(xlim=(0, side), xticks=np.arange(0, side, 50),
        ylim=(0, side), yticks=np.arange(0, side, 50))
    ax.plot(x[0], aux_y[0], marker="o", markersize=5, markeredgecolor="red", markerfacecolor="white")
    ax.plot(x[-1], aux_y[-1], marker="o", markersize=5, markeredgecolor="red", markerfacecolor="red")
    name = 'bigspherejourney_v{v}n{n}.png'.format(v=v, n=n)
    plt.savefig(name)
    plt.grid()
    plt.show()

def graphic(y,size, ylabel = 'Distribucion', xlabel = 'Tiempo entre colisiones (s)'):
    plt.style.use('default')
    fig, ax = plt.subplots()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    x = np.arange(0,len(y)*size,step=size)
    ymax = np.amax(y)
    ax.bar(x, y, width=size, edgecolor="white", linewidth=0.7)
    ax.set(xlim=(0-(size/2), len(x)*size), xticks=x,
        ylim=(0, ymax+0.001), yticks=np.arange(0, ymax, step=ymax/10))
    name = 'graphic_{ylabel},{v}n{n}.png'.format(ylabel=ylabel, v=v, n=n)
    plt.savefig(name)
    plt.show()