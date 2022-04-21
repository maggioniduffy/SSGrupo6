from config_loader import side,v,n
import matplotlib.pyplot as plt
import numpy as np

def save_big_sphere_journey(x,y):
    f = open('./bigsphere.txt','a')
    f.write('run\n')
    f.write('v:{v}\n'.format(v=v))
    for i in range(0,len(x)):
        f.write('{x},{y}\n'.format(x=x[i],y=y[i]))
    f.close()

def plot_big_sphere_journey():
    plt.style.use('default')
    # plot
    fig, ax = plt.subplots()
    ax.set(xlim=(0, side), xticks=np.arange(0, side, 50),
        ylim=(0, side), yticks=np.arange(0, side, 50))
    ax.grid()
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    f = open('./bigsphere.txt','r')
    travel = f.read()
    f.close()
    runs = travel.split('run\n')[1:]
    for r in runs:
        x = []
        y = []
        positions = r.split('\n')[1:][:-1]
        for line in positions:
            coordinates = line.split(',')
            xi, yi = float(coordinates[0]), float(coordinates[1])
            x.append(xi)
            dif = yi - 300
            y.append(300-dif)
        ax.plot(x,y)
        ax.plot(x[0], y[0], marker="o", markersize=5, markeredgecolor="red", markerfacecolor="white")
        ax.plot(x[-1], y[-1], marker="o", markersize=5, markeredgecolor="red", markerfacecolor="red")

    name = 'bigspherejourney_.png'.format(v=v, n=n)
    plt.savefig(name)
    plt.show()

plot_big_sphere_journey()