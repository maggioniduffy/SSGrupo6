import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)

import os
import sys

dynamic = sys.argv[1]
output = sys.argv[2]
element = sys.argv[3]

if not os.path.exists(dynamic):
    exit
    # file exists
if not os.path.exists(output):
    exit
    # file exists
if not element:
    exit
else:
    element = int(element)

# Fixing random state for reproducibility
# np.random.seed(19680801)
f = open(dynamic,'r')
g = open(output, 'r')

lines = f.readlines() # read all the lines of the text file and return them as a list of strings.
f.close()
lines.pop(0)

g_lines = g.readlines() # read all the lines of the text file and return them as a list of strings.
g.close()

x_arr = []
y_arr = []

colors = []
area = []

neighbors = []

for i in range(len(lines)):
    line = lines[i]
    numbers = line.strip().split(' ')

    x_arr.append(float(numbers[0]))
    y_arr.append(float(numbers[3]))

    if (i == element):
        colors.append('#FF0000')
        area.append(60)
        neighbors = (g_lines[i-1].strip().split(','))[1:]
        print(neighbors)
    else:
        colors.append('#000')
        area.append(35)

for neigh in neighbors:
    index = int(neigh)
    colors[index] = '#FFFA10'
    area[index] = 55

x = np.array(x_arr)
y = np.array(y_arr)
n = np.array(range(len(lines)))

N = len(x)

fig, ax = plt.subplots(figsize=(10, 8))
ax.scatter(x, y)

for i, txt in enumerate(n):
    ax.annotate(txt, (x[i], y[i]))

# Set axis ranges; by default this will put major ticks every 25.
ax.set_xlim(0, N)
ax.set_ylim(0, N)

# Change major ticks to show every 20.
ax.xaxis.set_major_locator(MultipleLocator(10))
ax.yaxis.set_major_locator(MultipleLocator(10))

# Change minor ticks to show every 5. (20/4 = 5)
ax.xaxis.set_minor_locator(AutoMinorLocator(1))
ax.yaxis.set_minor_locator(AutoMinorLocator(1))

# Turn grid on for both major and minor ticks and style minor slightly
# differently.
ax.grid(which='major', color='#CCCCCC', linestyle='--')
ax.grid(which='minor', color='#CCCCCC', linestyle=':')

#plt.grid()
plt.scatter(x, y, s=area, linewidths=1, c=colors, alpha=0.8)
plt.show()