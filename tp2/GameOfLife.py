from random import randint
import pygame
import numpy as np
import time
import sys
from math import floor

if len(sys.argv) > 1:
    percentage = int(sys.argv[1])
else:
    percentage = 0

pygame.init()

width, height = 1000, 1000
screen = pygame.display.set_mode((height, width))

bg = 25, 25, 25
screen.fill(bg)

nxC, nyC = 50, 50

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


#Defino los automatas, despues se puede hacer que se tomen de algun archivo o random
#Automata 1
# gameState[5, 3] = 1
# gameState[5, 4] = 1
# gameState[5, 5] = 1

#Automata 2
# gameState[21, 21] = 1
# gameState[22, 22] = 1
# gameState[22, 23] = 1
# gameState[21, 23] = 1
# gameState[20, 23] = 1

stop = False

while True:

    newGameState = np.copy(gameState)
    
    screen.fill(bg)
    time.sleep(0.1)
    
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
                if gameState[x, y] == 0 and n_neigh == 3:
                    newGameState[x, y] = 1
                
                #Regla 2
                elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x, y] = 0

            poly = [((x) * dimCW, y * dimCH),
                    ((x+1) * dimCW, y * dimCH),
                    ((x+1) * dimCW, (y+1) * dimCH),
                    ((x) * dimCW, (y+1) * dimCH)]

            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)
            
            if ((x == 0 or x == (nxC - 1)) or (y == 0 or y == (nyC - 1))) and newGameState[x, y] == 1:
                
                stop = True
    
    gameState = np.copy(newGameState)

    pygame.display.flip()

#Defino los automatas, despues se puede hacer que se tomen de algun archivo o random
#Automata 1
# gameState[5, 3] = 1
# gameState[5, 4] = 1
# gameState[5, 5] = 1

#Automata 2
# gameState[21, 21] = 1
# gameState[22, 22] = 1
# gameState[22, 23] = 1
# gameState[21, 23] = 1
# gameState[20, 23] = 1
