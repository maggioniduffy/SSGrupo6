import matplotlib.pyplot as plt
import numpy as np

def plot(x,y):
    print(x,y)
    plt.style.use('default')
    # plot
    fig, ax = plt.subplots()

    ax.plot(x, y, linewidth=2.0)
    xmax, ymax = int(np.amax(x)) + 1, int(np.amax(y)) + 1

    ax.set(xlim=(0, xmax), xticks=np.arange(1, xmax),
        ylim=(0, ymax), yticks=np.arange(1, ymax))

    plt.show()