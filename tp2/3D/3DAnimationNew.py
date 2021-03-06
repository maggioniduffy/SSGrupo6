import time

from matplotlib import pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation
from constants import centerX, centerY, centerZ

f = open('./output.txt')
data = f.read()
f.close()
gens = data.split('new gen\n')
gens.remove('')
gens_len = len(gens)
iteration = 0

fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(projection='3d')
gens_positions = []
for i in range(0, gens_len):
    lines = gens[i].split('\n')
    gens_positions.append({'x': [], 'y': [], 'z': []})
    for line in lines:
        cell = line.split(',')
        if cell[0] != '':
            x, y, z, state = float(cell[0]), float(cell[1]), float(cell[2]), float(cell[3])
            if state == 1:
                gens_positions[i]['x'].append(x)
                gens_positions[i]['y'].append(y)
                gens_positions[i]['z'].append(z)


x=np.array(gens_positions[0]['x'])
y=np.array(gens_positions[0]['y'])
z=np.array(gens_positions[0]['z'])
# print(x)
dif = np.zeros(len(x))
difX = np.zeros(len(x))
difY = np.zeros(len(x))
difZ = np.zeros(len(x))
# print(np.arange(100))

for i in range(0, len(x)):
    dif = np.zeros(len(x))
    for i in range(0, len(x)):
        dif[i] = np.linalg.norm(np.array((x[i], y[i], z[i])) - np.array((centerX, centerY, centerZ))) * 3

points = ax.scatter(x, y, z, c=dif, s=150, marker='o', cmap='Reds')
txt = fig.suptitle('')

eps = 1e-16
ax.axes.set_xlim3d(left=0.-eps, right=30+eps)
ax.axes.set_ylim3d(bottom=0.-eps, top=30+eps)
ax.axes.set_zlim3d(bottom=0.-eps, top=30+eps)

def update_points(txt, points, gens_positions):

    # calculate the new sets of coordinates here. The resulting arrays should have the same shape
    # as the original x,y,z
    global iteration
    global ax
    ax.clear()
    eps = 1e-16
    ax.axes.set_xlim3d(left=0. - eps, right=30 + eps)
    ax.axes.set_ylim3d(bottom=0. - eps, top=30 + eps)
    ax.axes.set_zlim3d(bottom=0. - eps, top=30 + eps)
    new_x = gens_positions[iteration]['x']
    new_y = gens_positions[iteration]['y']
    new_z = gens_positions[iteration]['z']
    dif = np.zeros(len(new_x))
    for i in range(0, len(new_x)):
        dif[i] = abs(np.linalg.norm(np.array((new_x[i], new_y[i], new_z[i])) - np.array((centerX, centerY, centerZ)))) * 3
    print(dif)
    # print(iteration)
    points = ax.scatter(new_x, new_y, new_z, c=dif, s=150, vmin=20, vmax=50, marker='o', cmap='Reds_r')

    iteration += 1
    plt.pause(0.5)
    # return modified artists
    return points

ani=animation.FuncAnimation(fig, update_points, frames=gens_len-1, fargs=(points, gens_positions))


plt.show()