from random import randint
import numpy as np
import sys
import time
from math import floor
from constants import centerX, centerY, centerZ, nxC, nyC, nzC
# from graphic import draw

def gameOfLife(maxNeighs = 3, minNeighs = 2):
    t_inicial = time.time()
    if len(sys.argv) > 1:
        percentage = int(sys.argv[1])
    else:
        percentage = 0

    if len(sys.argv) > 3:
        gen_limit = sys.argv[3]
    else:
        gen_limit = 200

    center = np.array((centerX,centerY,centerZ))

    factorx = nxC/3 * 2 - nxC/3
    factory = nyC/3 * 2 - nyC/3
    factorz = nzC/3 * 2 - nzC/3

    p_cells = floor(percentage * factorx * factory * factorz / 100)

    gameState = np.zeros((nxC, nyC, nzC))

    maxDistance = 0
    for _ in range(0, p_cells):
        x = randint(floor(nxC/3), floor(nxC/3)*2)
        y = randint(floor(nyC/3), floor(nyC/3)*2)
        z = randint(floor(nzC/3), floor(nzC/3)*2)
        while gameState[x, y, z] == 1:
            x = randint(floor(nxC/3), floor(nxC/3)*2)
            y = randint(floor(nyC/3), floor(nyC/3)*2)
            z = randint(floor(nzC/3), floor(nzC/3)*2)
        gameState[x, y, z] = 1
        point = np.array((x,y,z))
        dist = np.linalg.norm(center-point)
        if dist > maxDistance:
            maxDistance = dist

    distances = [maxDistance]
    maxDistance = 0
    stop = False
     
    alive_cells = p_cells
    alive_cells_ev = [alive_cells]
    go = True

    f = open('./output.txt', 'w')
    gens = 1
    while go:
        newGameState = np.copy(gameState)
        f.write('new gen\n')
        gens += 1
        for x in range(0, nxC):
            for y in range(0, nyC):
                for z in range(0, nzC):
                    line = ""
                    if not stop:
                        n_neigh = gameState[x-1, y-1, z-1] if (x-1) > 0 and (y-1) > 0 and (z-1) > 0 else 0
                        n_neigh += gameState[x-1, y-1, z] if (x-1) > 0 and (y-1) > 0 else 0
                        n_neigh += gameState[x-1, y-1, z + 1] if (x-1) > 0 and (y-1) > 0 and (z+1) < nzC else 0
                        n_neigh += gameState[x, y-1, z-1] if (y-1) > 0 and (z-1) > 0 else 0
                        n_neigh += gameState[x, y-1, z] if (y-1) > 0 else 0
                        n_neigh += gameState[x, y-1, z+1] if (y-1) > 0 and (z+1) < nzC else 0
                        n_neigh += gameState[x+1, y-1, z-1] if (x+1) < nxC and (y-1) > 0 and (z-1) > 0 else 0
                        n_neigh += gameState[x+1, y-1, z] if (x+1) < nxC and (y-1) > 0 else 0
                        n_neigh += gameState[x+1, y-1, z+1] if (x+1) < nxC and (y-1) > 0 and (z+1) < nzC else 0
                        n_neigh += gameState[x-1, y, z-1] if (x-1) > 0 and (z-1) > 0 else 0
                        n_neigh += gameState[x-1, y, z] if (x-1) > 0 else 0
                        n_neigh += gameState[x-1, y, z+1] if (x-1) > 0 and (z+1) < nzC else 0
                        n_neigh += gameState[x+1, y, z-1] if (x+1) < nxC and (z-1) > 0 else 0
                        n_neigh += gameState[x+1, y, z] if (x+1) < nxC else 0
                        n_neigh += gameState[x+1, y, z+1] if (x+1) < nxC and (z+1) < nzC else 0
                        n_neigh += gameState[x-1, y+1, z-1] if (x-1) > 0 and (y+1) < nyC and (z-1) > 0 else 0
                        n_neigh += gameState[x-1, y+1, z] if (x-1) > 0 and (y+1) < nyC else 0
                        n_neigh += gameState[x-1, y+1, z+1] if (x-1) > 0 and (y+1) < nyC and (z+1) < nzC else 0
                        n_neigh += gameState[x, y+1, z-1] if (y+1) < nyC and (z-1) > 0 else 0
                        n_neigh += gameState[x, y+1, z] if (y+1) < nyC else 0
                        n_neigh += gameState[x, y+1, z+1] if (y+1) < nyC and (z+1) < nzC else 0
                        n_neigh += gameState[x+1, y+1, z-1] if (x+1) < nxC and (y+1) < nyC and (z-1) > 0 else 0
                        n_neigh += gameState[x+1, y+1, z] if (x+1) < nxC and (y+1) < nyC else 0
                        n_neigh += gameState[x+1, y+1, z+1] if (x+1) < nxC and (y+1) < nyC and (z+1) < nzC else 0
                        n_neigh += gameState[x, y, z+1] if (z+1) < nzC else 0
                        n_neigh += gameState[x, y, z-1] if (z-1) > 0 else 0

                        #Regla 1
                        if gameState[x,y,z] == 0 and n_neigh == maxNeighs:
                            newGameState[x,y,z] = 1
                            alive_cells += 1
                        
                        #Regla 2
                        elif gameState[x,y,z] == 1 and (n_neigh < minNeighs or n_neigh > maxNeighs):
                            newGameState[x,y,z] = 0
                            alive_cells -= 1

                    if newGameState[x,y,z] == 0:
                        line = "{x},{y},{z},0".format(x = x,y = y,z = z)
                    else:
                        point = np.array((x,y,z))
                        dist = np.linalg.norm(center-point)
                        if dist > maxDistance:
                            maxDistance = dist
                        line = "{x},{y},{z},1".format(x = x,y = y,z = z)
            
                    if gens == gen_limit or alive_cells == 0 or ((x == 0 or x == (nxC - 1)) or (y == 0 or y == (nyC - 1)) or (z == 0 or z == (nzC - 1))) and newGameState[x,y,z] == 1:
                        go = False
                    f.write(line + '\n')
        maxDistance = 0
        gameState = np.copy(newGameState)
        alive_cells_ev.append(alive_cells)
        distances.append(maxDistance)

    t_final = time.time() - t_inicial
    f.close()
    g = open('./results.txt', 'w')
    g.write('Cantidad de celulas iniciales: ' + str(p_cells) + '\n')
    g.write('Celulas vivas en generacion: \n')
    for i in range(0, len(alive_cells_ev)):
        g.write(str(i) + ": " + str(alive_cells_ev[i]) + '\n')

    g.write('Rango maximo en generacion: \n')
    for i in range(0, len(distances)):
        g.write(str(i) + ": " + str(distances[i]) + '\n')
    
    g.write('Tiempo transcurrido en segundos: ' + str(t_final / 1000))
    g.close()
    # draw(gens, alive_cells_ev, p_cells, t_final)

def og_gameOfLife():
    gameOfLife(3,2)

def new_gameOfLife():
    gameOfLife(6,5)

if sys.argv[2] == '1':
    print('og')
    og_gameOfLife()
else:
    new_gameOfLife()