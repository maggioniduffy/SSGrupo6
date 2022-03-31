from random import randint
import pygame
import numpy as np
import time
import sys
from math import floor

def gameOfLife(maxNeighs = 3, minNeighs = 2):
    if len(sys.argv) > 1:
        percentage = int(sys.argv[1])
    else:
        percentage = 0

    pygame.init()
    r = 255
    g = 255
    b = 255
    width, height = 1000, 1000
    screen = pygame.display.set_mode((height, width))

    bg = 25, 25, 25
    screen.fill(bg)

    nxC, nyC = 50, 50
    centerX = nxC/2
    centerY = nyC/2
    center = np.array((centerX,centerY))

    factorx = nxC/5 * 4 - nxC/5
    factory = nyC/5 * 4 - nyC/5

    p_cells = floor(percentage * factorx * factory / 100)

    dimCW = width / nxC
    dimCH = height / nyC

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
        
        screen.fill(bg)
        time.sleep(0.7)
        
        for y in range(0, nxC):
            for x in range(0, nyC):
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

                poly = [((x) * dimCW, y * dimCH),
                        ((x+1) * dimCW, y * dimCH),
                        ((x+1) * dimCW, (y+1) * dimCH),
                        ((x) * dimCW, (y+1) * dimCH)]

                if newGameState[x, y] == 0:
                    pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
                else:
                    point = np.array((x,y))
                    dist = np.linalg.norm(center-point)
                    if dist > maxDistance:
                        maxDistance = dist
                    difX = abs(x-centerX)
                    difY = abs(y-centerY)
                    dif = difX if difX > difY else difY
                    dif = dif * 5 if dif >= 0 else 0
                    pygame.draw.polygon(screen, (r, g-dif, b), poly, 0)

                if alive_cells == 0 or ((x == 0 or x == (nxC - 1)) or (y == 0 or y == (nyC - 1))) and newGameState[x, y] == 1:
                    go = False
        
        alive_cells_ev.append(alive_cells)
        distances.append(maxDistance)
        maxDistance = 0
        gameState = np.copy(newGameState)

        pygame.display.flip()
    
    print(alive_cells_ev)
    print(distances)
    while True:
        pass

def og_gameOfLife():
    gameOfLife(3,2)

def new_gameOfLife():
    gameOfLife(1,9)

if sys.argv[2] == '1':
    print('og')
    og_gameOfLife()
else:
    new_gameOfLife()