f = open('./bigsphere.txt','r')
travel = f.read()
f.close()
runs = travel.split('run\n')
for r in runs:
    positions = r.split('\n')[1:]
    print(positions)