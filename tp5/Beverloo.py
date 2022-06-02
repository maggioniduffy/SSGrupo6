import matplotlib.pyplot as plt
import numpy as np
import math

volume = 1.0 * 0.3
diams = [0.15, 0.18, 0.22, 0.25]
nps = []
rads_prom = []
qs_prom = []
for diam in diams:
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
    for line in caudales[0].split('\n')[1:][:-1]:
        caudal.append(float(line))
    # print(len(caudal015))
    promedio = sum(caudal)/len(caudal)
    qs_prom.append(promedio)

beverloos = []
c_vals = np.linspace(0, 5, 100)
# print(c_vals)
def beverloo(npart, diam, rad_prom, c):
    return npart * math.sqrt(10) * math.pow((diam - c * rad_prom), 1.5)

def ecm(c, qs_prom, nps, diams, rads_prom):
    sum = 0
    for i,q in enumerate(qs_prom):
        bev = beverloo(nps[i], diams[i], rads_prom[i], c)
        # if(c > 1.42 and c < 1.47):
        #     beverloos.append(bev)
        sum += math.pow(q - bev, 2)
    return sum/(i+1)

result = []
for c in c_vals:
    result.append(ecm(c,qs_prom, nps, diams, rads_prom))
# print(c_vals[result.index(min(result))])
# print(beverloos)
plt.plot(c_vals, result, color='red')
plt.show()
