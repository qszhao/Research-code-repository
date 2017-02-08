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
# Prepare individual polygons (Here we have 35 grass polygons, then we need 35 feature classes.)
env.workspace = "C:\Users\qzhao24\Dropbox (ASU)\Nepal-data\Harvesting ArcMapFiles April 24 2013\Grass\Grass.gdb"

inFeatures1 = ["Grass_ID__0","Grass_ID__1","Grass_ID__2","Grass_ID__3","Grass_ID__4","Grass_ID__5","Grass_ID__6","Grass_ID__7","Grass_ID__8","Grass_ID__9","Grass_ID__10","Grass_ID__11","Grass_ID__12","Grass_ID__13","Grass_ID__14","Grass_ID__15","Grass_ID__16","Grass_ID__17","Grass_ID__18","Grass_ID__19","Grass_ID__20","Grass_ID__21","Grass_ID__22","Grass_ID__23","Grass_ID__24","Grass_ID__25","Grass_ID__26","Grass_ID__27","Grass_ID__28","Grass_ID__29","Grass_ID__30","Grass_ID__31","Grass_ID__32","Grass_ID__33","Grass_ID__34"]
outFeatures1 = "GrassUnion35"
fieldName = "NewID"
# Process: Union
arcpy.Union_analysis(inFeatures1,outFeatures1,"ALL", "", "GAPS")

# Process: Add Field
arcpy.AddField_management(outFeatures1, fieldName, "LONG")

# Process: Calculate Field
arcpy.CalculateField_management(outFeatures1, fieldName, "!OBJECTID!", "PYTHON_9.3", "")

#-------------------------------------------------------------------------------

# Step 3 was finished outside.
# One feature class with all the polygons. (make sure )
#-------------------------------------------------------------------------------
# Step 4

inFeatures2 = "Grass"
outFeatures2 = "GrassUnion1"
JoinFeatures2 = 'GrassSpatialJoin'

# Process: Union
arcpy.Union_analysis(inFeatures2,outFeatures2,"ALL", "", "GAPS")

#-------------------------------------------------------------------------------
# Step 5
# Process: Spatial Join
arcpy.SpatialJoin_analysis(outFeatures2,outFeatures1, JoinFeatures2, "JOIN_ONE_TO_ONE", "KEEP_ALL", "","ARE_IDENTICAL_TO")

#-------------------------------------------------------------------------------
# Step 6
# Process: Summary Statistics
arcpy.Statistics_analysis(JoinFeatures2, "Grass_summary", "NewID COUNT", "NewID")

#-------------------------------------------------------------------------------
# Step 7
# Process: Join summary statistics table to St
joinField = "NewID"
arcpy.JoinField_management(outFeatures1,joinField,"Grass_summary",joinField)

# The results are in GrassUnion22.shp, check Frequency column
end = time.time()
elapsed = end - start
print elapsed

