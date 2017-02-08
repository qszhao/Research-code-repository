#-------------------------------------------------------------------------------
# Name:        Polygon-heatmap
# Purpose:     Generate polygon overlap frequncy by using Arcpy, refer to http://gis.stackexchange.com/questions/48803/how-to-create-a-heat-map-or-density-map-from-stacked-polygons-in-arcmap-10
#
# Author:      qzhao24
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
# Prepare individual polygons (Here we have 23 grazing polygons, then we need 23 feature classes.)
env.workspace = "C:\Users\qzhao24\Dropbox (ASU)\Nepal-data\Harvesting ArcMapFiles April 24 2013\Grazing-split-by-QGIS\Grazing.gdb"

inFeatures = ["Grazing_ID__0","Grazing_ID__1","Grazing_ID__2","Grazing_ID__3","Grazing_ID__4","Grazing_ID__5","Grazing_ID__6","Grazing_ID__7","Grazing_ID__8","Grazing_ID__9","Grazing_ID__10","Grazing_ID__11","Grazing_ID__12","Grazing_ID__13","Grazing_ID__14","Grazing_ID__15","Grazing_ID__16","Grazing_ID__17","Grazing_ID__18","Grazing_ID__19","Grazing_ID__20","Grazing_ID__21","Grazing_ID__22"]
outFeatures = "GrazingUnion22"
fieldName = "NewID"
# Process: Union
arcpy.Union_analysis(inFeatures,outFeatures,"ALL", "", "GAPS")

# Process: Add Field
arcpy.AddField_management(outFeatures, fieldName, "LONG")

# Process: Calculate Field
arcpy.CalculateField_management(outFeatures, fieldName, "!OBJECTID!", "PYTHON_9.3", "")

#-------------------------------------------------------------------------------

# Step 3 was finished outside.
# One feature class with all the polygons
#-------------------------------------------------------------------------------
# Step 4
env.workspace = "C:\Users\qzhao24\Dropbox (ASU)\Nepal-data\Harvesting ArcMapFiles April 24 2013\Grazing-original\Grazing.gdb"

inFeatures = "Grazing"
outFeatures = "GrazingUnion1"
JoinFeatures = 'GrazingSpatialJoin'

# Process: Union
arcpy.Union_analysis(inFeatures,outFeatures,"ALL", "", "GAPS")

#-------------------------------------------------------------------------------
# Step 5
# Process: Spatial Join
arcpy.SpatialJoin_analysis(outFeatures,"C:\Users\qzhao24\Dropbox (ASU)\Nepal-data\Harvesting ArcMapFiles April 24 2013\Grazing-split-by-QGIS\Grazing.gdb\GrazingUnion22", JoinFeatures, "JOIN_ONE_TO_ONE", "KEEP_ALL", "","ARE_IDENTICAL_TO")

#-------------------------------------------------------------------------------
# Step 6
# Process: Summary Statistics
arcpy.Statistics_analysis(JoinFeatures, "Grazing_summary", "NewID COUNT", "NewID")

#-------------------------------------------------------------------------------
# Step 7
# Process: Join summary statistics table to St
joinField = "NewID"
arcpy.JoinField_management("C:\Users\qzhao24\Dropbox (ASU)\Nepal-data\Harvesting ArcMapFiles April 24 2013\Grazing-split-by-QGIS\Grazing.gdb\GrazingUnion22",joinField,"Grazing_summary",joinField)

end = time.time()
elapsed = end - start
print elapsed
