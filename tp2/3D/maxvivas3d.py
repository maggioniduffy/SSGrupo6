import matplotlib.pyplot as plt
import numpy as np

def max_alive():
    max_alive_cells30 = []
    ev_cells30 = []
    file = open('./results3da301.txt', 'r')
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

    file = open('./results3da302.txt', 'r')
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

    file = open('./results3da303.txt', 'r')
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

    file = open('./results3da304.txt', 'r')
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

    file = open('./results3da305.txt', 'r')
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
    file = open('./results3da501.txt', 'r')
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

    file = open('./results3da502.txt', 'r')
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

    file = open('./results3da503.txt', 'r')
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

    file = open('./results3da504.txt', 'r')
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

    file = open('./results3da505.txt', 'r')
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
    file = open('./results3da701.txt', 'r')
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

    file = open('./results3da702.txt', 'r')
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

    file = open('./results3da703.txt', 'r')
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

    file = open('./results3da704.txt', 'r')
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

    file = open('./results3da705.txt', 'r')
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
    file = open('./results3da801.txt', 'r')
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

    file = open('./results3da802.txt', 'r')
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

    file = open('./results3da803.txt', 'r')
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

    file = open('./results3da804.txt', 'r')
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

    file = open('./results3da805.txt', 'r')
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
    file = open('./results3da901.txt', 'r')
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

    file = open('./results3da902.txt', 'r')
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

    file = open('./results3da903.txt', 'r')
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

    file = open('./results3da904.txt', 'r')
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

    file = open('./results3da905.txt', 'r')
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
    file = open('./results3da1001.txt', 'r')
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

    file = open('./results3da1002.txt', 'r')
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

    file = open('./results3da1003.txt', 'r')
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

    file = open('./results3da1004.txt', 'r')
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

    file = open('./results3da1005.txt', 'r')
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
    file = open('./results3db301.txt', 'r')
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

    file = open('./results3db302.txt', 'r')
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

    file = open('./results3db303.txt', 'r')
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

    file = open('./results3db304.txt', 'r')
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

    file = open('./results3db305.txt', 'r')
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
    file = open('./results3db501.txt', 'r')
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

    file = open('./results3db502.txt', 'r')
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

    file = open('./results3db503.txt', 'r')
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

    file = open('./results3db504.txt', 'r')
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

    file = open('./results3db505.txt', 'r')
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
    file = open('./results3db701.txt', 'r')
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

    file = open('./results3db702.txt', 'r')
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

    file = open('./results3db703.txt', 'r')
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

    file = open('./results3db704.txt', 'r')
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

    file = open('./results3db705.txt', 'r')
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
    file = open('./results3db801.txt', 'r')
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

    file = open('./results3db802.txt', 'r')
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

    file = open('./results3db803.txt', 'r')
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

    file = open('./results3db804.txt', 'r')
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

    file = open('./results3db805.txt', 'r')
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
    file = open('./results3db901.txt', 'r')
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

    file = open('./results3db902.txt', 'r')
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

    file = open('./results3db903.txt', 'r')
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

    file = open('./results3db904.txt', 'r')
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

    file = open('./results3db905.txt', 'r')
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
    file = open('./results3db1001.txt', 'r')
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

    file = open('./results3db1002.txt', 'r')
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

    file = open('./results3db1003.txt', 'r')
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

    file = open('./results3db1004.txt', 'r')
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

    file = open('./results3da1005.txt', 'r')
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
    file = open('./results3dc301.txt', 'r')
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

    file = open('./results3dc302.txt', 'r')
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

    file = open('./results3dc303.txt', 'r')
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

    file = open('./results3dc304.txt', 'r')
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

    file = open('./results3dc305.txt', 'r')
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
    file = open('./results3dc501.txt', 'r')
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

    file = open('./results3dc502.txt', 'r')
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

    file = open('./results3dc503.txt', 'r')
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

    file = open('./results3dc504.txt', 'r')
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

    file = open('./results3dc505.txt', 'r')
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
    file = open('./results3dc701.txt', 'r')
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

    file = open('./results3dc702.txt', 'r')
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

    file = open('./results3dc703.txt', 'r')
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

    file = open('./results3dc704.txt', 'r')
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

    file = open('./results3dc705.txt', 'r')
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
    file = open('./results3dc801.txt', 'r')
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

    file = open('./results3dc802.txt', 'r')
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

    file = open('./results3dc803.txt', 'r')
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

    file = open('./results3dc804.txt', 'r')
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

    file = open('./results3dc805.txt', 'r')
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
    file = open('./results3dc901.txt', 'r')
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

    file = open('./results3dc902.txt', 'r')
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

    file = open('./results3dc903.txt', 'r')
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

    file = open('./results3dc904.txt', 'r')
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

    file = open('./results3dc905.txt', 'r')
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
    file = open('./results3dc1001.txt', 'r')
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

    file = open('./results3dc1002.txt', 'r')
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

    file = open('./results3dc1003.txt', 'r')
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

    file = open('./results3dc1004.txt', 'r')
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

    file = open('./results3da1005.txt', 'r')
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

    time1 = np.arange(0, len(ev_cells30newb), 1)
    time2 = np.arange(0, len(ev_cells50newb), 1)
    time3 = np.arange(0, len(ev_cells70newb), 1)
    time4 = np.arange(0, len(ev_cells80newb), 1)
    time5 = np.arange(0, len(ev_cells90newb), 1)
    time6 = np.arange(0, len(ev_cells100newb), 1)

    plt.plot(time1, ev_cells30newb, label='30%')
    plt.plot(time2, ev_cells50newb, label='50%')
    plt.plot(time3, ev_cells70newb, label='70%')
    plt.plot(time4, ev_cells80newb, label='80%')
    plt.plot(time5, ev_cells90newb, label='90%')
    plt.plot(time6, ev_cells100newb, label='100%')
    plt.legend()
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Particulas vivas')
    plt.show()

    #plt.errorbar(prc, proms, yerr, fmt='-o', label='455')
    #plt.errorbar(prc, promsnew, yerrnew, fmt='-o', label='576')
    #plt.errorbar(prc, promsnewb, yerrnewb, fmt='-o', label='565')
    #plt.legend()
    #plt.xlabel('Porcentaje (%)')
    #plt.ylabel('Max celdas vivas')
    #plt.show()

max_alive()