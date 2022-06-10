from random import randint
import time
import numpy as np
import sys
from math import floor
from constants import nxC, nyC, centerX, centerY
from graphic import draw;

def gameOfLife(a = 2, b = 3, c =3):
    t_inicial = time.time()
    f = open('./output.txt', 'w')
    if len(sys.argv) > 1:
        percentage = int(sys.argv[1])
    else:
        percentage = 0

    if len(sys.argv) > 3:
        gen_limit = sys.argv[3]
    else:
        gen_limit = 200
        
    center = np.array((centerX,centerY))

    factorx = nxC/5 * 4 - nxC/5
    factory = nyC/5 * 4 - nyC/5

    p_cells = floor(percentage * factorx * factory / 100)

    gameState = np.zeros((nxC, nyC))

    maxDistance = 0
    for _ in range(0, p_cells):
        x = randint(floor(nxC/5), floor(nxC/5)*4)
        y = randint(floor(nyC/5), floor(nyC/5)*4)
        while gameState[x, y] == 1:
            x = randint(floor(nxC/5), floor(nxC/5)*4)
            y = randint(floor(nyC/5), floor(nyC/5)*4)
        gameState[x, y] = 1
        point = np.array((x,y))
        dist = np.linalg.norm(center-point)
        if dist > maxDistance:
            maxDistance = dist

    distances = []
    distances.append(maxDistance)
    stop = False

    alive_cells = p_cells
    alive_cells_ev = [alive_cells]
    go = True

    gens = 1
    while go:
        maxDistance = 0
        newGameState = np.copy(gameState)
        gens += 1
        f.write('new gen\n')
        for x in range(0, nxC):
            line = ""
            for y in range(0, nyC):
                if not stop:
                    n_neigh = gameState[(x-1), (y-1)] if (x-1) > 0 and (y-1) > 0 else 0
                    n_neigh += gameState[(x), (y-1)] if (y-1) > 0 else 0
                    n_neigh += gameState[(x+1), (y-1)] if (x+1) < nxC and (y-1) > 0 else 0
                    n_neigh += gameState[(x-1), (y)] if (x-1) > 0 else 0
                    n_neigh += gameState[(x+1), (y)] if (x+1) < nxC else 0
                    n_neigh += gameState[(x-1), (y+1)] if (x-1) > 0 and (y+1) < nyC else 0
                    n_neigh += gameState[(x), (y+1)] if (y+1) < nyC else 0
                    n_neigh += gameState[(x+1), (y+1)] if (x+1) < nxC and (y+1) < nyC else 0

                    #Regla 1
                    if gameState[x, y] == 0 and n_neigh == c:
                        newGameState[x, y] = 1
                        alive_cells += 1
                    
                    #Regla 2
                    elif gameState[x, y] == 1 and (n_neigh < a or n_neigh > b):
                        newGameState[x, y] = 0
                        alive_cells -= 1

                if newGameState[x, y] == 0:
                    line = line + '0'
                else:
                    point = np.array((x,y))
                    dist = np.linalg.norm(center-point)
                    if dist > maxDistance:
                        maxDistance = dist
                    line = line + '1'

                if gens == gen_limit or alive_cells == 0 or (((x == 0 or x == (nxC - 1)) or (y == 0 or y == (nyC - 1))) and newGameState[x, y] == 1):
                    go = False
                    stop = True
            f.write(line + '\n')
        gameState = np.copy(newGameState)
        alive_cells_ev.append(alive_cells)
        distances.append(maxDistance)
        
    t_final = time.time() - t_inicial
    f.close()
    g = open('./results2dnewb1005.txt', 'w')
    g.write('Celdas vivas por generacion: \n')
    for i in range(0, len(alive_cells_ev)):
        g.write(str(i) + ": " + str(alive_cells_ev[i]) + '\n')

    g.write('Distancia maxima al centro por generacion: \n')
    for i in range(0, len(distances)):
        g.write(str(i) + ": " + str(distances[i]) + '\n')

    g.write('Tiempo transcurrido en segundos: ' + str(t_final / 1000))
    g.close()
    #draw(gens, alive_cells_ev, p_cells, t_final)

def og_gameOfLife():
    gameOfLife(2,3,3)

def new_gameOfLife():
    gameOfLife(2,7,2)

if sys.argv[2] == '1':
    print('og')
    og_gameOfLife()
else:
    new_gameOfLife()