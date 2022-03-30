import pygame
import numpy as np
import time

pygame.init()

width, height = 1000, 1000
screen = pygame.display.set_mode((height, width))

bg = 25, 25, 25
screen.fill(bg)

nxC, nyC = 50, 50

dimCW = width / nxC
dimCH = height / nyC

gameState = np.zeros((nxC, nyC))


#Defino los automatas, despues se puede hacer que se tomen de algun archivo o random
#Automata 1
gameState[5, 3] = 1
gameState[5, 4] = 1
gameState[5, 5] = 1
gameState[4, 5] = 1
gameState[4, 6] = 1

#Automata 2
gameState[22, 22] = 1
gameState[21, 23] = 1
gameState[20, 23] = 1
gameState[23, 23] = 1

while True:

    newGameState = np.copy(gameState)
    
    screen.fill(bg)
    time.sleep(0.1)
    
    for y in range(0, nxC):
        for x in range(0, nyC):

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
    
    gameState = np.copy(newGameState)

    pygame.display.flip()





