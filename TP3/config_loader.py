import json

f = open('config.json')
config = json.load(f)
v = config['max_speed']
n = config['quantity']
tc_big_sphere = config['max_time_big_sphere_graphic']
save_journey = config['save_journey']
SIDE_SIZE = 6;
SMALL_RADIUS = 0.2;
BIG_RADIUS = 0.7;
side = SIDE_SIZE * 100
bg = 25, 25, 25