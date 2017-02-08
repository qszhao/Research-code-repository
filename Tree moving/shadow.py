# create buildings
# this program calculates building generate file
# equations from http://pveducation.org/pvcdrom
# do not use negative signs in the longitude

import math
import string

class datatype:

    #def __init__(self, tree_id, lon, lat, xcoord, ycoord, height):
    #def __init__(self, tree_id, xcoord, ycoord, height, lon, lat):
    def __init__(self, xcoord, ycoord, tree_id, height, lon, lat):
            self.tree_id = int(tree_id)
            self.lon = float(lon)
            self.lat = float(lat)
            self.xcoord = float(xcoord)
            self.ycoord = float(ycoord)
            self.height = float(height)

    def getTreeId(self):
        return self.tree_id

    def getLat(self):
        return self.lat

    def getLon(self):
        return self.lon

    def getXcoord(self):
        return self.xcoord

    def getYcoord(self):
        return self.ycoord

    def getHeight(self):
        return self.height

def main():

    mylist = []
    open_file(mylist)
    gen_time(mylist)
    print "done"

def open_file(mylist):

    #fname = raw_input("Enter filename: ")
    #infile = open(fname, 'r')
    infile = open('roof33.txt','r')
    for line in infile:
        #tree_id, lon, lat, xcoord, ycoord, height = string.split(line)
        #n = datatype(tree_id, lon, lat, xcoord, ycoord, height)
        #tree_id, xcoord, ycoord, height, lon, lat= string.split(line)
        #n = datatype(tree_id, xcoord, ycoord, height, lon, lat)
        xcoord, ycoord, tree_id, height, lon, lat= string.split(line)
        n = datatype(xcoord, ycoord, tree_id, height, lon, lat)
        mylist.append(n)
    infile.close
    return mylist

def gen_time(mylist):
    fname = raw_input("Enter output filename: ")
    outfile = open(fname, 'w')
    outfile.write("Polygon\n")
    t = 1
    for i in mylist:
# 3.3 based on the average height of the roof
        height = i.getHeight()-3.3
        outfile.write("%d 0\n" % (t))
        outfile.write("0 %f %f\n" % (i.getXcoord(),i.getYcoord()))

        for LT in range(13,15):
            HRA = calcHRA(i, LT)
            elevation = calcElevation(i, HRA)
            print elevation
           # print elevation
            if elevation > 0:
                azimuth = calcAzimuth(i, HRA, LT)
                print azimuth
                #print azimuth
                shadow_length = height / math.tan(math.radians(elevation))
                newCoords = calcNewXY(i, shadow_length, azimuth)


                #outfile.write("0 %f %f\n" % (i.getXcoord(),i.getYcoord()))
                outfile.write("%d %f %f\n" % ((LT-9),newCoords[0],newCoords[1]))
               # outfile.write("%f\n" % (shadow_length))
               # outfile.write("end\n")
        t+=1
        outfile.write("%d %f %f\n" % ((LT-9+1),i.getXcoord(),i.getYcoord()))
    outfile.write("END")
    outfile.close
    return

def calcDeclinationAngle():
    # August 15th/16th
    T = 226.0
    angle = .9863 * (T - 81.0)
    psi = 23.45 * calcSin(angle)
    return psi

def calcHRA(i, LT):
    LSTM = -15 * 7.0 # Local standard time meridian
    T = 226.0  # 226 days after January 1st
    B = .9863 * (T - 81) #
    EoT = 9.87 * calcSin(2*B) - 7.53 * calcCos(B) - 1.5 * calcSin(B)
    # Equation of time
    TC = 4 * (i.getLon() - LSTM) + EoT  # Time correction factor
    #Longitude is negative, problems
    LST = LT + (TC / 60.0) # local solar time
    #print ("local solar time is",LST)
    HRA = 15 * (LST - 12) # Hour angle
    return HRA

def calcNewXY(i, shadow_length, azimuth):
 #   theta = 270 - azimuth
 #   x = i.getXcoord() + shadow_length * calcCos(theta)
 #   y = i.getYcoord() + shadow_length * calcSin(theta)
   # print azimuth
    if azimuth < 180:
        theta = 180 - azimuth
        x = i.getXcoord() - shadow_length * calcSin(theta)
        y = i.getYcoord() + shadow_length * calcCos(theta)
        newcoords = [x,y]
    else:
        theta = azimuth - 180
        x = i.getXcoord() + shadow_length * calcSin(theta)
        y = i.getYcoord() + shadow_length * calcCos(theta)
        newcoords = [x,y]
    return newcoords

def calcElevation(i, HRA):
    psi = calcDeclinationAngle()
    phi = i.getLat()
    alpha = (calcCos(phi) * calcCos(psi) * calcCos(HRA)) + (calcSin(psi) * calcSin(phi))
    n = math.degrees(calcArcSin(alpha))
    return n

def calcAzimuth(i, HRA, LT):
    psi = calcDeclinationAngle()
    phi = i.getLat()
    alpha = 90 - phi + psi
    temp = ((calcSin(psi) * calcCos(phi) - (calcCos(psi) * calcSin(phi) * calcCos(HRA))) / calcCos(alpha))
    #problem for the angle
    n = math.degrees(calcArcCos(temp))

    LSTM = 15 * 7.0 # Local standard time meridian
    T = 226.0  # 226 days after January 1st
    B = .9863 * (T - 81) #
    EoT = 9.87 * calcSin(2*B) - 7.53 * calcCos(B) - 1.5 * calcSin(B)
    # Equation of time
    TC = 4 * (i.getLon() - LSTM) + EoT  # Time correction factor
    LST = LT + (TC / 60.0) # local solar time

    if HRA > 0 or LST > 12:
        n = 360 - n
    #Problematic
    return n

def calcCos(a):
    return math.cos(math.radians(a))

def calcSin(a):
    return math.sin(math.radians(a))

def calcArcCos(a):
    return math.acos(a)

def calcArcSin(a):
    return math.asin(a)

if __name__ == '__main__':main()
