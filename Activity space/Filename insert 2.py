#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      qzhao24
#
# Created:     29/01/2016
# Copyright:   (c) qzhao24 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Import standard library modules
import arcpy, os, sys
from arcpy import env
import time

# Allow for file overwrite
arcpy.env.overwriteOutput = True

# Set the workspace directory
# Files need to be shapefile.
env.workspace = r"C:\Users\qzhao24\Desktop\Best_route_shapefile"

# Get the list of the featureclasses to process
fc_tables = arcpy.ListFeatureClasses()

# Loop through each file and perform the processing
for fc in fc_tables:

    start = time.time()

    print str("processing " + fc)

    # Define field name and expression
    field = "FILENAME"
    expression = str(fc) #populates field

    # Create a new field with a new name
    arcpy.AddField_management(fc,field,"TEXT")

    # Calculate field here
    # The expression part is tricky.
    arcpy.CalculateField_management(fc, field, "'"+ expression+"'", "PYTHON")

    end = time.time()
    elapsed = end - start
    print elapsed

