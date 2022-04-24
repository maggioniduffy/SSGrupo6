import pygame
from speedDistributions import *
from config_loader import *
import numpy as np
from time import sleep
from utils import set_pdf
#from Plot import *
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

def set_collisions_per_secs(time, collision_times, total_collisions):
    interval_size = ct_interval_size
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
    y = []
    i = 0
    b = bins[i]
    while b > 0:
        #used_bins.append(b/(len(bins))) #ELEGIR PDF o Distribucion comun
        #print(b/total_collisions)/interval_size
        y.append((b)/(total_collisions*interval_size))
        i+=1
        b = bins[i]
    #def set_pdf(y, var, file, operation='a'):
    set_pdf(y,var='N={n}'.format(n=N), file='./pdf.txt')

def getDist(particle):
    return particle[2]

def animate():
    clock = 0
    big_particle_x = []
    big_particle_y = []
    center_particles = []
    center_particles_open = True
    save = False
    #screen = pygame_set()
    collisions = read_output()
    y = 0
    collision_times = []
    prev_time = 0
    pos_center = np.sqrt((3.0)**2 + (3.0)**2)

    pos_g = open('./posGrande.txt', 'a')
    #pos_g.write("\nSimulacion")

    pos_ch = open('./dcmChicas.txt', 'w')

    for g in range(1, len(collisions)):
        if g == 2:
            center_particles.sort(key=getDist)
            center_particles = center_particles[:10]
        lines = collisions[g].split('\n')
        time = float(lines[0].split(' ')[1])
        collision_times.append(time-prev_time)
        prev_time = time

        if (float(time) >= float(clock)):
            clock = float(clock + 10)
            save = True
        else:
            save = False
        #screen.fill(bg)
        for line in range(1,len(lines)-1):
             index = lines[line].split(':')
             coordinates = index[1].split(',')
             x,y = float(coordinates[0]) * 100, float(coordinates[1]) * 100
             if (index[0] == '0'): #GRANDE
                 #if (float(time) >= float(clock)):
                  #  pos_g.write("\n" + str((pos_center - (np.sqrt((x/100)**2 + (y/100)**2)))**2))
                  #  clock = float(clock + 5)
                 #pygame.draw.circle(screen, (159, 0, 255), (x, y), BIG_RADIUS * 100)
                 if save_journey and N == 130 and time <= tc_big_sphere:
                    big_particle_x.append(x)
                    big_particle_y.append(y)
             else: #CHICAS
                 ind = int(index[0])
                 if g == 1:
                    dist = (pos_center - (np.sqrt((x/100)**2 + (y/100)**2)))**2
                    pos_initial = np.sqrt((x/100)**2 + (y/100)**2)
                    aux = [ind,pos_initial,dist]
                    #print(aux)
                    center_particles.append(aux)
                 elif save and center_particles_open:
                    indexes = np.array([row[0] for row in center_particles])
                    #print(indexes)
                    place = np.where(indexes == ind)[0]
                    #print(place[0])
                    if len(place) > 0:
                        place = place[0]
                        center = center_particles[place][1]
                        pos_ch.write("\n" + str((pos_center - (np.sqrt((x/100)**2 + (y/100)**2)))**2))
                        #clock = float(clock + 5)
                    if x == 3.0 or y == 3.0:
                        print('BORDE')
                        pos_ch.close()
                        center_particles_open = False
                #pygame.draw.circle(screen, (255,255,255), (x, y), SMALL_RADIUS * 100)
        #pygame.display.flip()
        if save:
            pos_ch.write('\ndt')
    if center_particles_open:
        pos_ch.close()
    pos_g.close()
    frec = len(collisions) / time
    title = 'frecuenciasv{v}n{n}.txt'.format(v=v,n=N)
    g = open(title, 'a')
    g.write("\n" + str(frec) + "+")
    g.close()
    sleep(2)
    if save_journey and N == 130: 
        save_big_sphere_journey(big_particle_x,big_particle_y)
    
    collision_time_media = time / (len(collisions)-1)
    set_collisions_per_secs(time,collision_times, len(collisions))
    #pdf(used_bins, interval_size)

animate()