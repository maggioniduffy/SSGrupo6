import matplotlib.pyplot as plt
import numpy as np

plt.style.use('default')

def draw(gens, y: list, p_cells, time):
    fig, ax = plt.subplots()
    plt.title('Juego de la vida 2D, ' + 'Celulas iniciales: ' + str(p_cells) + '\n Tiempo de ejecucion: \n' + str(time) + ' segundos\n Ultima cantidad de celdas: ' +str(y[-1]))
    plt.xlabel('Generaciones')
    plt.ylabel('Celulas vivas')
    print(y, gens)
    x_data, y_data = np.arange(0, gens),y

    step_x = 1
    max_y = np.amax(y)
    step_y = gens * 10

    ax.plot(x_data, y_data, linewidth=2.0)
    ax.set(xlim=(0, gens), xticks=np.arange(1, gens, step_x),
        ylim=(0, max_y + 10), yticks=np.arange(1, max_y+10, step_y))
    
    plt.show()