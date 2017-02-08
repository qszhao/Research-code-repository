def area(roof,facade,window):

    csv_f1 = csv.reader(roof)
    csv_f2 = csv.reader(facade)
    csv_f3 = csv.reader(window)

################
##### Roof #####
################
    lighted1 = []
    time1 = []
    shade1 = []
    time2 = []
    ninehalf = []
    ten = []
    tenhalf = []
    eleven = []
    elevenhalf = []
    twelve = []
    twelvehalf = []
    thirteen = []
    thirteenhalf = []
    fourteen = []
    fourteenhalf = []
    fifteen = []
    fifteenhalf = []
    shadearea1 = []

    for row in csv_f1:
        lighted1.append(row[3])
        time1.append(row[1])
#    print lighted1
#    print time1

    # jump over the errors, calculate shade area
    for i in range(len(lighted1)):
        try:
            shade1.append(100-float(lighted1[i]))
        except:
            pass
    # create hour lists
    for j in range(len(time1)-2):
        time2.append((time1[j+2][:5]))


    for k in range(len(time2)):
        if time2[k] == '09:30':
            ninehalf.append(shade1[k])
        if time2[k] == '10:00':
            ten.append(shade1[k])
        if time2[k] == '10:30':
            tenhalf.append(shade1[k])
        if time2[k] == '11:00':
            eleven.append(shade1[k])
        if time2[k] == '11:30':
            elevenhalf.append(shade1[k])
        if time2[k] == '12:00':
            twelve.append(shade1[k])
        if time2[k] == '12:30':
            twelvehalf.append(shade1[k])
        if time2[k] == '13:00':
            thirteen.append(shade1[k])
        if time2[k] == '13:30':
            thirteenhalf.append(shade1[k])
        if time2[k] == '14:00':
            fourteen.append(shade1[k])
        if time2[k] == '14:30':
            fourteenhalf.append(shade1[k])
        if time2[k] == '15:00':
            fifteen.append(shade1[k])
        if time2[k] == '15:30':
            fifteenhalf.append(shade1[k])
#    print ninehalf
#    print ten
#    Average shade area
    for l in range(4):
        shadearea1.append((ninehalf[l] + ten[l] + tenhalf[l] + eleven[l] + elevenhalf[l] + twelve[l] + twelvehalf[l] + thirteen[l] + thirteenhalf[l] + fourteen[l] + fourteenhalf[l] + fifteen[l] + fifteenhalf[l])/13)
#    print shadearea1
#    print "\n"
#    month = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
#    dictionary1 = dict(zip(month, shadearea1))
##################
##### Facade #####
##################
    lighted1 = []
    time1 = []
    shade1 = []
    time2 = []
    ninehalf = []
    ten = []
    tenhalf = []
    eleven = []
    elevenhalf = []
    twelve = []
    twelvehalf = []
    thirteen = []
    thirteenhalf = []
    fourteen = []
    fourteenhalf = []
    fifteen = []
    fifteenhalf = []
    shadearea2 = []

    for row in csv_f2:
        lighted1.append(row[3])
        time1.append(row[1])
#    print lighted1
#    print time1
    # jump over the errors, calculate shade area
    for i in range(len(lighted1)):
        try:
            shade1.append(100-float(lighted1[i]))
        except:
            pass
    # create hour lists
    for j in range(len(time1)-2):
        time2.append((time1[j+2][:5]))

    for k in range(len(time2)):
        if time2[k] == '09:30':
            ninehalf.append(shade1[k])
        if time2[k] == '10:00':
            ten.append(shade1[k])
        if time2[k] == '10:30':
            tenhalf.append(shade1[k])
        if time2[k] == '11:00':
            eleven.append(shade1[k])
        if time2[k] == '11:30':
            elevenhalf.append(shade1[k])
        if time2[k] == '12:00':
            twelve.append(shade1[k])
        if time2[k] == '12:30':
            twelvehalf.append(shade1[k])
        if time2[k] == '13:00':
            thirteen.append(shade1[k])
        if time2[k] == '13:30':
            thirteenhalf.append(shade1[k])
        if time2[k] == '14:00':
            fourteen.append(shade1[k])
        if time2[k] == '14:30':
            fourteenhalf.append(shade1[k])
        if time2[k] == '15:00':
            fifteen.append(shade1[k])
        if time2[k] == '15:30':
            fifteenhalf.append(shade1[k])

    for l in range(4):
        shadearea2.append((ninehalf[l] + ten[l] + tenhalf[l] + eleven[l] + elevenhalf[l] + twelve[l] + twelvehalf[l] + thirteen[l] + thirteenhalf[l] + fourteen[l] + fourteenhalf[l] + fifteen[l] + fifteenhalf[l])/13)
