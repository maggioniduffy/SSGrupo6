import matplotlib.pyplot as plt
import numpy as np

def caudal():

    #0.25
    file = open('./caudal025.txt', 'r')
    data = file.read()
    file.close()
    caudales = data.split(':')[1:]
    caudal025 = []
    for line in caudales[0].split('\n')[1:][:-1]:
        caudal025.append(float(line))

    #0.50
    file = open('./caudal050.txt', 'r')
    data = file.read()
    file.close()
    caudales = data.split(':')[1:]
    caudal050 = []
    for line in caudales[0].split('\n')[1:][:-1]:
        caudal050.append(float(line))

    #0.75
    file = open('./caudal075.txt', 'r')
    data = file.read()
    file.close()
    caudales = data.split(':')[1:]
    caudal075 = []
    for line in caudales[0].split('\n')[1:][:-1]:
        caudal075.append(float(line))

    #1.00
    file = open('./caudal0100.txt', 'r')
    data = file.read()
    file.close()
    caudales = data.split(':')[1:]
    caudal100 = []
    for line in caudales[0].split('\n')[1:][:-1]:
        caudal100.append(float(line))

    dt = 0.00005
    time = np.arange(0, 100001*dt, dt)

    eqtimes = []
    i = 0
    for t in time:
        if t >= 0.25 and time[i-1] < 0.25:
            eqtimes.append(i)
        if t >= 0.50 and time[i-1] < 0.50:
            eqtimes.append(i)
        if t >= 0.75 and time[i-1] < 0.75:
            eqtimes.append(i)
        if t >= 1.00 and time[i-1] < 1.00:
            eqtimes.append(i)
        i += 1
    print(eqtimes)
    proms = [0,0,0,0]
    i = 0
    min = caudal025[eqtimes[0]]
    max = 0
    for k in caudal025:
        if i >= eqtimes[0]:
            proms[0] += k
            if k < min:
                min = k
            if k > max:
                max = k
        i += 1
    proms[0] = proms[0]/(100000-eqtimes[0])
    minmax025 = (proms[0]-min, max-proms[0])
    
    i = 0
    min = caudal050[eqtimes[1]]
    max = 0
    for k in caudal050:
        if i >= eqtimes[1]:
            proms[1] += k
            if k < min:
                min = k
            if k > max:
                max = k
        i += 1
    proms[1] = proms[1]/(100000-eqtimes[1])
    minmax050 = (proms[1]-min, max-proms[1])
    
    i = 0
    min = caudal075[eqtimes[2]]
    max = 0
    for k in caudal075:
        if i >= eqtimes[2]:
            proms[2] += k
            if k < min:
                min = k
            if k > max:
                max = k
        i += 1
    proms[2] = proms[2]/(100000-eqtimes[2])
    minmax075 = (proms[2]-min, max-proms[2])
    
    i = 0
    min = caudal100[eqtimes[3]]
    max = 0
    for k in caudal100:
        if i >= eqtimes[3]:
            proms[3] += k
            if k < min:
                min = k
            if k > max:
                max = k
        i += 1
    proms[3] = proms[3]/(100000-eqtimes[3])
    minmax100 = (proms[3]-min, max-proms[3])

    yerr = np.array([minmax025, minmax050, minmax075, minmax100]).T
    kts = [0.25, 0.50, 0.75, 1.00]

    plt.errorbar(kts, proms, yerr, fmt='o')
    plt.yscale("log")
    plt.xlabel('Abertura del silo (m)')
    plt.ylabel('Caudal (m³/s)')
    plt.show()

caudal()
