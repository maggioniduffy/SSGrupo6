from unittest import skip
import matplotlib.pyplot as plt
import numpy as np
import statistics
import os

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

def countprop():
    files = [f for f in os.listdir("./") if f.startswith('rmi') and os.path.isfile(os.path.join("./", f))]
    sim_count = len(files)
    cut_cond_count = {5000: [], 16250: [], 27500: [], 38750: [], 50000: []}
    for f in files:
        file = open(f, 'r')
        speed = int(f.split("_")[2].split(".")[0])
        data = file.read()
        data = data.split("\n")
        cut_cond = data[-1]
        cut_cond_count[speed].append(cut_cond)
    absorbed = []
    left = []
    right = []
    bottom = []
    top = []
    for key in cut_cond_count:
        results = cut_cond_count[key]
        absorbed.append(results.count("Absorbed"))
        left.append(results.count("Left"))
        right.append(results.count("Right"))
        bottom.append(results.count("Bottom"))
        top.append(results.count("Top"))
        
    plt.plot(cut_cond_count.keys, [(number/15)*100 for number in absorbed], marker='o', label="Absorbed")
    plt.plot(cut_cond_count.keys, [(number/15)*100 for number in left], marker='o', label='Left')
    plt.plot(cut_cond_count.keys, [(number/15)*100 for number in right], marker='o', label='Right')
    plt.plot(cut_cond_count.keys, [(number/15)*100 for number in bottom], marker='o', label='Bottom')
    plt.plot(cut_cond_count.keys, [(number/15)*100 for number in top], marker='o', label='Top')
    plt.xlabel('Velocidad (m/s)')
    plt.ylabel('Porcentaje (%)')
    plt.legend()
    plt.ylim([-5,100])
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
    plt.show()

def place_in_bins(value, bins, interval_size):
    stop = False
    bins = np.array(bins)
    aux = bins.copy()
    n = 1
    while not stop:
        if value <= interval_size * n:
            aux[n-1] = aux[n-1] + 1
            stop = True
        else:
            n += 1 
    return aux

def prob_dist():
    files = [f for f in os.listdir("./") if f.startswith('absorbed') and os.path.isfile(os.path.join("./", f))]
    trayectories = {5000: [], 16250: [], 27500: [], 38750: [], 50000: []}
    aux = []
    for f in files:
        file = open(f, 'r')
        speed = int(f.split("_")[2].split(".")[0])
        data = float(file.read())
        aux.append(data)
        trayectories[speed].append(data)

    for speed in trayectories.keys():
        bin_size = sum(trayectories[speed])/len(trayectories[speed])
        bin_ammount = len(trayectories[speed])
        bins = np.zeros(bin_ammount) #ver cuantos bins poner por cada speed (nose si es asi tampoco)
        intervals = np.arange(0, bin_size*len(bins), step=bin_size)
        for tr in trayectories[speed]:
            bins = place_in_bins(tr, bins, bin_size)
        plt.plot(intervals, bins/len(bins), label=(str(speed)+" m/s"))
        print(trayectories[speed])
        print(bins)
        print("-------")
    plt.xlabel('Trayectoria (m)')
    plt.ylabel('Probabilidad')
    plt.legend()
    plt.show()
#energies()
#longT()
#countprop()
prob_dist()