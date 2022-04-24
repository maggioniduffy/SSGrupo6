import pygame
from config_loader import *

def pygame_set():
    pygame.init()
    width, height = SIDE_SIZE * 100, SIDE_SIZE * 100
    screen = pygame.display.set_mode((height, width))
    screen.fill(bg)

    return screen

def read_output():
    f = open('./output.txt', 'r')
    matrix = f.read()
    f.close()
    collisions = matrix.split('Collision\n')

    return collisions

def animate():
    screen = pygame_set()
    collisions = read_output()
    y = 0
    for g in range(1, len(collisions)):
        lines = collisions[g].split('\n')
        screen.fill(bg)
        for line in range(1,len(lines)-1):
             index = lines[line].split(':')
             coordinates = index[1].split(',')
             x,y = float(coordinates[0]) * 100, float(coordinates[1]) * 100
             if (index[0] == '0'): #GRANDE
                 pygame.draw.circle(screen, (159, 0, 255), (x, y), BIG_RADIUS * 100)
             else: #CHICAS
                pygame.draw.circle(screen, (255,255,255), (x, y), SMALL_RADIUS * 100)
        pygame.display.flip()

animate()