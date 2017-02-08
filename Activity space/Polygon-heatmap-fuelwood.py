#-------------------------------------------------------------------------------
# Name:        Polygon-heatmap
# Purpose:     Generate polygon overlap frequncy by using Arcpy, refer to http://gis.stackexchange.com/questions/48803/how-to-create-a-heat-map-or-density-map-from-stacked-polygons-in-arcmap-10
#
# Author:      Qunshan Zhao
#
# Created:     09/01/2016
# Copyright:   (c) qzhao24 2016
# Licence:     <your licence>
#------------------------------------------------------------------------------

import arcpy
import time
from arcpy import env

start = time.time()

#-------------------------------------------------------------------------------
# Step 1 and 2
# Prepare individual polygons (Here we have 27 fodder polygons, then we need 27 feature classes.)
env.workspace = "C:\Users\qzhao24\Dropbox (ASU)\Nepal-data\Harvesting ArcMapFiles April 24 2013\Fuelwood\Fuelwood.gdb"

inFeatures1 = ["Fuelwood_ID__0","Fuelwood_ID__1","Fuelwood_ID__2","Fuelwood_ID__3","Fuelwood_ID__4","Fuelwood_ID__5","Fuelwood_ID__6","Fuelwood_ID__7","Fuelwood_ID__8","Fuelwood_ID__9","Fuelwood_ID__10","Fuelwood_ID__11","Fuelwood_ID__12","Fuelwood_ID__13","Fuelwood_ID__14","Fuelwood_ID__15","Fuelwood_ID__16","Fuelwood_ID__17","Fuelwood_ID__18"]
outFeatures1 = "FuelwoodUnion22"
fieldName = "NewID"
# Process: Union
arcpy.Union_analysis(inFeatures1,outFeatures1,"ALL", "", "GAPS")

# Process: Add Field
arcpy.AddField_management(outFeatures1, fieldName, "LONG")

# Process: Calculate Field
arcpy.CalculateField_management(outFeatures1, fieldName, "!OBJECTID!", "PYTHON_9.3", "")

#-------------------------------------------------------------------------------

# Step 3 was finished outside.
# One feature class with all the polygons
#-------------------------------------------------------------------------------
# Step 4

inFeatures2 = "Fuelwood"
outFeatures2 = "FuelwoodUnion1"
JoinFeatures2 = 'FuelwoodSpatialJoin'

# Process: Union
arcpy.Union_analysis(inFeatures2,outFeatures2,"ALL", "", "GAPS")

#-------------------------------------------------------------------------------
# Step 5
# Process: Spatial Join
arcpy.SpatialJoin_analysis(outFeatures2,outFeatures1, JoinFeatures2, "JOIN_ONE_TO_ONE", "KEEP_ALL", "","ARE_IDENTICAL_TO")

#-------------------------------------------------------------------------------
# Step 6
# Process: Summary Statistics
arcpy.Statistics_analysis(JoinFeatures2, "Fuelwood_summary", "NewID COUNT", "NewID")

#-------------------------------------------------------------------------------
# Step 7
# Process: Join summary statistics table to St
joinField = "NewID"
arcpy.JoinField_management(outFeatures1,joinField,"Fuelwood_summary",joinField)

# The results are in FuelwoodUnion22.shp, check Frequency column
end = time.time()
elapsed = end - start
print elapsed

