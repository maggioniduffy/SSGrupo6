import matplotlib.pyplot as plt
import numpy as np
import math

volume = 1.0 * 0.3

file = open('./caudal015.txt', 'r')
data = file.read()
file.close()
first_line = data.split("\n")[0].split(" ")
nps = []
rads_prom = []
qs_prom = []
diams = [0.15, 0.18, 0.22, 0.25]
n015 = int(first_line[0])
rad_prom015 = float(first_line[1])
np015 = n015 / volume
rads_prom.append(rad_prom015)
nps.append(np015)
# print(str(n015) + " " + str(rad_prom015))
caudales = data.split(':')[1:]
caudal015 = []
for line in caudales[0].split('\n')[1:][:-1]:
    caudal015.append(float(line))
# print(len(caudal015))
promedio_015 = sum(caudal015)/len(caudal015)
qs_prom.append(promedio_015)
# print("promedio 0.15: ")
# print(promedio_015)

file = open('./caudal018.txt', 'r')
data = file.read()
file.close()
caudales = data.split(':')[1:]
caudal018 = []
i = 0
first_line = data.split("\n")[0].split(" ")
n018 = int(first_line[0])
rad_prom018 = float(first_line[1])
np018 = n018 / volume
rads_prom.append(rad_prom018)
nps.append(np018)
for line in caudales[0].split('\n')[1:][:-1]:
    caudal018.append(float(line))
promedio_018 = sum(caudal018)/len(caudal018)
qs_prom.append(promedio_018)
# print("promedio 0.18: ")
# print(promedio_018)

file = open('./caudal022.txt', 'r')
data = file.read()
file.close()
caudales = data.split(':')[1:]
caudal022 = []
i = 0
first_line = data.split("\n")[0].split(" ")
n022 = int(first_line[0])
rad_prom022 = float(first_line[1])
np022 = n022 / volume
rads_prom.append(rad_prom022)
nps.append(np022)
for line in caudales[0].split('\n')[1:][:-1]:
    caudal022.append(float(line))

promedio_022 = sum(caudal022)/len(caudal022)
qs_prom.append(promedio_022)
# print("promedio 0.22: ")
# print(promedio_022)

file = open('./caudal025.txt', 'r')
data = file.read()
file.close()
caudales = data.split(':')[1:]
caudal025 = []
i = 0
first_line = data.split("\n")[0].split(" ")
n025 = int(first_line[0])
rad_prom025 = float(first_line[1])
np025 = n025 / volume
rads_prom.append(rad_prom025)
nps.append(np025)
for line in caudales[0].split('\n')[1:][:-1]:
    caudal025.append(float(line))
promedio_025 = sum(caudal025)/len(caudal025)
qs_prom.append(promedio_025)
# print(diams)
# print(rads_prom)
# print(nps)
# print(qs_prom)
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
