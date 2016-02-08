# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Activityspace.py
# Created on: 2016-01-26 16:41:55.00000
#   (generated by ArcGIS/ModelBuilder)
# Description:
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy
import os
import time


#indir = "C:\Users\qzhao24\Desktop\Acitivty Space Data October 2015-From Scott\KMZ_to_shapefile"
indir = "C:\Users\qzhao24\Desktop\Acitivty Space Data October 2015-From Scott\KMZ_to_shapefile"
outdir = "C:\Users\qzhao24\Desktop\Acitivty Space Data October 2015-From Scott\New SDE\GDB_projection"

from arcpy import env

for fgdb in os.listdir(indir):

    start = time.time()

    if fgdb.endswith(".gdb"):
        file1 = fgdb
        print file1
        env.workspace = os.path.join(indir,file1)

        datasetList = arcpy.ListDatasets("*", "Feature")
        for dataset in datasetList:
            print dataset
# here you are creating a list of all features from your workspace
            fcList = arcpy.ListFeatureClasses("*","",dataset)
# and here you are looping
            for fc in fcList:
                print fc
# Make use to use the right name. (without .kml)

# Process: Project
                arcpy.Project_management(fc, os.path.join(outdir,os.path.splitext(file1)[0][0:9]), "PROJCS['WGS_1984_UTM_Zone_45N',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',87.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]", "", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", "NO_PRESERVE_SHAPE", "")


    end = time.time()
    elapsed = end - start
    print elapsed