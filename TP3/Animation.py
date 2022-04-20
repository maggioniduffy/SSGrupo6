import pygame
from config_loader import v,n as N
import numpy as np
from time import sleep
from Plot import *

SIDE_SIZE = 6;
SMALL_RADIUS = 0.2;
BIG_RADIUS = 0.7;

def animate():
    big_particle_x = []
    big_particle_y = []
    pygame.init()
    width, height = SIDE_SIZE * 100, SIDE_SIZE * 100
    screen = pygame.display.set_mode((height, width))

    bg = 25, 25, 25

    screen.fill(bg)

    f = open('./output.txt', 'r')
    matrix = f.read()
    f.close()
    collisions = matrix.split('Collision\n')
    side = SIDE_SIZE * 100
    y = 0
    collision_times = []
    prev_time = 0
    for g in range(1, len(collisions)):
        lines = collisions[g].split('\n')
        time = lines[0]
        #print(time)
        time = float(time.split(' ')[1])
        collision_times.append(time-prev_time)
        prev_time = time
        screen.fill(bg)
        for line in range(1,len(lines)-1):
             index = lines[line].split(':')
             coordinates = index[1].split(',')
             x,y = float(coordinates[0]) * 100, float(coordinates[1]) * 100
             if (index[0] == '0'): #GRANDE
                 pygame.draw.circle(screen, (255,0,0), (x, y), BIG_RADIUS * 100)
                 big_particle_x.append(x)
                 big_particle_y.append(y)
             else: #CHICAS
                pygame.draw.circle(screen, (255,255,255), (x, y), SMALL_RADIUS * 100)
        pygame.display.flip()
    frec = len(collisions) / time
    collision_time_media = time / (len(collisions)-1)
    print("Media: ", collision_time_media)
    interval_size = 0.0015
    intervals = int(np.ceil(time / interval_size))
    print("Intervals: ", intervals)
    bins = np.zeros(intervals)

    for ct in collision_times:
        stop = False
        n = 1
        while not stop:
            if ct <= interval_size * n:
                bins[n-1] = bins[n-1] + 1
                stop = True
            else:
                n += 1  
    title = 'frecuenciasv{v}n{n}.txt'.format(v=v,n=N)
    g = open(title, 'a')
    g.write("\n" + str(frec) + "+")
    g.close()
    sleep(2)
    big_sphere_journey(big_particle_x,big_particle_y,side)
    used_bins = []
    i = 0
    b = bins[i]
    while b > 0:
        #print(interval_size*len(bins))
        used_bins.append(b/(len(bins))) #ELEGIR   
        print(b/(interval_size))
        i+=1
        b = bins[i]
    collision_times_distribution(used_bins, interval_size)

animate()