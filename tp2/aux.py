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