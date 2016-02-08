#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Qunshan
#
# Created:     03/03/2014
# Copyright:   (c) Qunshan 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def moveGeomToPoint(geometry, x, y):
    """Returns a geometry whose coordinates are shifted such that the new centroid is located at the coordinates x and y"""
    # Get the current centroid
    oldCentroid = geometry.TrueCentroid

    # Get the delta x and y factors
    dX = x - oldCentroid.x
    dY = y - oldCentroid.y

    # Print details of translation
    print "Current Centroid: (%.12F, %.12F)" % (oldCentroid.x, oldCentroid.y)
    print "New Centroid: (%.12F, %.12F)" % (x, y)
    print "dX, dY: (%.12F, %.12F)" % (dX, dY)

    # Check if geometry is point first
    if geometry.type == "point":
        # Get the existing point object
        pnt = geometry.GetPart()

        # Create a new point object and assign to it the new translated coordinates
        newPnt = gp.CreateObject("Point")
        newPnt.x = pnt.x + dX
        newPnt.y = pnt.y + dY

        # Return the new point instead of going through all the parts
        return newPnt

    # Keep track of where we are in the geometry array
    partnum = 0
    partcount = geometry.PartCount

    # Create a new geometry array -- this is what we are ultimately going to return
    newGeom = gp.CreateObject("Array")

    # Loop through all of the parts in the geometry array
    while partnum < partcount:
        print "Part " + str(partnum) + ":"
        part = geometry.GetPart(partnum)

        # Create a new array just for the part we are currently on
        newPart = gp.CreateObject("Array")

        # Get the first vertex of the current part
        pnt = part.Next()
        pntcount = 0

        # Enter while loop for each vertex
        while pnt:
            # Print x,y coordinates of current point and new point
            oldX = pnt.x
            oldY = pnt.y
            newX = oldX + dX
            newY = oldY + dY
            #print "%.12F, %.12F --> %.12F, %.12F" % (oldX, oldY, newX, newY)

            # Create a new point object and assign to it the new translated coordinates
            newPnt = gp.CreateObject("Point")
            newPnt.x = newX
            newPnt.y = newY

            # Add the new point object to the new part array
            newPart.add(newPnt)

            pnt = part.Next()
            pntcount += 1

            # If pnt is null, either the part is finished or there is an interior ring
            if not pnt:
                pnt = part.Next()
                if pnt:
                    print "Interior Ring:"
        # Add the new part to the new geometry array
        newGeom.add(newPart)
        partnum += 1
    return newGeom
###########################################################################################


def main():

    import arcgisscripting
    import arcpy
    import numpy as np
    global gp,xx,yy,hh,h,t,xxx,yyy
    gp = arcgisscripting.create(10.1)

    roof33_1011 = "C:\\Users\\Qunshan\\Desktop\\Research\\export\\roof33_1011.shp"
    roof33_1112 = "C:\\Users\\Qunshan\\Desktop\\Research\\export\\dissovle_1112.shp"
    roof33_1213 = "C:\\Users\\Qunshan\\Desktop\\Research\\export\\roof33_1213.shp"
    roof33_1314 = "C:\\Users\\Qunshan\\Desktop\\Research\\export\\roof33_1314.shp"
    roof33_1415 = "C:\\Users\\Qunshan\\Desktop\\Research\\export\\roof33_1415.shp"
    h = 0
    fp = open('point.txt','r')
    #fp = open('point1.txt','r')

    lines = fp.readlines()
    point = [map(float,l.strip().split()) for l in lines]
    num = 0
    for l in lines:
        num = num+1
    fp.close()

    fpp = open('treepoint_error_1415.txt','r')

    line = fpp.readline()
    lines = fpp.readlines()
    point1 = [map(float,l.strip().split()) for l in lines]
    fpp.close()
    xx = []
    yy = []
    xxx = 0
    yyy = 0
    hh = []
    t = 0
    print point1[0][2]
    print point1[0][3]
    for i in range(num):
        x = point[i][0]
        y = point[i][1]
        # Ignore north part of the area
        if y > 3697249:
            continue

        rows = gp.UpdateCursor(roof33_1415)
        row = rows.Next()
# If not intersect, continue
        try:
            while row:
                # Based on the shadow centroid and the tree centroid
                row.shape = moveGeomToPoint(row.shape, x+point1[0][2] , y+point1[0][3])
                rows.updateRow(row)
                row = rows.Next()

                # Local variables:
                onehouse1 = "C:\\Users\\Qunshan\\Desktop\\Research\\export\\onehouse1.shp"
                intersect123 = "C:\\Users\\Qunshan\\Desktop\\Research\\export\\intersect123.shp"
                area1_shp = "C:\\Users\\Qunshan\\Desktop\\Research\\export\\area1.shp"
                v1011dissolvenew_shp = "C:\\Users\\Qunshan\\Desktop\\Research\\export\\1011dissolvenew.shp"
                v1011raster2 = "C:\\Users\\Qunshan\\Desktop\\Research\\export\\1011raster2"


                if arcpy.Exists(intersect123):
                    arcpy.Delete_management(intersect123)
                if arcpy.Exists(area1_shp):
                    arcpy.Delete_management(area1_shp)


                # Process: Intersect
                arcpy.Intersect_analysis([onehouse1,roof33_1415], intersect123,"NO_FID")

                # Process: Calculate Areas
                arcpy.CalculateAreas_stats(intersect123, area1_shp)

                # Process: Add Field
                arcpy.AddField_management(area1_shp, "percentage", "DOUBLE", "3", "3", "", "", "NULLABLE", "NON_REQUIRED", "")

                # Process: Calculate Field
                arcpy.CalculateField_management(area1_shp, "percentage", "!F_AREA! / !Area!", "PYTHON", "")

                input = "C:\\Users\\Qunshan\\Desktop\\Research\\export\\area1.shp"
                arr = arcpy.da.TableToNumPyArray(input, ('percentage'))
                arrlist = arr.tolist()

                if arrlist[0] > h:
                    h = arrlist[0]
                    print h
                    xxx = point[i][0]
                    yyy = point[i][1]
            del row
            del rows

            xx.append(x)
            yy.append(y)
            hh.append(arrlist[0])
            t += 1
        except:
            xx.append(x)
            yy.append(y)
            hh.append(0)
            t += 1
            continue

    rows = gp.UpdateCursor(roof33_1415)
    row = rows.Next()
    # Based on the shadow centroid and the tree centroid
    row.shape = moveGeomToPoint(row.shape, xxx+point1[0][2] , yyy+point1[0][3])
    rows.updateRow(row)
    row = rows.Next()
    del row
    del rows

def output():
    outfile = open('optimalpoint_1415.txt', 'w')
    outfile.write ("During 14-15 am: Possible point location:\n")
    for i in range(t):
        if h == hh[i]:
            outfile.write("%f " %xx[i])
            outfile.write("%f\n" %yy[i])

    outfile.write("Maximal coverage percentage:")
    outfile.write("%f\n"%h)

    outfile.write("Location coordinates now:")
    outfile.write("%f %f"%(xxx,yyy))


    outfile1 = open('xyp_1415.txt', 'w')
    for i in range(t):
        outfile1.write("%f " %xx[i])
        outfile1.write("%f " %yy[i])
        outfile1.write("%f\n" %hh[i])

if __name__ == '__main__':
    import time
    start = time.clock()
    main()
    output()
    elapse = time.clock() - start
    print ("Time(second):%f"%elapse)
