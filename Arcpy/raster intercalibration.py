#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      qzhao24
#
# Created:     06/11/2015
# Copyright:   (c) qzhao24 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Import system modules
# Check out Map Algebra
# http://resources.arcgis.com/EN/HELP/MAIN/10.1/index.html#//00p600000003000000
# http://resources.arcgis.com/de/help/main/10.1/index.html#//005m000000mm000000

import arcpy,os
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:\\Users\\qzhao24\\Desktop\\NTL_DMSPOLS_2000_2011"

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Set local variables
indir = "C:\\Users\\qzhao24\\Desktop\\NTL_DMSPOLS_2000_2011"
outdir = "C:\\Users\\qzhao24\\Desktop\\NTL-intercalibration"

# Read intercalibration data
fp = open('intercalibration_parameter.txt','r')
line = fp.readline()
serial = line.split()
row = int(serial[0])
column = int(serial[1])

lines = fp.readlines()
parameter = []
for l in lines:
	parameter = [map(str,l.strip().split()) for l in lines]

i = 0

for ftif in os.listdir(indir):
    if ftif.endswith("clip.tif"):
        file1 = ftif
        print file1

        image = Raster(os.path.join(indir,file1))

        a = float(parameter[i][0])
        b = float(parameter[i][1])
        c = float(parameter[i][2])

# Execute intercalibration
        outRaster = image * image * a + image * b + c

# Save the output
        outRaster.save(os.path.join(outdir,file1))
        i += 1

