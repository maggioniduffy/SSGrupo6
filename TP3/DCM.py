from cProfile import label
import matplotlib.pyplot as plt
import numpy as np

def plot_z(zs, labels):
    plt.style.use('default')
    fig, ax = plt.subplots()
    plt.xlabel('Tiempo (s)')
    plt.ylabel('DCM')
    i = 0
    for z in zs:
        zmax = np.amax(z)
        x = np.arange(0,len(z)*10,step=10)
        print('z: ', z)
        print('x: ', x)
        # plot
        ax.plot(x, z, linewidth=2.0, label=labels[i])
        ax.legend()
        ax.set(xlim=(0, np.amax(x)+1), xticks=np.arange(0, np.amax(x)+1,10),
            ylim=(0, zmax+1), yticks=np.arange(0, zmax+1))
        i += 1
    plt.grid()
    plt.show()

def big_particle_dcm():
    f = open('./posGrande.txt', 'r')
    data = f.read()
    f.close()
    simulations = data.split('Simulacion')[1:]
    aux_pos = simulations[0].split('\n')[1:][:-1]
    n = len(aux_pos)
    print('ENE: ', n)
    z = np.zeros(n)
    for s in simulations:
        positions = s.split('\n')[1:][:-1]
        i = 0
        for pos in positions:
            pos = round(float(pos),1)
            print(pos)
            z[i] += pos
            i += 1
    print(z)
    z = z/n
    return z

#big_particle_dcm()
def small_particles_dcm():
    f = open('./dcmChicas.txt', 'r')
    data = f.read()
    f.close()
    simulations = data.split('\ndt')[1:][:-1]
    aux_pos = simulations[0].split('\n')[1:]
    n = len(simulations)
    z = np.zeros(n)
    i = 0
    for s in simulations:
        positions = s.split('\n')[1:]
        aux = 0
        for p in positions:
            aux += float(p)
        z[i] = aux/n
        i += 1
    z = np.append(0,z)
    return z

z1, z2 = big_particle_dcm(), small_particles_dcm()
plot_z([z1,z2], ['Grande', '10 Chicas'])
