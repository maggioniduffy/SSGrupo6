import matplotlib.pyplot as plt
import numpy as np

def caudales():
    file = open('./caudal015.txt', 'r')
    data = file.read()
    file.close()
    caudales = data.split(':')[1:]
    caudal015 = []
    for line in caudales[0].split('\n')[1:][:-1]:
        caudal015.append(float(line))

    file = open('./caudal018.txt', 'r')
    data = file.read()
    file.close()
    caudales = data.split(':')[1:]
    caudal018 = []
    i = 0
    for line in caudales[0].split('\n')[1:][:-1]:
        if(i < len(caudal015)):
            caudal018.append(float(line))
            i += 1

    file = open('./caudal022.txt', 'r')
    data = file.read()
    file.close()
    caudales = data.split(':')[1:]
    caudal022 = []
    i = 0
    for line in caudales[0].split('\n')[1:][:-1]:
        if(i < len(caudal015)):
            caudal022.append(float(line))
            i += 1

    file = open('./caudal025.txt', 'r')
    data = file.read()
    file.close()
    caudales = data.split(':')[1:]
    caudal025 = []
    i = 0
    for line in caudales[0].split('\n')[1:][:-1]:
        if(i < len(caudal015)):
            caudal025.append(float(line))
            i += 1

    time = np.arange(0, len(caudal015))

    plt.scatter(time/100, caudal015, label='0.15')
    plt.scatter(time/100, caudal018, label='0.18')
    plt.scatter(time/100, caudal022, label='0.22')
    plt.scatter(time/100, caudal025, label='0.25')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Caudal (1/s)')
    plt.legend()
    plt.show()

caudales()