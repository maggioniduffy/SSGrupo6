import matplotlib.pyplot as plt
import numpy as np

def kinetic():

    #0.88
    file = open('./kinetic05kn.txt', 'r')
    data = file.read()
    file.close()
    kinetics = data.split(':')[1:]
    kinetic05kn = []
    for line in kinetics[0].split('\n')[1:][:-1]:
        kinetic05kn.append(float(line))

    #0.72
    file = open('./kinetickn.txt', 'r')
    data = file.read()
    file.close()
    kinetics = data.split(':')[1:]
    kinetickn = []
    for line in kinetics[0].split('\n')[1:][:-1]:
        kinetickn.append(float(line))

    #0.44
    file = open('./kinetic2kn.txt', 'r')
    data = file.read()
    file.close()
    kinetics = data.split(':')[1:]
    kinetic2kn = []
    for line in kinetics[0].split('\n')[1:][:-1]:
        kinetic2kn.append(float(line))

    #0.43
    file = open('./kinetic3kn.txt', 'r')
    data = file.read()
    file.close()
    kinetics = data.split(':')[1:]
    kinetic3kn = []
    for line in kinetics[0].split('\n')[1:][:-1]:
        kinetic3kn.append(float(line))

    dt = 0.00001
    time = np.arange(0, 500001*dt, dt)

    eqtimes = []
    i = 0
    for t in time:
        if t >= 0.43 and time[i-1] < 0.43:
            eqtimes.append(i)
        if t >= 0.44 and time[i-1] < 0.44:
            eqtimes.append(i)
        if t >= 0.72 and time[i-1] < 0.72:
            eqtimes.append(i)
        if t >= 0.88 and time[i-1] < 0.88:
            eqtimes.append(i)
        i += 1

    proms = [0,0,0,0]
    i = 0
    min = kinetic05kn[eqtimes[3]]
    max = 0
    for k in kinetic05kn:
        if i >= eqtimes[3]:
            proms[0] += k
            if k < min:
                min = k
            if k > max:
                max = k
        i += 1
    proms[0] = proms[0]/(500000-eqtimes[3])
    minmax05kn = (proms[0]-min, max-proms[0])
    i = 0
    min = kinetic05kn[eqtimes[2]]
    max = 0
    for k in kinetickn:
        if i >= eqtimes[2]:
            proms[1] += k
            if k < min:
                min = k
            if k > max:
                max = k
        i += 1
    proms[1] = proms[1]/(500000-eqtimes[2])
    minmaxkn = (proms[1]-min, max-proms[1])
    i = 0
    min = kinetic05kn[eqtimes[1]]
    max = 0
    for k in kinetic2kn:
        if i >= eqtimes[1]:
            proms[2] += k
            if k < min:
                min = k
            if k > max:
                max = k
        i += 1
    proms[2] = proms[2]/(500000-eqtimes[1])
    minmax2kn = (proms[2]-min, max-proms[2])
    i = 0
    min = kinetic05kn[eqtimes[0]]
    max = 0
    for k in kinetic3kn:
        if i >= eqtimes[0]:
            proms[3] += k
            if k < min:
                min = k
            if k > max:
                max = k
        i += 1
    proms[3] = proms[3]/(500000-eqtimes[0])
    minmax3kn = (proms[3]-min, max-proms[3])

    yerr = np.array([minmax05kn, minmaxkn, minmax2kn, minmax3kn]).T
    kts = [0.5, 1, 2, 3]


    #plt.plot(time, kinetic05kn, label='0.5kn')
    #plt.plot(time, kinetickn, label='kn')
    #plt.plot(time, kinetic2kn, label='2kn')
    #plt.plot(time, kinetic3kn, label='3kn')
    #plt.yscale("log")
    #plt.xlabel('Tiempo (s)')
    #plt.ylabel('Energia Cinetica (J)')
    #plt.legend(prop={'size': 12})
    #plt.show()

    plt.errorbar(kts, proms, yerr, fmt='o')
    plt.yscale("log")
    plt.xlabel('kt (kn)')
    plt.ylabel('Energia Residual (J)')
    plt.show()

kinetic()