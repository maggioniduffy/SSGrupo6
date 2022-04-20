import numpy as np
from config_loader import v

interval_size = 0.25
v_intervals = int(v/interval_size)

s = open('./speeds.txt', 'r')
speeds = s.read()
s.close()

def initialSpeedDistrib():
    v_bins_initial = np.zeros(v_intervals)
    s_colls = speeds.split('Collision')[1]
    lines = s_colls.split('\n')[3:][:-1]

    for pair in lines:
        speed = float(pair.split(':')[1])
        print(speed)
        stop = False
        n = 1
        while not stop:
            if speed <= interval_size * n:
                v_bins_initial[n-1] = v_bins_initial[n-1] + 1
                stop = True
            else:
                n += 1  
    return v_bins_initial

