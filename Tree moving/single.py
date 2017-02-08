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
    print avg3


    area = (avg1*16.2*0.5+0.25*avg2*45.7-0.25*avg3*98.4)/100
 #   print area


    return area


def main():

    t = []
    westw = open('west2win.csv')
    westf = open('west2facade.csv')
    westr = open('west2roof.csv')

    eastw = open('east2win.csv')
    eastf = open('east2facade.csv')
    eastr = open('east2roof.csv')

    originw = open('north1win.csv')
    originf = open('north1facade.csv')
    originr = open('north1roof.csv')

    t.append(area(westw,westf,westr))
    t.append(area(eastw,eastf,eastr))
    t.append(area(originw,originf,originr))

    file = open("secondstep.txt","wb")

    file.write("West is: %f \n" %float(t[0]))
    file.write("East is: %f \n" %float(t[1]))
    file.write("Origin is: %f \n" %float(t[2]))

    print t

if __name__ == '__main__':
    import csv
    main()