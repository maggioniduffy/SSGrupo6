import matplotlib.pyplot as plt
import numpy as np

def kinetic():
    file = open('./kinetic05kn.txt', 'r')
    data = file.read()
    file.close()
    kinetics = data.split(':')[1:]
    kinetic05kn = []
    for line in kinetics[0].split('\n')[1:][:-1]:
        kinetic05kn.append(float(line))

    file = open('./kinetickn.txt', 'r')
    data = file.read()
    file.close()
    kinetics = data.split(':')[1:]
    kinetickn = []
    for line in kinetics[0].split('\n')[1:][:-1]:
        kinetickn.append(float(line))

    file = open('./kinetic2kn.txt', 'r')
    data = file.read()
    file.close()
    kinetics = data.split(':')[1:]
    kinetic2kn = []
    for line in kinetics[0].split('\n')[1:][:-1]:
        kinetic2kn.append(float(line))

    file = open('./kinetic3kn.txt', 'r')
    data = file.read()
    file.close()
    kinetics = data.split(':')[1:]
    kinetic3kn = []
    for line in kinetics[0].split('\n')[1:][:-1]:
        kinetic3kn.append(float(line))

    dt = 0.00001

    time = np.arange(0, 500001*dt, dt)

    plt.plot(time, kinetic05kn, label='0.5kn')
    plt.plot(time, kinetickn, label='kn')
    plt.plot(time, kinetic2kn, label='2kn')
    plt.plot(time, kinetic3kn, label='3kn')
    plt.yscale("log")
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Energia Cinetica (J)')
    plt.legend()
    plt.show()

kinetic()