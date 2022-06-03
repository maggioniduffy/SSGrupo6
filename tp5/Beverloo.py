import matplotlib.pyplot as plt
import numpy as np
import math

window = 40
volume = 1.0 * 0.3
nps = []
rads_prom = []
qs_prom = []
des = []
caudals = {0.10 : [], 0.12: [], 0.15: [], 0.18: []}
for diam in list(caudals.keys()):
    file = open('./caudal0' + str(int(diam*100)) + '.txt', 'r')
    data = file.read()
    file.close()
    first_line = data.split("\n")[0].split(" ")
    n = int(first_line[0])
    rad_prom = float(first_line[1])
    nparts = n / volume
    rads_prom.append(rad_prom)
    nps.append(nparts)
    # print(str(n015) + " " + str(rad_prom015))
    caudales = data.split(':')[1:]
    caudal = []
    i = 0
    for line in caudales[0].split('\n')[1:][:-1]:
        caudal.append(float(line))
    for i,time in enumerate(caudal):
        if i + window - 1 < len(caudal)-(window-1):
            caudals[diam].append(window/(caudal[i+window-1]-time))

    # print(len(caudal015))
    des.append(np.std(caudals[diam]))
    promedio = sum(caudals[diam])/len(caudals[diam])
    qs_prom.append(promedio)

beverloos = []
c_vals = np.linspace(2, 4, 100)
# print(c_vals)
def beverloo(npart, diam, rad_prom, c):
    return npart * math.sqrt(10) * math.pow((diam - c * rad_prom), 1.5)

def ecm(c, qs_prom, nps, diams, rads_prom):
    sum = 0
    for i,q in enumerate(qs_prom):
        bev = beverloo(nps[i], diams[i], rads_prom[i], c)
        sum += math.pow(q - bev, 2)
    return sum/(i+1)

result = []
for c in c_vals:
    result.append(ecm(c,qs_prom, nps, list(caudals.keys()), rads_prom))
# print(c_vals[result.index(min(result))])
# print(beverloos)
min_c = c_vals[result.index(min(result))]
print("c minimo: " + str(min_c))
print("error min: " + str(min(result)))
x_vals = np.linspace(0.1, 0.2, 100)
for x in x_vals:
    beverloos.append(beverloo(nps[0], x, rads_prom[0], min_c))
plt.plot(x_vals, beverloos, color='blue')
plt.errorbar(list(caudals.keys()), qs_prom, des, fmt='o')
# plt.plot(c_vals, result, color='red')
plt.show()
