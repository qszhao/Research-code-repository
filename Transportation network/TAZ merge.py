f1 = open("D1_D2.txt", "r")
f2 = open("D1_D2_2.txt", "w")
line = f1.readline()
f2.write("TAZ_Centroid_ID" + " " + "Junction_ID" + '\n')
while line:
    # p = line.rfind(' ')
    line1 = line.split()
    # for i in line1:
    Id = line1[0]
    idh = line1[1]
    dh = int(line1[2])
    ids = line1[3]
    ds = int(line1[4])
    if dh / ds >= 2:
        if dh < 1609:
            d = idh
        else:
            d = ids
    elif dh / ds < 1.25:
        d = idh
    else:
        if dh > 6437:
            d = ids
        else:
            d = idh
    f2.write(Id + " " + d + '\n')
    line = f1.readline()
f1.close()
f2.close()
