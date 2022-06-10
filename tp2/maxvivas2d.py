import matplotlib.pyplot as plt
import numpy as np

def max_alive():
    max_alive_cells30 = []
    ev_cells30 = []
    file = open('./results2d301.txt', 'r')
    data = file.read()
    file.close()
    max301 = data.split('generacion')[1:]
    max301 = max301[0].split('\n')[1:]
    max301.pop(0)
    max301.pop()
    max_aux = 0
    for line in max301:
        n = line.split(": ")[1:]
        ev_cells30.append(float(n[0]))
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells30.append(max_aux)

    file = open('./results2d302.txt', 'r')
    data = file.read()
    file.close()
    max302 = data.split('generacion')[1:]
    max302 = max302[0].split('\n')[1:]
    max302.pop(0)
    max302.pop()
    max_aux = 0
    for line in max302:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells30.append(max_aux)

    file = open('./results2d303.txt', 'r')
    data = file.read()
    file.close()
    max303 = data.split('generacion')[1:]
    max303 = max303[0].split('\n')[1:]
    max303.pop(0)
    max303.pop()
    max_aux = 0
    for line in max303:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells30.append(max_aux)

    file = open('./results2d304.txt', 'r')
    data = file.read()
    file.close()
    max304 = data.split('generacion')[1:]
    max304 = max304[0].split('\n')[1:]
    max304.pop(0)
    max304.pop()
    max_aux = 0
    for line in max304:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells30.append(max_aux)

    file = open('./results2d305.txt', 'r')
    data = file.read()
    file.close()
    max305 = data.split('generacion')[1:]
    max305 = max305[0].split('\n')[1:]
    max305.pop(0)
    max305.pop()
    max_aux = 0
    for line in max305:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells30.append(max_aux)

    max_alive_cells50 = []
    ev_cells50 = []
    file = open('./results2d501.txt', 'r')
    data = file.read()
    file.close()
    max501 = data.split('generacion')[1:]
    max501 = max501[0].split('\n')[1:]
    max501.pop(0)
    max501.pop()
    max_aux = 0
    for line in max501:
        n = line.split(": ")[1:]
        ev_cells50.append(float(n[0]))
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells50.append(max_aux)

    file = open('./results2d502.txt', 'r')
    data = file.read()
    file.close()
    max502 = data.split('generacion')[1:]
    max502 = max502[0].split('\n')[1:]
    max502.pop(0)
    max502.pop()
    max_aux = 0
    for line in max502:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells50.append(max_aux)

    file = open('./results2d503.txt', 'r')
    data = file.read()
    file.close()
    max503 = data.split('generacion')[1:]
    max503 = max503[0].split('\n')[1:]
    max503.pop(0)
    max503.pop()
    max_aux = 0
    for line in max503:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells50.append(max_aux)

    file = open('./results2d504.txt', 'r')
    data = file.read()
    file.close()
    max504 = data.split('generacion')[1:]
    max504 = max504[0].split('\n')[1:]
    max504.pop(0)
    max504.pop()
    max_aux = 0
    for line in max504:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells50.append(max_aux)

    file = open('./results2d505.txt', 'r')
    data = file.read()
    file.close()
    max505 = data.split('generacion')[1:]
    max505 = max505[0].split('\n')[1:]
    max505.pop(0)
    max505.pop()
    max_aux = 0
    for line in max505:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells50.append(max_aux)

    max_alive_cells70 = []
    ev_cells70 = []
    file = open('./results2d701.txt', 'r')
    data = file.read()
    file.close()
    max701 = data.split('generacion')[1:]
    max701 = max701[0].split('\n')[1:]
    max701.pop(0)
    max701.pop()
    max_aux = 0
    for line in max701:
        n = line.split(": ")[1:]
        ev_cells70.append(float(n[0]))
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells70.append(max_aux)

    file = open('./results2d702.txt', 'r')
    data = file.read()
    file.close()
    max702 = data.split('generacion')[1:]
    max702 = max702[0].split('\n')[1:]
    max702.pop(0)
    max702.pop()
    max_aux = 0
    for line in max702:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells70.append(max_aux)

    file = open('./results2d703.txt', 'r')
    data = file.read()
    file.close()
    max703 = data.split('generacion')[1:]
    max703 = max703[0].split('\n')[1:]
    max703.pop(0)
    max703.pop()
    max_aux = 0
    for line in max703:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells70.append(max_aux)

    file = open('./results2d704.txt', 'r')
    data = file.read()
    file.close()
    max704 = data.split('generacion')[1:]
    max704 = max704[0].split('\n')[1:]
    max704.pop(0)
    max704.pop()
    max_aux = 0
    for line in max704:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells70.append(max_aux)

    file = open('./results2d705.txt', 'r')
    data = file.read()
    file.close()
    max705 = data.split('generacion')[1:]
    max705 = max705[0].split('\n')[1:]
    max705.pop(0)
    max705.pop()
    max_aux = 0
    for line in max705:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells70.append(max_aux)

    max_alive_cells80 = []
    ev_cells80 = []
    file = open('./results2d801.txt', 'r')
    data = file.read()
    file.close()
    max801 = data.split('generacion')[1:]
    max801 = max801[0].split('\n')[1:]
    max801.pop(0)
    max801.pop()
    max_aux = 0
    for line in max801:
        n = line.split(": ")[1:]
        ev_cells80.append(float(n[0]))
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells80.append(max_aux)

    file = open('./results2d802.txt', 'r')
    data = file.read()
    file.close()
    max802 = data.split('generacion')[1:]
    max802 = max802[0].split('\n')[1:]
    max802.pop(0)
    max802.pop()
    max_aux = 0
    for line in max802:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells80.append(max_aux)

    file = open('./results2d803.txt', 'r')
    data = file.read()
    file.close()
    max803 = data.split('generacion')[1:]
    max803 = max803[0].split('\n')[1:]
    max803.pop(0)
    max803.pop()
    max_aux = 0
    for line in max803:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells80.append(max_aux)

    file = open('./results2d804.txt', 'r')
    data = file.read()
    file.close()
    max804 = data.split('generacion')[1:]
    max804 = max804[0].split('\n')[1:]
    max804.pop(0)
    max804.pop()
    max_aux = 0
    for line in max804:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells80.append(max_aux)

    file = open('./results2d805.txt', 'r')
    data = file.read()
    file.close()
    max805 = data.split('generacion')[1:]
    max805 = max805[0].split('\n')[1:]
    max805.pop(0)
    max805.pop()
    max_aux = 0
    for line in max805:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells80.append(max_aux)

    max_alive_cells90 = []
    ev_cells90 = []
    file = open('./results2d901.txt', 'r')
    data = file.read()
    file.close()
    max901 = data.split('generacion')[1:]
    max901 = max901[0].split('\n')[1:]
    max901.pop(0)
    max901.pop()
    max_aux = 0
    for line in max901:
        n = line.split(": ")[1:]
        ev_cells90.append(float(n[0]))
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells90.append(max_aux)

    file = open('./results2d902.txt', 'r')
    data = file.read()
    file.close()
    max902 = data.split('generacion')[1:]
    max902 = max902[0].split('\n')[1:]
    max902.pop(0)
    max902.pop()
    max_aux = 0
    for line in max902:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells90.append(max_aux)

    file = open('./results2d903.txt', 'r')
    data = file.read()
    file.close()
    max903 = data.split('generacion')[1:]
    max903 = max903[0].split('\n')[1:]
    max903.pop(0)
    max903.pop()
    max_aux = 0
    for line in max903:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells90.append(max_aux)

    file = open('./results2d904.txt', 'r')
    data = file.read()
    file.close()
    max904 = data.split('generacion')[1:]
    max904 = max904[0].split('\n')[1:]
    max904.pop(0)
    max904.pop()
    max_aux = 0
    for line in max904:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells90.append(max_aux)

    file = open('./results2d905.txt', 'r')
    data = file.read()
    file.close()
    max905 = data.split('generacion')[1:]
    max905 = max905[0].split('\n')[1:]
    max905.pop(0)
    max905.pop()
    max_aux = 0
    for line in max905:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells90.append(max_aux)

    max_alive_cells100 = []
    ev_cells100 = []
    file = open('./results2d1001.txt', 'r')
    data = file.read()
    file.close()
    max1001 = data.split('generacion')[1:]
    max1001 = max1001[0].split('\n')[1:]
    max1001.pop(0)
    max1001.pop()
    max_aux = 0
    for line in max1001:
        n = line.split(": ")[1:]
        ev_cells100.append(float(n[0]))
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells100.append(max_aux)

    file = open('./results2d1002.txt', 'r')
    data = file.read()
    file.close()
    max1002 = data.split('generacion')[1:]
    max1002 = max1002[0].split('\n')[1:]
    max1002.pop(0)
    max1002.pop()
    max_aux = 0
    for line in max1002:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells100.append(max_aux)

    file = open('./results2d1003.txt', 'r')
    data = file.read()
    file.close()
    max1003 = data.split('generacion')[1:]
    max1003 = max1003[0].split('\n')[1:]
    max1003.pop(0)
    max1003.pop()
    max_aux = 0
    for line in max1003:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells100.append(max_aux)

    file = open('./results2d1004.txt', 'r')
    data = file.read()
    file.close()
    max1004 = data.split('generacion')[1:]
    max1004 = max1004[0].split('\n')[1:]
    max1004.pop(0)
    max1004.pop()
    max_aux = 0
    for line in max1004:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells100.append(max_aux)

    file = open('./results2d1005.txt', 'r')
    data = file.read()
    file.close()
    max1005 = data.split('generacion')[1:]
    max1005 = max1005[0].split('\n')[1:]
    max1005.pop(0)
    max1005.pop()
    max_aux = 0
    for line in max1005:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells100.append(max_aux)

    proms = [0,0,0,0,0,0]
    min = max_alive_cells30[0]
    max = 0
    for n in max_alive_cells30:
        proms[0] += n
        if n < min:
            min = n
        if n > max:
            max = n
    proms[0] = proms[0]/len(max_alive_cells30)
    minmax30 = (proms[0]-min, max-proms[0])

    min = max_alive_cells50[0]
    max = 0
    for n in max_alive_cells50:
        proms[1] += n
        if n < min:
            min = n
        if n > max:
            max = n
    proms[1] = proms[1]/len(max_alive_cells50)
    minmax50 = (proms[1]-min, max-proms[1])

    min = max_alive_cells70[0]
    max = 0
    for n in max_alive_cells70:
        proms[2] += n
        if n < min:
            min = n
        if n > max:
            max = n
    proms[2] = proms[2]/len(max_alive_cells70)
    minmax70 = (proms[2]-min, max-proms[2])

    min = max_alive_cells80[0]
    max = 0
    for n in max_alive_cells80:
        proms[3] += n
        if n < min:
            min = n
        if n > max:
            max = n
    proms[3] = proms[3]/len(max_alive_cells80)
    minmax80 = (proms[3]-min, max-proms[3])

    min = max_alive_cells90[0]
    max = 0
    for n in max_alive_cells90:
        proms[4] += n
        if n < min:
            min = n
        if n > max:
            max = n
    proms[4] = proms[4]/len(max_alive_cells90)
    minmax90 = (proms[4]-min, max-proms[4])

    min = max_alive_cells100[0]
    max = 0
    for n in max_alive_cells100:
        proms[5] += n
        if n < min:
            min = n
        if n > max:
            max = n
    proms[5] = proms[5]/len(max_alive_cells100)
    minmax100 = (proms[5]-min, max-proms[5])

    yerr = np.array([minmax30, minmax50, minmax70, minmax80, minmax90, minmax100]).T

    max_alive_cells30 = []
    ev_cells30new = []
    file = open('./results2dnew301.txt', 'r')
    data = file.read()
    file.close()
    max301 = data.split('generacion')[1:]
    max301 = max301[0].split('\n')[1:]
    max301.pop(0)
    max301.pop()
    max_aux = 0
    for line in max301:
        n = line.split(": ")[1:]
        ev_cells30new.append(float(n[0]))
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells30.append(max_aux)

    file = open('./results2dnew302.txt', 'r')
    data = file.read()
    file.close()
    max302 = data.split('generacion')[1:]
    max302 = max302[0].split('\n')[1:]
    max302.pop(0)
    max302.pop()
    max_aux = 0
    for line in max302:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells30.append(max_aux)

    file = open('./results2dnew303.txt', 'r')
    data = file.read()
    file.close()
    max303 = data.split('generacion')[1:]
    max303 = max303[0].split('\n')[1:]
    max303.pop(0)
    max303.pop()
    max_aux = 0
    for line in max303:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells30.append(max_aux)

    file = open('./results2dnew304.txt', 'r')
    data = file.read()
    file.close()
    max304 = data.split('generacion')[1:]
    max304 = max304[0].split('\n')[1:]
    max304.pop(0)
    max304.pop()
    max_aux = 0
    for line in max304:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells30.append(max_aux)

    file = open('./results2dnew305.txt', 'r')
    data = file.read()
    file.close()
    max305 = data.split('generacion')[1:]
    max305 = max305[0].split('\n')[1:]
    max305.pop(0)
    max305.pop()
    max_aux = 0
    for line in max305:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells30.append(max_aux)

    max_alive_cells50 = []
    ev_cells50new = []
    file = open('./results2dnew501.txt', 'r')
    data = file.read()
    file.close()
    max501 = data.split('generacion')[1:]
    max501 = max501[0].split('\n')[1:]
    max501.pop(0)
    max501.pop()
    max_aux = 0
    for line in max501:
        n = line.split(": ")[1:]
        ev_cells50new.append(float(n[0]))
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells50.append(max_aux)

    file = open('./results2dnew502.txt', 'r')
    data = file.read()
    file.close()
    max502 = data.split('generacion')[1:]
    max502 = max502[0].split('\n')[1:]
    max502.pop(0)
    max502.pop()
    max_aux = 0
    for line in max502:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells50.append(max_aux)

    file = open('./results2dnew503.txt', 'r')
    data = file.read()
    file.close()
    max503 = data.split('generacion')[1:]
    max503 = max503[0].split('\n')[1:]
    max503.pop(0)
    max503.pop()
    max_aux = 0
    for line in max503:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells50.append(max_aux)

    file = open('./results2dnew504.txt', 'r')
    data = file.read()
    file.close()
    max504 = data.split('generacion')[1:]
    max504 = max504[0].split('\n')[1:]
    max504.pop(0)
    max504.pop()
    max_aux = 0
    for line in max504:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells50.append(max_aux)

    file = open('./results2dnew505.txt', 'r')
    data = file.read()
    file.close()
    max505 = data.split('generacion')[1:]
    max505 = max505[0].split('\n')[1:]
    max505.pop(0)
    max505.pop()
    max_aux = 0
    for line in max505:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells50.append(max_aux)

    max_alive_cells70 = []
    ev_cells70new = []
    file = open('./results2dnew701.txt', 'r')
    data = file.read()
    file.close()
    max701 = data.split('generacion')[1:]
    max701 = max701[0].split('\n')[1:]
    max701.pop(0)
    max701.pop()
    max_aux = 0
    for line in max701:
        n = line.split(": ")[1:]
        ev_cells70new.append(float(n[0]))
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells70.append(max_aux)

    file = open('./results2dnew702.txt', 'r')
    data = file.read()
    file.close()
    max702 = data.split('generacion')[1:]
    max702 = max702[0].split('\n')[1:]
    max702.pop(0)
    max702.pop()
    max_aux = 0
    for line in max702:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells70.append(max_aux)

    file = open('./results2dnew703.txt', 'r')
    data = file.read()
    file.close()
    max703 = data.split('generacion')[1:]
    max703 = max703[0].split('\n')[1:]
    max703.pop(0)
    max703.pop()
    max_aux = 0
    for line in max703:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells70.append(max_aux)

    file = open('./results2dnew704.txt', 'r')
    data = file.read()
    file.close()
    max704 = data.split('generacion')[1:]
    max704 = max704[0].split('\n')[1:]
    max704.pop(0)
    max704.pop()
    max_aux = 0
    for line in max704:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells70.append(max_aux)

    file = open('./results2dnew705.txt', 'r')
    data = file.read()
    file.close()
    max705 = data.split('generacion')[1:]
    max705 = max705[0].split('\n')[1:]
    max705.pop(0)
    max705.pop()
    max_aux = 0
    for line in max705:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells70.append(max_aux)

    max_alive_cells80 = []
    ev_cells80new = []
    file = open('./results2dnew801.txt', 'r')
    data = file.read()
    file.close()
    max801 = data.split('generacion')[1:]
    max801 = max801[0].split('\n')[1:]
    max801.pop(0)
    max801.pop()
    max_aux = 0
    for line in max801:
        n = line.split(": ")[1:]
        ev_cells80new.append(float(n[0]))
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells80.append(max_aux)

    file = open('./results2dnew802.txt', 'r')
    data = file.read()
    file.close()
    max802 = data.split('generacion')[1:]
    max802 = max802[0].split('\n')[1:]
    max802.pop(0)
    max802.pop()
    max_aux = 0
    for line in max802:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells80.append(max_aux)

    file = open('./results2dnew803.txt', 'r')
    data = file.read()
    file.close()
    max803 = data.split('generacion')[1:]
    max803 = max803[0].split('\n')[1:]
    max803.pop(0)
    max803.pop()
    max_aux = 0
    for line in max803:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells80.append(max_aux)

    file = open('./results2dnew804.txt', 'r')
    data = file.read()
    file.close()
    max804 = data.split('generacion')[1:]
    max804 = max804[0].split('\n')[1:]
    max804.pop(0)
    max804.pop()
    max_aux = 0
    for line in max804:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells80.append(max_aux)

    file = open('./results2dnew805.txt', 'r')
    data = file.read()
    file.close()
    max805 = data.split('generacion')[1:]
    max805 = max805[0].split('\n')[1:]
    max805.pop(0)
    max805.pop()
    max_aux = 0
    for line in max805:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells80.append(max_aux)

    max_alive_cells90 = []
    ev_cells90new = []
    file = open('./results2dnew901.txt', 'r')
    data = file.read()
    file.close()
    max901 = data.split('generacion')[1:]
    max901 = max901[0].split('\n')[1:]
    max901.pop(0)
    max901.pop()
    max_aux = 0
    for line in max901:
        n = line.split(": ")[1:]
        ev_cells90new.append(float(n[0]))
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells90.append(max_aux)

    file = open('./results2dnew902.txt', 'r')
    data = file.read()
    file.close()
    max902 = data.split('generacion')[1:]
    max902 = max902[0].split('\n')[1:]
    max902.pop(0)
    max902.pop()
    max_aux = 0
    for line in max902:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells90.append(max_aux)

    file = open('./results2dnew903.txt', 'r')
    data = file.read()
    file.close()
    max903 = data.split('generacion')[1:]
    max903 = max903[0].split('\n')[1:]
    max903.pop(0)
    max903.pop()
    max_aux = 0
    for line in max903:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells90.append(max_aux)

    file = open('./results2dnew904.txt', 'r')
    data = file.read()
    file.close()
    max904 = data.split('generacion')[1:]
    max904 = max904[0].split('\n')[1:]
    max904.pop(0)
    max904.pop()
    max_aux = 0
    for line in max904:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells90.append(max_aux)

    file = open('./results2dnew905.txt', 'r')
    data = file.read()
    file.close()
    max905 = data.split('generacion')[1:]
    max905 = max905[0].split('\n')[1:]
    max905.pop(0)
    max905.pop()
    max_aux = 0
    for line in max905:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells90.append(max_aux)

    max_alive_cells100 = []
    ev_cells100new = []
    file = open('./results2dnew1001.txt', 'r')
    data = file.read()
    file.close()
    max1001 = data.split('generacion')[1:]
    max1001 = max1001[0].split('\n')[1:]
    max1001.pop(0)
    max1001.pop()
    max_aux = 0
    for line in max1001:
        n = line.split(": ")[1:]
        ev_cells100new.append(float(n[0]))
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells100.append(max_aux)

    file = open('./results2dnew1002.txt', 'r')
    data = file.read()
    file.close()
    max1002 = data.split('generacion')[1:]
    max1002 = max1002[0].split('\n')[1:]
    max1002.pop(0)
    max1002.pop()
    max_aux = 0
    for line in max1002:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells100.append(max_aux)

    file = open('./results2dnew1003.txt', 'r')
    data = file.read()
    file.close()
    max1003 = data.split('generacion')[1:]
    max1003 = max1003[0].split('\n')[1:]
    max1003.pop(0)
    max1003.pop()
    max_aux = 0
    for line in max1003:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells100.append(max_aux)

    file = open('./results2dnew1004.txt', 'r')
    data = file.read()
    file.close()
    max1004 = data.split('generacion')[1:]
    max1004 = max1004[0].split('\n')[1:]
    max1004.pop(0)
    max1004.pop()
    max_aux = 0
    for line in max1004:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells100.append(max_aux)

    file = open('./results2d1005.txt', 'r')
    data = file.read()
    file.close()
    max1005 = data.split('generacion')[1:]
    max1005 = max1005[0].split('\n')[1:]
    max1005.pop(0)
    max1005.pop()
    max_aux = 0
    for line in max1005:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells100.append(max_aux)

    promsnew = [0,0,0,0,0,0]
    min = max_alive_cells30[0]
    max = 0
    for n in max_alive_cells30:
        promsnew[0] += n
        if n < min:
            min = n
        if n > max:
            max = n
    promsnew[0] = promsnew[0]/len(max_alive_cells30)
    minmax30 = (promsnew[0]-min, max-promsnew[0])

    min = max_alive_cells50[0]
    max = 0
    for n in max_alive_cells50:
        promsnew[1] += n
        if n < min:
            min = n
        if n > max:
            max = n
    promsnew[1] = promsnew[1]/len(max_alive_cells50)
    minmax50 = (promsnew[1]-min, max-promsnew[1])

    min = max_alive_cells70[0]
    max = 0
    for n in max_alive_cells70:
        promsnew[2] += n
        if n < min:
            min = n
        if n > max:
            max = n
    promsnew[2] = promsnew[2]/len(max_alive_cells70)
    minmax70 = (promsnew[2]-min, max-promsnew[2])

    min = max_alive_cells80[0]
    max = 0
    for n in max_alive_cells80:
        promsnew[3] += n
        if n < min:
            min = n
        if n > max:
            max = n
    promsnew[3] = promsnew[3]/len(max_alive_cells80)
    minmax80 = (promsnew[3]-min, max-promsnew[3])

    min = max_alive_cells90[0]
    max = 0
    for n in max_alive_cells90:
        promsnew[4] += n
        if n < min:
            min = n
        if n > max:
            max = n
    promsnew[4] = promsnew[4]/len(max_alive_cells90)
    minmax90 = (promsnew[4]-min, max-promsnew[4])

    min = max_alive_cells100[0]
    max = 0
    for n in max_alive_cells100:
        promsnew[5] += n
        if n < min:
            min = n
        if n > max:
            max = n
    promsnew[5] = promsnew[5]/len(max_alive_cells100)
    minmax100 = (promsnew[5]-min, max-promsnew[5])

    yerrnew = np.array([minmax30, minmax50, minmax70, minmax80, minmax90, minmax100]).T

    max_alive_cells30 = []
    ev_cells30newb = []
    file = open('./results2dnewb301.txt', 'r')
    data = file.read()
    file.close()
    max301 = data.split('generacion')[1:]
    max301 = max301[0].split('\n')[1:]
    max301.pop(0)
    max301.pop()
    max_aux = 0
    for line in max301:
        n = line.split(": ")[1:]
        ev_cells30newb.append(float(n[0]))
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells30.append(max_aux)

    file = open('./results2dnewb302.txt', 'r')
    data = file.read()
    file.close()
    max302 = data.split('generacion')[1:]
    max302 = max302[0].split('\n')[1:]
    max302.pop(0)
    max302.pop()
    max_aux = 0
    for line in max302:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells30.append(max_aux)

    file = open('./results2dnewb303.txt', 'r')
    data = file.read()
    file.close()
    max303 = data.split('generacion')[1:]
    max303 = max303[0].split('\n')[1:]
    max303.pop(0)
    max303.pop()
    max_aux = 0
    for line in max303:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells30.append(max_aux)

    file = open('./results2dnewb304.txt', 'r')
    data = file.read()
    file.close()
    max304 = data.split('generacion')[1:]
    max304 = max304[0].split('\n')[1:]
    max304.pop(0)
    max304.pop()
    max_aux = 0
    for line in max304:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells30.append(max_aux)

    file = open('./results2dnewb305.txt', 'r')
    data = file.read()
    file.close()
    max305 = data.split('generacion')[1:]
    max305 = max305[0].split('\n')[1:]
    max305.pop(0)
    max305.pop()
    max_aux = 0
    for line in max305:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells30.append(max_aux)

    max_alive_cells50 = []
    ev_cells50newb = []
    file = open('./results2dnewb501.txt', 'r')
    data = file.read()
    file.close()
    max501 = data.split('generacion')[1:]
    max501 = max501[0].split('\n')[1:]
    max501.pop(0)
    max501.pop()
    max_aux = 0
    for line in max501:
        n = line.split(": ")[1:]
        ev_cells50newb.append(float(n[0]))
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells50.append(max_aux)

    file = open('./results2dnewb502.txt', 'r')
    data = file.read()
    file.close()
    max502 = data.split('generacion')[1:]
    max502 = max502[0].split('\n')[1:]
    max502.pop(0)
    max502.pop()
    max_aux = 0
    for line in max502:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells50.append(max_aux)

    file = open('./results2dnewb503.txt', 'r')
    data = file.read()
    file.close()
    max503 = data.split('generacion')[1:]
    max503 = max503[0].split('\n')[1:]
    max503.pop(0)
    max503.pop()
    max_aux = 0
    for line in max503:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells50.append(max_aux)

    file = open('./results2dnewb504.txt', 'r')
    data = file.read()
    file.close()
    max504 = data.split('generacion')[1:]
    max504 = max504[0].split('\n')[1:]
    max504.pop(0)
    max504.pop()
    max_aux = 0
    for line in max504:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells50.append(max_aux)

    file = open('./results2dnewb505.txt', 'r')
    data = file.read()
    file.close()
    max505 = data.split('generacion')[1:]
    max505 = max505[0].split('\n')[1:]
    max505.pop(0)
    max505.pop()
    max_aux = 0
    for line in max505:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells50.append(max_aux)

    max_alive_cells70 = []
    ev_cells70newb = []
    file = open('./results2dnewb701.txt', 'r')
    data = file.read()
    file.close()
    max701 = data.split('generacion')[1:]
    max701 = max701[0].split('\n')[1:]
    max701.pop(0)
    max701.pop()
    max_aux = 0
    for line in max701:
        n = line.split(": ")[1:]
        ev_cells70newb.append(float(n[0]))
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells70.append(max_aux)

    file = open('./results2dnewb702.txt', 'r')
    data = file.read()
    file.close()
    max702 = data.split('generacion')[1:]
    max702 = max702[0].split('\n')[1:]
    max702.pop(0)
    max702.pop()
    max_aux = 0
    for line in max702:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells70.append(max_aux)

    file = open('./results2dnewb703.txt', 'r')
    data = file.read()
    file.close()
    max703 = data.split('generacion')[1:]
    max703 = max703[0].split('\n')[1:]
    max703.pop(0)
    max703.pop()
    max_aux = 0
    for line in max703:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells70.append(max_aux)

    file = open('./results2dnewb704.txt', 'r')
    data = file.read()
    file.close()
    max704 = data.split('generacion')[1:]
    max704 = max704[0].split('\n')[1:]
    max704.pop(0)
    max704.pop()
    max_aux = 0
    for line in max704:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells70.append(max_aux)

    file = open('./results2dnewb705.txt', 'r')
    data = file.read()
    file.close()
    max705 = data.split('generacion')[1:]
    max705 = max705[0].split('\n')[1:]
    max705.pop(0)
    max705.pop()
    max_aux = 0
    for line in max705:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells70.append(max_aux)

    max_alive_cells80 = []
    ev_cells80newb = []
    file = open('./results2dnewb801.txt', 'r')
    data = file.read()
    file.close()
    max801 = data.split('generacion')[1:]
    max801 = max801[0].split('\n')[1:]
    max801.pop(0)
    max801.pop()
    max_aux = 0
    for line in max801:
        n = line.split(": ")[1:]
        ev_cells80newb.append(float(n[0]))
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells80.append(max_aux)

    file = open('./results2dnewb802.txt', 'r')
    data = file.read()
    file.close()
    max802 = data.split('generacion')[1:]
    max802 = max802[0].split('\n')[1:]
    max802.pop(0)
    max802.pop()
    max_aux = 0
    for line in max802:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells80.append(max_aux)

    file = open('./results2dnewb803.txt', 'r')
    data = file.read()
    file.close()
    max803 = data.split('generacion')[1:]
    max803 = max803[0].split('\n')[1:]
    max803.pop(0)
    max803.pop()
    max_aux = 0
    for line in max803:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells80.append(max_aux)

    file = open('./results2dnewb804.txt', 'r')
    data = file.read()
    file.close()
    max804 = data.split('generacion')[1:]
    max804 = max804[0].split('\n')[1:]
    max804.pop(0)
    max804.pop()
    max_aux = 0
    for line in max804:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells80.append(max_aux)

    file = open('./results2dnewb805.txt', 'r')
    data = file.read()
    file.close()
    max805 = data.split('generacion')[1:]
    max805 = max805[0].split('\n')[1:]
    max805.pop(0)
    max805.pop()
    max_aux = 0
    for line in max805:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells80.append(max_aux)

    max_alive_cells90 = []
    ev_cells90newb = []
    file = open('./results2dnewb901.txt', 'r')
    data = file.read()
    file.close()
    max901 = data.split('generacion')[1:]
    max901 = max901[0].split('\n')[1:]
    max901.pop(0)
    max901.pop()
    max_aux = 0
    for line in max901:
        n = line.split(": ")[1:]
        ev_cells90newb.append(float(n[0]))
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells90.append(max_aux)

    file = open('./results2dnewb902.txt', 'r')
    data = file.read()
    file.close()
    max902 = data.split('generacion')[1:]
    max902 = max902[0].split('\n')[1:]
    max902.pop(0)
    max902.pop()
    max_aux = 0
    for line in max902:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells90.append(max_aux)

    file = open('./results2dnewb903.txt', 'r')
    data = file.read()
    file.close()
    max903 = data.split('generacion')[1:]
    max903 = max903[0].split('\n')[1:]
    max903.pop(0)
    max903.pop()
    max_aux = 0
    for line in max903:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells90.append(max_aux)

    file = open('./results2dnewb904.txt', 'r')
    data = file.read()
    file.close()
    max904 = data.split('generacion')[1:]
    max904 = max904[0].split('\n')[1:]
    max904.pop(0)
    max904.pop()
    max_aux = 0
    for line in max904:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells90.append(max_aux)

    file = open('./results2dnewb905.txt', 'r')
    data = file.read()
    file.close()
    max905 = data.split('generacion')[1:]
    max905 = max905[0].split('\n')[1:]
    max905.pop(0)
    max905.pop()
    max_aux = 0
    for line in max905:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells90.append(max_aux)

    max_alive_cells100 = []
    ev_cells100newb = []
    file = open('./results2dnewb1001.txt', 'r')
    data = file.read()
    file.close()
    max1001 = data.split('generacion')[1:]
    max1001 = max1001[0].split('\n')[1:]
    max1001.pop(0)
    max1001.pop()
    max_aux = 0
    for line in max1001:
        n = line.split(": ")[1:]
        ev_cells100newb.append(float(n[0]))
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells100.append(max_aux)

    file = open('./results2dnewb1002.txt', 'r')
    data = file.read()
    file.close()
    max1002 = data.split('generacion')[1:]
    max1002 = max1002[0].split('\n')[1:]
    max1002.pop(0)
    max1002.pop()
    max_aux = 0
    for line in max1002:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells100.append(max_aux)

    file = open('./results2dnewb1003.txt', 'r')
    data = file.read()
    file.close()
    max1003 = data.split('generacion')[1:]
    max1003 = max1003[0].split('\n')[1:]
    max1003.pop(0)
    max1003.pop()
    max_aux = 0
    for line in max1003:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells100.append(max_aux)

    file = open('./results2dnewb1004.txt', 'r')
    data = file.read()
    file.close()
    max1004 = data.split('generacion')[1:]
    max1004 = max1004[0].split('\n')[1:]
    max1004.pop(0)
    max1004.pop()
    max_aux = 0
    for line in max1004:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells100.append(max_aux)

    file = open('./results2d1005.txt', 'r')
    data = file.read()
    file.close()
    max1005 = data.split('generacion')[1:]
    max1005 = max1005[0].split('\n')[1:]
    max1005.pop(0)
    max1005.pop()
    max_aux = 0
    for line in max1005:
        n = line.split(": ")[1:]
        if float(n[0]) > max_aux:
            max_aux = float(n[0])
    max_alive_cells100.append(max_aux)

    promsnewb = [0,0,0,0,0,0]
    min = max_alive_cells30[0]
    max = 0
    for n in max_alive_cells30:
        promsnewb[0] += n
        if n < min:
            min = n
        if n > max:
            max = n
    promsnewb[0] = promsnewb[0]/len(max_alive_cells30)
    minmax30 = (promsnewb[0]-min, max-promsnewb[0])

    min = max_alive_cells50[0]
    max = 0
    for n in max_alive_cells50:
        promsnewb[1] += n
        if n < min:
            min = n
        if n > max:
            max = n
    promsnewb[1] = promsnewb[1]/len(max_alive_cells50)
    minmax50 = (promsnewb[1]-min, max-promsnewb[1])

    min = max_alive_cells70[0]
    max = 0
    for n in max_alive_cells70:
        promsnewb[2] += n
        if n < min:
            min = n
        if n > max:
            max = n
    promsnewb[2] = promsnewb[2]/len(max_alive_cells70)
    minmax70 = (promsnewb[2]-min, max-promsnewb[2])

    min = max_alive_cells80[0]
    max = 0
    for n in max_alive_cells80:
        promsnewb[3] += n
        if n < min:
            min = n
        if n > max:
            max = n
    promsnewb[3] = promsnewb[3]/len(max_alive_cells80)
    minmax80 = (promsnewb[3]-min, max-promsnewb[3])

    min = max_alive_cells90[0]
    max = 0
    for n in max_alive_cells90:
        promsnewb[4] += n
        if n < min:
            min = n
        if n > max:
            max = n
    promsnewb[4] = promsnewb[4]/len(max_alive_cells90)
    minmax90 = (promsnewb[4]-min, max-promsnewb[4])

    min = max_alive_cells100[0]
    max = 0
    for n in max_alive_cells100:
        promsnewb[5] += n
        if n < min:
            min = n
        if n > max:
            max = n
    promsnewb[5] = promsnewb[5]/len(max_alive_cells100)
    minmax100 = (promsnewb[5]-min, max-promsnewb[5])

    yerrnewb = np.array([minmax30, minmax50, minmax70, minmax80, minmax90, minmax100]).T

    prc = [30, 50, 70, 80, 90, 100]

    time1 = np.arange(0, len(ev_cells30), 1)
    time2 = np.arange(0, len(ev_cells50), 1)
    time3 = np.arange(0, len(ev_cells70), 1)
    time4 = np.arange(0, len(ev_cells80), 1)
    time5 = np.arange(0, len(ev_cells90), 1)
    time6 = np.arange(0, len(ev_cells100), 1)

    #plt.plot(time1, ev_cells30, label='30%')
    #plt.plot(time2, ev_cells50, label='50%')
    #plt.plot(time3, ev_cells70, label='70%')
    #plt.plot(time4, ev_cells80, label='80%')
    #plt.plot(time5, ev_cells90, label='90%')
    #plt.plot(time6, ev_cells100, label='100%')
    #plt.legend()
    #plt.xlabel('Tiempo (s)')
    #plt.ylabel('Particulas vivas')
    #plt.show()

    plt.errorbar(prc, proms, yerr, fmt='-o', label='233')
    plt.errorbar(prc, promsnew, yerrnew, fmt='-o', label='344')
    plt.errorbar(prc, promsnewb, yerrnewb, fmt='-o', label='272')
    plt.legend()
    plt.xlabel('Porcentaje (%)')
    plt.ylabel('Max celdas vivas')
    plt.show()

max_alive()