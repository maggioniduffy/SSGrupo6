import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
# np.random.seed(19680801)
f = open('Dynamic100.txt','r')
g = open('AlgunosVecinos_100_rc6.txt', 'r')

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

    if (i == 91):
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

N = len(x)

plt.grid()
plt.scatter(x, y, s=area, linewidths=1, c=colors, alpha=0.8)
plt.show()