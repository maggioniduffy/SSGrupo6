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
    i = 0
    for line in caudales[1].split('\n')[1:][:-1]:
        if(i < len(caudal015)):
            caudal015[i] += float(line)
            i += 1
    i = 0
    for line in caudales[2].split('\n')[1:][:-1]:
        if(i < len(caudal015)):
            caudal015[i] += float(line)
            i += 1
    i = 0
    for line in caudales[3].split('\n')[1:][:-1]:
        if(i < len(caudal015)):
            caudal015[i] = (caudal015[i] + float(line))/4
            i += 1

    time015 = np.arange(0, len(caudal015))

    plt.loglog(time015, caudal015, label='0.15')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Caudal (1/s)')
    plt.legend()
    plt.show()