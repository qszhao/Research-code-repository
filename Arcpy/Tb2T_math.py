# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Tb2T_math.py
# Created on: 2015-10-22 14:04:05.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import os
import arcpy

arcpy.env.overwriteOutput = True
# Check out any necessary licenses
arcpy.CheckOutExtension("spatial")

indir = "D:\\UHI\\masked"
outdir = "D:\\UHI\\temperature"
intermediate = "D:\\UHI\\intermediate"
# Local variables:
for ftif in os.listdir(indir):
    if ftif.endswith(".tif"):
        file = ftif
        print file
        output = os.path.join(outdir,os.path.splitext(file)[0] + "_temperature.tif")
        
# Process: Divide
        arcpy.gp.Divide_sa(os.path.join(indir,file), 10, os.path.join(intermediate,file))
# Process: Times (2)
        arcpy.gp.Times_sa(os.path.join(intermediate,file), 0.98, os.path.join(outdir, output))
