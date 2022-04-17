import matplotlib.pyplot as plt
import numpy as np

def plot(x,y,side):
    plt.style.use('default')
    plt.xlabel('X')
    plt.ylabel('Y')
    # plot
    fig, ax = plt.subplots()
    print(x[-1], y[-1])
    ax.plot(x, y, linewidth=2.0)
    ax.set(xlim=(0, side), xticks=np.arange(1, side, 50),
        ylim=(0, side), yticks=np.arange(1, side, 50))
    plt.savefig('plot.png')
    plt.show()