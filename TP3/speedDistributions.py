import numpy as np
from config_loader import v,n as N
from Plot import *

interval_size = 0.25
v_intervals_initial = int(v/interval_size)
v_intervals = int(4/interval_size)

s = open('./speeds.txt', 'r')
speeds = s.read()
s.close()

def place_in_bins(value, bins):
    stop = False
    aux = bins.copy()
    n = 1
    while not stop:
        if value <= interval_size * n:
            aux[n-1] = aux[n-1] + 1
            stop = True
        else:
            n += 1 
    return aux

def initialSpeedDistrib():
    v_bins_initial = np.zeros(v_intervals_initial)
    s_colls = speeds.split('Collision')[1]
    lines = s_colls.split('\n')[3:][:-1]

    for pair in lines:
        speed = float(pair.split(':')[1])
        print(speed)
        v_bins_initial = place_in_bins(speed,v_bins_initial)
    return v_bins_initial

init_bins = initialSpeedDistrib()

def lastThirdSpeedDistrib():
    v_bins_last_third = np.zeros(v_intervals)
    s_colls = speeds.split('Collision')
    #particles = np.zeros(N)
    last_third = int(np.ceil(len(s_colls) * 2/3))
    s_colls = s_colls[last_third:]
    for s in s_colls:
        lines = s.split('\n')[2:][:-1]
        #'77:0.931039'
        for pair in lines:
            data = pair.split(':')
            speed = float(data[1])
            v_bins_last_third = place_in_bins(speed, v_bins_last_third)
        #print(lines)
    last_third_collisions = len(s_colls) * N
    return v_bins_last_third, last_third_collisions

last_third, size = lastThirdSpeedDistrib()
print(init_bins)
init_bins = init_bins/N
last_third = last_third/size
graphic(last_third, interval_size, xlabel='Velocidad particulas chicas (m/s)')