import matplotlib.pyplot as plt
import numpy as np

def kinetic():
    file = open('./kinetic010.txt', 'r')
    data = file.read()
    file.close()
    kinetics = data.split(':')[1:]
    kinetic010 = []
    for line in kinetics[0].split('\n')[1:][:-1]:
        kinetic010.append(float(line))

    file = open('./kinetic012.txt', 'r')
    data = file.read()
    file.close()
    kinetics = data.split(':')[1:]
    kinetic012 = []
    for line in kinetics[0].split('\n')[1:][:-1]:
        kinetic012.append(float(line))

    file = open('./kinetic015.txt', 'r')
    data = file.read()
    file.close()
    kinetics = data.split(':')[1:]
    kinetic015 = []
    for line in kinetics[0].split('\n')[1:][:-1]:
        kinetic015.append(float(line))

    file = open('./kinetic018.txt', 'r')
    data = file.read()
    file.close()
    kinetics = data.split(':')[1:]
    kinetic018 = []
    for line in kinetics[0].split('\n')[1:][:-1]:
        kinetic018.append(float(line))

    dt = 0.00001

    time = np.arange(0, 500001*dt, dt)

    plt.plot(time, kinetic010, label='0.1')
    plt.plot(time, kinetic012, label='0.12')
    plt.plot(time, kinetic015, label='0.15')
    plt.plot(time, kinetic018, label='0.18')
    plt.yscale("log")
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Energia Cinetica (J)')
    plt.legend(prop={'size': 12})
    plt.show()

kinetic()