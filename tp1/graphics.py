import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
# np.random.seed(19680801)
f = open('Dynamic100.txt','r')

lines = f.readlines() # read all the lines of the text file and return them as a list of strings.
f.close()
lines.pop(0)
x_arr = []
y_arr = []

for line in lines:
    print(line)
    numbers = line.strip().split(' ')
    print(numbers)
    x_arr.append(float(numbers[0]))
    y_arr.append(float(numbers[3]))

x = np.array(x_arr)
y = np.array(y_arr)

g = open('AlgunosVecinos_100_rc6.txt', 'r')
g_lines = g.readlines() # read all the lines of the text file and return them as a list of strings.
g.close()

neighbors = []

for line in g_lines:
    numbers = line.strip().split(',')
    neighbors.append(numbers)

N = len(x)
colors = []
area = []
for i in range(N):
    if (i == 91):
        colors.append('#FF0000')
        area.append(60)
    else:
        colors.append('#000')
        area.append(35)

plt.grid()
plt.scatter(x, y, s=area, linewidths=1, c=colors, alpha=0.8)
plt.show()