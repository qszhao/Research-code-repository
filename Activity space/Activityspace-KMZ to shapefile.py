#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      qzhao24
#
# Created:     26/01/2016
# Copyright:   (c) qzhao24 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcpy
import os
import time

indir = "C:\Users\qzhao24\Desktop\Acitivty Space Data October 2015-From Scott\Tablet_Data_957\Tablet_Data_957"
outdir = "C:\Users\qzhao24\Desktop\Acitivty Space Data October 2015-From Scott\KMZ_to_shapefile"
intermediate = "C:\\Users\\qzhao24\\Desktop\\NTL_point"



for fkmz in os.listdir(indir):
    start = time.time()
    if fkmz.endswith(".kmz"):
        file1 = fkmz
        print file1

# Process: KMZ to shapefile
        arcpy.KMLToLayer_conversion(os.path.join(indir,file1), outdir, file1, "NO_GROUNDOVERLAY")

    end = time.time()
    elapsed = end - start
    print elapsed