def area(win,facade,roof):

    csv_f1 = csv.reader(win)
    csv_f2 = csv.reader(facade)
    csv_f3 = csv.reader(roof)

#############################
    light1 = []
    lighted1 = []
    shade1 = []
    t1 = 0.0
    for row in csv_f1:

        light1.append(row[6])

    #print light1

    for i in range(7):

        lighted1.append(float(light1[i+6]))

    #print lighted1

    for i in range(7):
    
        shade1.append(100-lighted1[i])

    for i in range(7):
        t1 += shade1[i]

    avg1 = t1/7
##############################
    light2 = []
    lighted2 = []
    shade2 = []
    t2 = 0.0
    for row in csv_f2:

        light2.append(row[4])

    #print light2

    for i in range(7):

        lighted2.append(float(light2[i+6]))

    #print lighted2

    for i in range(7):
   
        shade2.append(100-lighted2[i])

    for i in range(7):
        t2 += shade2[i]

    avg2 = t2/7

################################
    light3 = []
    lighted3 = []
    shade3 = []
    t3 = 0.0
    for row in csv_f3:

        light3.append(row[6])

    #print light3

    for i in range(7):

        lighted3.append(float(light3[i+6]))

    #print lighted3

    for i in range(7):
       
        shade3.append(100-lighted3[i])

    for i in range(7):
        t3 += shade3[i]

    avg3 = t3/7


#####################################

    area = (avg1*16.2*0.5+0.25*avg2*45.7+0.25*avg3*98.4)/100
    print area


    return area


def main():

    t = []

    file = open("0.5_0.25_0.25_small.txt","wb")
    
    import fileinput
    from glob import glob

    r = glob('roof*.csv')
    f = glob('facade*.csv')
    w = glob('win*.csv')

    for i in range(10):


        roof = open(r[i])
        facade = open(f[i])
        win = open(w[i])
 
        t.append(area(win,facade,roof))
        
        file.write("%f\n" %float(t[i]))
        file.write("%s\n" %(r[i]))


#    max = sorted(t, reverse = True)
#    print max

    file.close

    roof.close()
    facade.close()
    win.close()

if __name__ == '__main__':
    import csv
    main()