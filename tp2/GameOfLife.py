from random import randint
import numpy as np
import sys
from math import floor

nxC, nyC = 50, 50
centerX = nxC/2
centerY = nyC/2

def gameOfLife(maxNeighs = 3, minNeighs = 2):
    f = open('./output.txt', 'w')
    if len(sys.argv) > 1:
        percentage = int(sys.argv[1])
    else:
        percentage = 0

    center = np.array((centerX,centerY))

    factorx = nxC/5 * 4 - nxC/5
    factory = nyC/5 * 4 - nyC/5

    p_cells = floor(percentage * factorx * factory / 100)

    gameState = np.zeros((nxC, nyC))

    for _ in range(0, p_cells):
        x = randint(floor(nxC/5), floor(nxC/5)*4)
        y = randint(floor(nyC/5), floor(nyC/5)*4)
        while gameState[x, y] == 1:
            x = randint(floor(nxC/5), floor(nxC/5)*4)
            y = randint(floor(nyC/5), floor(nyC/5)*4)
        gameState[x, y] = 1

    stop = False
     
    alive_cells = p_cells
    alive_cells_ev = [alive_cells]
    go = True

    distances = []
    maxDistance = 0

    while go:
        newGameState = np.copy(gameState)
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
                    if gameState[x, y] == 0 and n_neigh == maxNeighs:
                        newGameState[x, y] = 1
                        alive_cells += 1
                    
                    #Regla 2
                    elif gameState[x, y] == 1 and (n_neigh <= minNeighs or n_neigh > maxNeighs):
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

                if alive_cells == 0 or ((x == 0 or x == (nxC - 1)) or (y == 0 or y == (nyC - 1))) and newGameState[x, y] == 1:
                    go = False
            f.write(line + '\n')
        alive_cells_ev.append(alive_cells)
        distances.append(maxDistance)
        maxDistance = 0
        gameState = np.copy(newGameState)

    f.close()
    print(alive_cells_ev)
    print(distances)

def og_gameOfLife():
    gameOfLife(3,2)

def new_gameOfLife():
    gameOfLife(1,9)

if sys.argv[2] == '1':
    print('og')
    og_gameOfLife()
else:
    new_gameOfLife()