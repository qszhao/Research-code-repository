# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# DN2Temp.py
# Created on: 2015-10-29 19:49:38.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy
import os

arcpy.env.overwriteOutput = True
# Check out any necessary licenses
arcpy.CheckOutExtension("spatial")

indir = "E:\\UHI\\Landsat\\thermal\\masked"
outdir = "E:\\UHI\\Landsat\\thermal\\temperature"
intermediate_m = "E:\\UHI\\Landsat\\thermal\\intermediate_m"
intermediate_t = "E:\\UHI\\Landsat\\thermal\\intermediate_t"
intermediate_p = "E:\\UHI\\Landsat\\thermal\\intermediate_p"
lmax_5 = 15.303
lmin_5 = 1.238
qcalmax = 255
qcalmin = 1
k1_5 = 607.76
k2_5 = 1260.56

lmax_7 = 12.65
lmin_7 = 3.2
k1_7 = 666.09
k2_7 = 1282.71
# Local variables:
for ftif in os.listdir(indir):
    if ftif.endswith(".tif"):
        file = os.path.join(indir, ftif)
        fname = ftif
        print file
        if os.path.splitext(file)[0][0:2] == "LT":
            arcpy.gp.Minus_sa(file, 1, os.path.join(intermediate_m,fname))
            arcpy.gp.Times_sa(os.path.join(intermediate_m,fname), 0.055374, os.path.join(intermediate_t,fname))
            arcpy.gp.Plus_sa(os.path.join(intermediate_t,fname), lmin_5, os.path.join(intermediate_p,fname))
        else:
            arcpy.gp.Minus_sa(file, 1, os.path.join(intermediate_m,fname))
            arcpy.gp.Times_sa(os.path.join(intermediate_m,fname), 0.037204, os.path.join(intermediate_t,fname))
            arcpy.gp.Plus_sa(os.path.join(intermediate_t,fname), lmin_7, os.path.join(intermediate_p,fname))
        output = os.path.join(outdir,os.path.splitext(fname)[0] + "_temperature.tif")
