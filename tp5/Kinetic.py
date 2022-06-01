import matplotlib.pyplot as plt
import numpy as np

def kinetic():
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

    file = open('./kinetic022.txt', 'r')
    data = file.read()
    file.close()
    kinetics = data.split(':')[1:]
    kinetic022 = []
    for line in kinetics[0].split('\n')[1:][:-1]:
        kinetic022.append(float(line))

    file = open('./kinetic025.txt', 'r')
    data = file.read()
    file.close()
    kinetics = data.split(':')[1:]
    kinetic025 = []
    for line in kinetics[0].split('\n')[1:][:-1]:
        kinetic025.append(float(line))

    time = np.arange(0, len(kinetic015))

    plt.loglog(time/100, kinetic015, label='0.15')
    plt.loglog(time/100, kinetic018, label='0.18')
    plt.loglog(time/100, kinetic022, label='0.22')
    plt.loglog(time/100, kinetic025, label='0.25')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Energia Cinetica (J)')
    plt.legend()
    plt.show()

kinetic()