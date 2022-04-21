import pygame
from speedDistributions import *
from config_loader import *
import numpy as np
from time import sleep
from Plot import *
from bigSphereTravel import save_big_sphere_journey

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

def set_collisions_per_secs(time, collision_times):
    interval_size = 0.0015
    intervals = int(np.ceil(time / interval_size))
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
    used_bins = []
    i = 0
    b = bins[i]
    while b > 0:
        used_bins.append(b/(len(bins))) #ELEGIR PDF o Distribucion comun
        i+=1
        b = bins[i]
        
    return used_bins

def animate():
    big_particle_x = []
    big_particle_y = []
    screen = pygame_set()
    collisions = read_output()

    y = 0
    collision_times = []
    prev_time = 0
    for g in range(1, len(collisions)):
        lines = collisions[g].split('\n')
        time = float(lines[0].split(' ')[1])
        collision_times.append(time-prev_time)
        prev_time = time
        screen.fill(bg)
        for line in range(1,len(lines)-1):
             index = lines[line].split(':')
             coordinates = index[1].split(',')
             x,y = float(coordinates[0]) * 100, float(coordinates[1]) * 100
             if (index[0] == '0'): #GRANDE
                 pygame.draw.circle(screen, (255,0,0), (x, y), BIG_RADIUS * 100)
                 if save_journey and N == 130 and time <= tc_big_sphere:
                    big_particle_x.append(x)
                    big_particle_y.append(y)
             else: #CHICAS
                pygame.draw.circle(screen, (255,255,255), (x, y), SMALL_RADIUS * 100)
        pygame.display.flip()

    frec = len(collisions) / time
    title = 'frecuenciasv{v}n{n}.txt'.format(v=v,n=N)
    g = open(title, 'a')
    g.write("\n" + str(frec) + "+")
    g.close()
    sleep(2)
    if save_journey and N == 130: 
        save_big_sphere_journey(big_particle_x,big_particle_y)
    
    collision_time_media = time / (len(collisions)-1)
    used_bins = set_collisions_per_secs(time,collision_times)
    graphic(used_bins, interval_size)

animate()