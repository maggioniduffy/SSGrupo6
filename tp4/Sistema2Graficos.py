import matplotlib.pyplot as plt
import numpy as np
import statistics

def energies():
    file = open('./energies1e-15.txt', 'r')
    data = file.read()
    file.close()
    energies = data.split(':')[1:]
    energies15 = []
    for line in energies[0].split('\n')[1:][:-1]:
        energies15.append(float(line))
    i = 0
    for line in energies[1].split('\n')[1:][:-1]:
        if(i < len(energies15)):
            energies15[i] += float(line)
            i += 1
    i = 0
    for line in energies[2].split('\n')[1:][:-1]:
        if(i < len(energies15)):
            energies15[i] += float(line)
            i += 1
    i = 0
    for line in energies[3].split('\n')[1:][:-1]:
        if(i < len(energies15)):
            energies15[i] += float(line)
            i += 1
    i = 0
    for line in energies[4].split('\n')[1:][:-1]:
        if(i < len(energies15)):
            energies15[i] = (energies15[i] + float(line))/5
            i += 1

    file = open('./energies1e-16.txt', 'r')
    data = file.read()
    file.close()
    energies = data.split(':')[1:]
    energies16 = []
    for line in energies[0].split('\n')[1:][:-1]:
        energies16.append(float(line))
    i = 0
    for line in energies[1].split('\n')[1:][:-1]:
        if(i < len(energies16)):
            energies16[i] += float(line)
            i += 1
    i = 0
    for line in energies[2].split('\n')[1:][:-1]:
        if(i < len(energies16)):
            energies16[i] += float(line)
            i += 1
    i = 0
    for line in energies[3].split('\n')[1:][:-1]:
        if(i < len(energies16)):
            energies16[i] += float(line)
            i += 1
    i = 0
    for line in energies[4].split('\n')[1:][:-1]:
        if(i < len(energies16)):
            energies16[i] = (energies16[i] + float(line))/5
            i += 1

    file = open('./energies1e-17.txt', 'r')
    data = file.read()
    file.close()
    energies = data.split(':')[1:]
    energies17 = []
    for line in energies[0].split('\n')[1:][:-1]:
        energies17.append(float(line))
    i = 0
    for line in energies[1].split('\n')[1:][:-1]:
        if(i < len(energies17)):
            energies17[i] += float(line)
            i += 1
    i = 0
    for line in energies[2].split('\n')[1:][:-1]:
        if(i < len(energies17)):
            energies17[i] += float(line)
            i += 1
    i = 0
    for line in energies[3].split('\n')[1:][:-1]:
        if(i < len(energies17)):
            energies17[i] += float(line)
            i += 1
    i = 0
    for line in energies[4].split('\n')[1:][:-1]:
        if(i < len(energies17)):
            energies17[i] = (energies17[i] + float(line))/5
            i += 1

    file = open('./energies1e-18.txt', 'r')
    data = file.read()
    file.close()
    energies = data.split(':')[1:]
    energies18 = []
    for line in energies[0].split('\n')[1:][:-1]:
        energies18.append(float(line))
    i = 0
    for line in energies[1].split('\n')[1:][:-1]:
        if(i < len(energies18)):
            energies18[i] += float(line)
            i += 1
    i = 0
    for line in energies[2].split('\n')[1:][:-1]:
        if(i < len(energies18)):
            energies18[i] += float(line)
            i += 1
    i = 0
    for line in energies[3].split('\n')[1:][:-1]:
        if(i < len(energies18)):
            energies18[i] += float(line)
            i += 1
    i = 0
    for line in energies[4].split('\n')[1:][:-1]:
        if(i < len(energies18)):
            energies18[i] = (energies18[i] + float(line))/5
            i += 1

    dt15 = (1e-15)*50
    time15 = np.arange(0, len(energies15)*dt15, dt15)
    dt16 = (1e-16)*50
    time16 = np.arange(0, len(energies16)*dt16, dt16)
    dt17 = (1e-17)*50
    time17 = np.arange(0, len(energies17)*dt17, dt17)
    dt18 = (1e-18)*50
    time18 = np.arange(0, len(energies18)*dt18, dt18)

    plt.loglog(time15, energies15, label='1e-15')
    plt.loglog(time16, energies16, label='1e-16')
    plt.loglog(time17, energies17, label='1e-17')
    plt.loglog(time18, energies18, label='1e-18')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Promedio Diferencias Relativas')
    plt.legend()
    plt.show()

def longT():
    V0s = [5000, 16250, 27500, 38750, 50000]

    file = open('./longT5000.txt', 'r')
    data = file.read()
    file.close()
    longs = data.split(':')[1:]
    longT = []
    long5000 = []
    longT.append(float(longs[0].split('\n')[1:][:-1][0]))
    long5000.append(float(longs[0].split('\n')[1:][:-1][0]))
    for i in range(1,14):
        longT[0] += float(longs[i].split('\n')[1:][:-1][0])
        long5000.append(float(longs[i].split('\n')[1:][:-1][0]))
    longT[0] = longT[0]/15
    file = open('./longT16250.txt', 'r')
    data = file.read()
    file.close()
    longs = data.split(':')[1:]
    long16250 = []
    longT.append(float(longs[0].split('\n')[1:][:-1][0]))
    long16250.append(float(longs[0].split('\n')[1:][:-1][0]))
    for i in range(1,14):
        longT[1] += float(longs[i].split('\n')[1:][:-1][0])
        long16250.append(float(longs[i].split('\n')[1:][:-1][0]))
    longT[1] = longT[1]/15
    file = open('./longT27500.txt', 'r')
    data = file.read()
    file.close()
    longs = data.split(':')[1:]
    long27500 = []
    longT.append(float(longs[0].split('\n')[1:][:-1][0]))
    long27500.append(float(longs[0].split('\n')[1:][:-1][0]))
    for i in range(1,14):
        longT[2] += float(longs[i].split('\n')[1:][:-1][0])
        long27500.append(float(longs[i].split('\n')[1:][:-1][0]))
    longT[2] = longT[2]/15
    file = open('./longT38750.txt', 'r')
    data = file.read()
    file.close()
    longs = data.split(':')[1:]
    long38750 = []
    longT.append(float(longs[0].split('\n')[1:][:-1][0]))
    long38750.append(float(longs[0].split('\n')[1:][:-1][0]))
    for i in range(1,14):
        longT[3] += float(longs[i].split('\n')[1:][:-1][0])
        long38750.append(float(longs[i].split('\n')[1:][:-1][0]))
    longT[3] = longT[3]/15
    file = open('./longT50000.txt', 'r')
    data = file.read()
    file.close()
    longs = data.split(':')[1:]
    long50000 = []
    longT.append(float(longs[0].split('\n')[1:][:-1][0]))
    long50000.append(float(longs[0].split('\n')[1:][:-1][0]))
    for i in range(1,14):
        longT[4] += float(longs[i].split('\n')[1:][:-1][0])
        long50000.append(float(longs[i].split('\n')[1:][:-1][0]))
    longT[4] = longT[4]/15
    std = []
    std.append(statistics.stdev(long5000))
    std.append(statistics.stdev(long16250))
    std.append(statistics.stdev(long27500))
    std.append(statistics.stdev(long38750))
    std.append(statistics.stdev(long50000))


    plt.errorbar(V0s, longT, std, marker='o')
    plt.xlabel('V0 (m/s)')
    plt.ylabel('Longitud de Trayectoria (m)')
    plt.legend()
    plt.show()

#energies()
longT()