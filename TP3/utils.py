def set_pdf(y, var, file, operation='a'):
    f = open(file, operation)
    f.write('run\n')
    f.write(var+'\n')
    for yi in y:
        f.write(str(yi)+'\n')
    f.close()

def save_big_sphere_journey(x,y):
    f = open('./bigsphere.txt','a')
    f.write('run\n')
    f.write('v:{v}\n'.format(v=v))
    for i in range(0,len(x)):
        f.write('{x},{y}\n'.format(x=x[i],y=y[i]))
    f.close()