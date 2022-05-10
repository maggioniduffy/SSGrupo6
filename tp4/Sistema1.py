import matplotlib.pyplot as plt
import numpy as np

def pos():
    dt = 0.001

    time = np.arange(0, 5, dt)

    file = open('./output.txt', 'r')
    data = file.read()
    file.close()
    solutions = data.split(':')[1:]
    analytical = []
    for line in solutions[0].split('\n')[1:][:-1]:
            analytical.append(float(line))
    verlet = []
    for line in solutions[1].split('\n')[1:][:-1]:
        verlet.append(float(line))
    beeman = []
    for line in solutions[2].split('\n')[1:][:-1]:
        beeman.append(float(line))
    gear5 = []
    for line in solutions[3].split('\n')[1:][:-1]:
        gear5.append(float(line))

    auxTime = []
    for i in range(0, len(analytical)):
        auxTime.append(time[i])

    plt.plot(time, analytical, label='Analitica')
    plt.plot(time, verlet, label='Verlet')
    plt.plot(time, beeman, label='Beeman')
    plt.plot(time, gear5, label='Gear Predictor-Corrector')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Posicion (m)')
    plt.legend()
    plt.show()

def ecm():
    dts = [0.1, 0.01, 0.001, 0.0001, 0.00001]
    vecm = []
    becm = []
    gecm = []

    file = open('./ecm.txt', 'r')
    data = file.read()
    file.close()
    ecms = data.split(':')[1:]
    for i in range(0, len(dts)):
        aux = ecms[i].split('\n')[1:][:-1]
        vecm.append(float(aux[0]))
        becm.append(float(aux[1]))
        gecm.append(float(aux[2]))

    plt.loglog(dts, vecm, marker='o', label='Verlet')
    plt.loglog(dts, becm, marker='o', label='Beeman')
    plt.loglog(dts, gecm, marker='o', label='Gear Predictor-Corrector')
    plt.xlabel('dt (s)')
    plt.ylabel('ECM (m^2)')
    plt.legend()
    plt.show()

#pos()
ecm()