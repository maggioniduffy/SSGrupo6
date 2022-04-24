def set_pdf(y, var, file, operation='a'):
    f = open(file, operation)
    f.write('run\n')
    f.write(var+'\n')
    for yi in y:
        f.write(str(yi)+'\n')
    f.close()