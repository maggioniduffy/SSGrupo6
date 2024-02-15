import matplotlib.pyplot as plt
import numpy as np

def caudales():
    #for(int i = 0; i < outTimes.size()-49 ; i++){
  #  writer.write( (50.0/(outTimes.get(i+49)-outTimes.get(i))) + "\n");
    #}

    window = 100

    file = open('./caudal015.txt', 'r')
    data = file.read()
    file.close()
    caudales = data.split(':')[1:]
    caudal010 = []
    for line in caudales[0].split('\n')[1:][:-1]:
        caudal010.append(float(line))
    caud10 = []
    for i,time in enumerate(caudal010):
        if i + window - 1 < len(caudal010)-(window-1):
            caud10.append(window/(caudal010[i+window-1]-time))

    file = open('./caudal018.txt', 'r')
    data = file.read()
    file.close()
    caudales = data.split(':')[1:]
    caudal012 = []
    for line in caudales[0].split('\n')[1:][:-1]:
        caudal012.append(float(line))
    caud12 = []
    for i,time in enumerate(caudal012):
        if i + window - 1 < len(caudal012)-(window-1):
            caud12.append(window/(caudal012[i+window-1]-time))

    file = open('./caudal020.txt', 'r')
    data = file.read()
    file.close()
    caudales = data.split(':')[1:]
    caudal015 = []
    for line in caudales[0].split('\n')[1:][:-1]:
        caudal015.append(float(line))
    caud15 = []
    for i,time in enumerate(caudal015):
        if i + window - 1 < len(caudal015)-(window-1):
            caud15.append(window/(caudal015[i+window-1]-time))


    file = open('./caudal022.txt', 'r')
    data = file.read()
    file.close()
    caudales = data.split(':')[1:]
    caudal018 = []
    for line in caudales[0].split('\n')[1:][:-1]:
            caudal018.append(float(line))
    caud18 = []
    for i,time in enumerate(caudal018):
        if i + window - 1 < len(caudal018)-(window-1):
            caud18.append(window/(caudal018[i+window-1]-time))


    #time = np.arange(0, len(caud10))
    time10 = np.linspace(0, 7.5, len(caud10))
    time12 = np.linspace(0, 7.5, len(caud12))
    time15 = np.linspace(0, 7.5, len(caud15))
    time18 = np.linspace(0, 7.5, len(caud18))
    plt.scatter(time10, caud10, label='0.15')
    plt.scatter(time12, caud12, label='0.18')
    plt.scatter(time15, caud15, label='0.20')
    plt.scatter(time18, caud18, label='0.22')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Caudal (1/s)')
    plt.legend(prop={'size': 12})
    plt.show()

caudales()