#    print shadearea2
#    print "\n"
#    month = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
#    dictionary2 = dict(zip(month, shadearea2))

###################
##### Windows #####
###################
    lighted1 = []
    time1 = []
    shade1 = []
    time2 = []
    ninehalf = []
    ten = []
    tenhalf = []
    eleven = []
    elevenhalf = []
    twelve = []
    twelvehalf = []
    thirteen = []
    thirteenhalf = []
    fourteen = []
    fourteenhalf = []
    fifteen = []
    fifteenhalf = []
    shadearea3 = []
    area = []
    for row in csv_f3:
        lighted1.append(row[6])
        time1.append(row[1])
#    print lighted1
#    print time1
    # jump over the errors, calculate shade area
    for i in range(len(lighted1)):
        try:
            shade1.append(100-float(lighted1[i]))
        except:
            pass
    # create hour lists
    for j in range(len(time1)-2):
        time2.append((time1[j+2][:5]))

    for k in range(len(time2)):
        if time2[k] == '09:30':
            ninehalf.append(shade1[k])
        if time2[k] == '10:00':
            ten.append(shade1[k])
        if time2[k] == '10:30':
            tenhalf.append(shade1[k])
        if time2[k] == '11:00':
            eleven.append(shade1[k])
        if time2[k] == '11:30':
            elevenhalf.append(shade1[k])
        if time2[k] == '12:00':
            twelve.append(shade1[k])
        if time2[k] == '12:30':
            twelvehalf.append(shade1[k])
        if time2[k] == '13:00':
            thirteen.append(shade1[k])
        if time2[k] == '13:30':
            thirteenhalf.append(shade1[k])
        if time2[k] == '14:00':
            fourteen.append(shade1[k])
        if time2[k] == '14:30':
            fourteenhalf.append(shade1[k])
        if time2[k] == '15:00':
            fifteen.append(shade1[k])
        if time2[k] == '15:30':
            fifteenhalf.append(shade1[k])

    for l in range(4):
        shadearea3.append((ninehalf[l] + ten[l] + tenhalf[l] + eleven[l] + elevenhalf[l] + twelve[l] + twelvehalf[l] + thirteen[l] + thirteenhalf[l] + fourteen[l] + fourteenhalf[l] + fifteen[l] + fifteenhalf[l])/13)
#    print shadearea3
#    print "\n"
#    month = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
#    dictionary3 = dict(zip(month, shadearea3))


#####################################
## Weighted shade area
    for i in range(4):
        area.append((shadearea1[i]*108.5*(0.1)+shadearea2[i]*45*0.3+shadearea3[i]*9*0.6)/100)
#    print area
    return area


def main():

    import fileinput
    from glob import glob

    t = []

    file = open("0.6_0.3_0.1.txt","wb")


    r = glob('Roof*.csv')
    f = glob('facade*.csv')
    w = glob('window*.csv')

    for i in range(9):

        roof = open(r[i])
        facade = open(f[i])
        win = open(w[i])

        t.append(area(roof,facade,win))
# limit three digit of decimal points
    for i in range(9):
        for j in range(4):
            print ("%0.3f" %t[i][j])
#            file.write("%0.3f" %t[i][j])
#            file.write("\n")
        print "\n"

#    max = sorted(t, reverse = True)
#    print max

    file.close

    roof.close()
    facade.close()
    win.close()

if __name__ == '__main__':
    import csv
    main()