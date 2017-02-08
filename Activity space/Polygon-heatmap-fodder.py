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
env.workspace = "C:\Users\qzhao24\Dropbox (ASU)\Nepal-data\Harvesting ArcMapFiles April 24 2013\Fodder\Fodder.gdb"

inFeatures1 = ["Fodder_ID__0","Fodder_ID__1","Fodder_ID__2","Fodder_ID__3","Fodder_ID__4","Fodder_ID__5","Fodder_ID__6","Fodder_ID__7","Fodder_ID__8","Fodder_ID__9","Fodder_ID__10","Fodder_ID__11","Fodder_ID__12","Fodder_ID__13","Fodder_ID__14","Fodder_ID__15","Fodder_ID__16","Fodder_ID__17","Fodder_ID__18","Fodder_ID__19","Fodder_ID__20","Fodder_ID__21","Fodder_ID__22","Fodder_ID__23","Fodder_ID__24","Fodder_ID__25","Fodder_ID__26"]
outFeatures1 = "FodderUnion22"
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

inFeatures2 = "Fodder"
outFeatures2 = "FodderUnion1"
JoinFeatures2 = 'FodderSpatialJoin'

# Process: Union
arcpy.Union_analysis(inFeatures2,outFeatures2,"ALL", "", "GAPS")

#-------------------------------------------------------------------------------
# Step 5
# Process: Spatial Join
arcpy.SpatialJoin_analysis(outFeatures2,outFeatures1, JoinFeatures2, "JOIN_ONE_TO_ONE", "KEEP_ALL", "","ARE_IDENTICAL_TO")

#-------------------------------------------------------------------------------
# Step 6
# Process: Summary Statistics
arcpy.Statistics_analysis(JoinFeatures2, "Fodder_summary", "NewID COUNT", "NewID")

#-------------------------------------------------------------------------------
# Step 7
# Process: Join summary statistics table to St
joinField = "NewID"
arcpy.JoinField_management(outFeatures1,joinField,"Fodder_summary",joinField)

# The results are in FodderUnion22.shp, check Frequency column
end = time.time()
elapsed = end - start
print elapsed

