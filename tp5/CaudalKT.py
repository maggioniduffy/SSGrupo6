import matplotlib.pyplot as plt
import numpy as np

def caudales():
    window = 100
    diams = [0.25, 0.40, 0.50, 0.60]
    caudales_promedio = []
    errores = []

    for diam in diams:
        # Leer datos del archivo
        file = open(f'./caudal0{(int)(diam*100)}.txt', 'r')
        data = file.read()
        file.close()
        caudales = data.split(':')[1:]
        tiempos_salida = []
        for line in caudales[0].split('\n')[1:][:-1]:
            tiempos_salida.append(float(line))

        # Calcular caudal usando una ventana de partículas
        caudal = []
        for i,time in enumerate(tiempos_salida):
            if i + window - 1 < len(tiempos_salida)-(window-1):
                caudal.append(window/(tiempos_salida[i+window-1]-time))

        # Calcular promedio y error
        promedio = np.average(caudal)
        error = np.std(caudal)
        caudales_promedio.append(promedio)
        errores.append(error)

    # Graficar resultados
    plt.errorbar(diams, caudales_promedio, yerr=errores, fmt='o')
    plt.xlabel('Constante kT (kN)')
    plt.ylabel('Caudal (1/s)')
    plt.show()

caudales()
