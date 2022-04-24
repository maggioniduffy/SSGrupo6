from cProfile import label
from pyexpat.model import XML_CTYPE_EMPTY
from config_loader import v,n, ct_interval_size
import matplotlib.pyplot as plt
import numpy as np
import math

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

def pdf(interval_size,file,xlabel = 'Tiempo entre colisiones (s)', isInitial=False):
    ylabel = 'PDF'
    plt.style.use('default')
    fig, ax = plt.subplots()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(loc="upper left")
    f = open(file,'r')
    data = f.read()
    ymax = 0
    f.close()
    runs = data.split('run\n')[1:]
    colors = ['red','green','blue']
    j = 0
    for run in runs:
        lines = run.split('\n')
        n = lines[0].split('=')[-1]
        y = lines[1:][:-1]
        y = list(map(lambda y : float(y), y))
        n_max = np.amax(y)
        ymax = n_max if n_max > ymax else ymax
        step = interval_size if not isInitial else interval_size * 6
        x_i = np.arange(0,len(y)*step,step=step)
        ax.plot(x_i, y, label=str(n))
        ax.legend()
        for i in range(0,len(x_i)):
            ax.plot(x_i[i],y[i],'o', color=colors[j])
        j += 1
        name = 'pdf:{v}n{n}.png'.format(ylabel=ylabel, v=v, n=n)
    
    x = np.arange(0,20*interval_size,step=interval_size*3)
    ax.set(xlim=(0, len(x)*interval_size), xticks=x,
        ylim=(0, ymax+0.0015), yticks=np.arange(0, ymax, step=ymax/10))
    ax.grid()
    plt.savefig(name)
    plt.show()
    
def pdf_speeds(interval_size,colors,file,xlabel = 'Tiempo entre colisiones (s)', isInitial=False):
    ylabel = 'PDF'
    plt.style.use('default')
    fig, ax = plt.subplots()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(loc="upper left")
    f = open(file,'r')
    data = f.read()
    ymax = 0
    f.close()
    runs = data.split('run\n')[1:]
    j = 0
    for run in runs:
        lines = run.split('\n')
        n = lines[0].split('=')[-1]
        y = lines[1:][:-1]
        y = list(map(lambda y : float(y), y))
        n_max = np.amax(y)
        ymax = n_max if n_max > ymax else ymax
        x_i = np.arange(0,len(y)*0.25,step=interval_size)
        
        ax.plot(x_i, y, label=str(n))
        ax.legend()
        for i in range(0,len(x_i)):
            ax.plot(x_i[i],y[i],'o', color=colors[j])
        j += 1
        name = 'pdf:{v}n{n}.png'.format(ylabel=ylabel, v=v, n=n)
    
    x = np.arange(0,10*interval_size,step=interval_size)
    ax.set(xlim=(0, 10*interval_size), xticks=x,
        ylim=(0, ymax+0.0015), yticks=np.arange(0, ymax, step=ymax/10))
    ax.grid()
    plt.savefig(name)
    plt.show()