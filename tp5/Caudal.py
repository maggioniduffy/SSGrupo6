import matplotlib.pyplot as plt
import numpy as np

def caudales():
    #for(int i = 0; i < outTimes.size()-49 ; i++){
  #  writer.write( (50.0/(outTimes.get(i+49)-outTimes.get(i))) + "\n");
    #}

    window = 70

    file = open('./caudal010.txt', 'r')
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

    file = open('./caudal015.txt', 'r')
    data = file.read()
    file.close()
    caudales = data.split(':')[1:]
    caudal015 = []
    j = 0
    for line in caudales[0].split('\n')[1:][:-1]:
        caudal015.append(float(line))
    caud15 = []
    for i,time in enumerate(caudal015):
        if i + window - 1 < len(caudal015)-(window-1):
            if(j < len(caud10)):
                caud15.append(window/(caudal015[i+window-1]-time))
                j += 1


    file = open('./caudal018.txt', 'r')
    data = file.read()
    file.close()
    caudales = data.split(':')[1:]
    caudal018 = []
    j = 0
    for line in caudales[0].split('\n')[1:][:-1]:
            caudal018.append(float(line))
    caud18 = []
    for i,time in enumerate(caudal018):
        if i + window - 1 < len(caudal018)-(window-1):
            if(j < len(caud10)):
                caud18.append(window/(caudal018[i+window-1]-time))
                j += 1

    file = open('./caudal022.txt', 'r')
    data = file.read()
    file.close()
    caudales = data.split(':')[1:]
    caudal022 = []
    j = 0
    for line in caudales[0].split('\n')[1:][:-1]:
            caudal022.append(float(line))
    caud22 = []
    for i,time in enumerate(caudal022):
        if i + window - 1 < len(caudal022)-(window-1):
            if(j < len(caud10)):
                caud22.append(window/(caudal022[i+window-1]-time))
                j += 1

    #time = np.arange(0, len(caud10))
    time = np.linspace(0, 5, len(caud10))
    plt.scatter(time, caud10, label='0.1')
    plt.scatter(time, caud15, label='0.15')
    plt.scatter(time, caud18, label='0.18')
    plt.scatter(time, caud22, label='0.22')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Caudal (1/s)')
    plt.legend()
    plt.show()

caudales()