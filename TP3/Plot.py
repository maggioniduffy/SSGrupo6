from pyexpat.model import XML_CTYPE_EMPTY
from config_loader import v,n
import matplotlib.pyplot as plt
import numpy as np

def big_sphere_journey(x,y,side):
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
    name = 'bigspherejourney_v{v}n{n}.png'.format(v=v, n=n)
    plt.savefig(name)
    plt.show()

def collision_times_distribution(y,size):
    plt.style.use('default')
    fig, ax = plt.subplots()
    plt.title('DFC v={v}, N={n}'.format(v=v, n=n))
    plt.xlabel('Segundos')
    plt.ylabel('')
    x = np.arange(0,len(y)*size,step=size)
    ymax = np.amax(y)
    ax.bar(x, y, width=size, edgecolor="white", linewidth=0.7)
    ax.set(xlim=(0-(size/2), len(x)*size), xticks=x,
        ylim=(0, ymax+100), yticks=np.arange(0, ymax+0.001, step=ymax/10))
    name = 'colltimedistribution_v{v}n{n}.png'.format(v=v, n=n)
    plt.savefig(name)
    plt.show()