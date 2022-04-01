import pygame
import time
from GameOfLife import nxC, nyC, centerX, centerY

nxC, nyC = 50, 50
centerX = nxC/2
centerY = nyC/2

def animate():
    pygame.init()
    print('init')
    r = 255
    g = 255
    b = 255
    width, height = 500, 500
    screen = pygame.display.set_mode((height, width))

    bg = 25, 25, 25
    screen.fill(bg)

    dimCW = width / nxC
    dimCH = height / nyC
    f = open('./output.txt', 'r')
    matrix = f.read()
    gens = matrix.split('new gen\n')
    f.close()
    y = 0
    for g in range(1, len(gens)):
        print('G: ', g)
        lines = gens[g].split('\n')
        time.sleep(0.5)
        y = 0
        for line in lines:
            y += 1
            print(y)
            x = -1
            for c in line:
                x += 1
                poly = [((x) * dimCW, y * dimCH), ((x+1) * dimCW, y * dimCH), ((x+1) * dimCW, (y+1) * dimCH), ((x) * dimCW, (y+1) * dimCH)]
                if c == '0':
                    print('CERO')
                    pygame.draw.polygon(screen, (5, 5, 5), poly, 0)
                elif c == '1':
                    difX = abs(x-centerX)
                    difY = abs(y-centerY)
                    dif = difX if difX > difY else difY
                    dif = dif * 7 if dif >= 0 else 0
                    pygame.draw.polygon(screen, (r, 0, 0 + dif), poly, 0)
        pygame.display.flip()
    while True:
        pass

animate()