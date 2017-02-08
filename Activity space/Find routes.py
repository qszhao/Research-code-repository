# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Find routes.py
# Created on: 2017-02-05 16:18:21.00000
#   Qunshan Zhao
# Description:
# This is a script to calculate the best routes for each household activites
# starting from home. (Activty space projects)
# ---------------------------------------------------------------------------

class LicenseError(Exception):
    pass

# Set desktop license used to Basic (keyword is arcview)
# http://desktop.arcgis.com/en/arcmap/10.4/analyze/python/access-to-licensing-and-extensions.htm#GUID-4B9662C3-6C73-43F4-B005-0D2797D5EF75

import arcpy
import os
import time
from arcpy import env

onlyoneactivity = []
# make it possible to overwrite all the existing feature classes
# https://geonet.esri.com/thread/121285
arcpy.env.overwriteOutput = True

try:
    if arcpy.CheckExtension("Network") == "Available":
        arcpy.CheckOutExtension("Network")
    else:
        # Raise a custom exception
        raise LicenseError

#Set local variables
    inNetworkDataset = r'C:\Users\qzhao24\Dropbox (ASU)\Nepal-data\Neighborhood-network\Neighborhood.gdb\Nepal_network\Nepal_network_ND'
#    inStops = r'C:\Users\qzhao24\Desktop\Activity_last_week_split\Activity_last_week_new_ID_text__001099003.shp'
    outGeodatabase = r'C:\Users\qzhao24\Desktop\Best_route\Best_Route.gdb'
    measurement_units = "Meters"

    indir = "C:\Users\qzhao24\Desktop\Remaining"
    for fshp in os.listdir(indir):
        if fshp.endswith(".shp"):
            file1 = fshp
            print file1
# get the last 9 digit of the file name
# http://stackoverflow.com/questions/646644/how-to-get-last-items-of-a-list-in-python
            outRoutes = "Routes" + os.path.splitext(file1)[0][-9:]
            outRouteEdges = "RouteEdges"+ os.path.splitext(file1)[0][-9:]
            outDirections = "Directions"+ os.path.splitext(file1)[0][-9:]
            outStops = "Stops"+ os.path.splitext(file1)[0][-9:]
            start = time.time()

            # Run FindRoutes. Reorder the stops to find the fastest route, but maintain
            # the last stop as the end point.
            # http://pro.arcgis.com/en/pro-app/arcpy/get-started/error-handling-with-python.htm#GUID-67136187-389D-4627-93CB-C47DFE1E46F2 (try except statement)
            try:
                arcpy.na.FindRoutes(os.path.join(indir,file1), measurement_units, inNetworkDataset, outGeodatabase, outRoutes, outRouteEdges, outDirections, outStops, Reorder_Stops_to_Find_Optimal_Routes=True, Preserve_Terminal_Stops="PRESERVE_LAST")
            except Exception:
                onlyoneactivity.append(os.path.splitext(file1)[0][-9:])
                print onlyoneactivity
                continue

            end = time.time()
            elapsed = end - start
            print "Script completed successfully"
            print elapsed

except Exception as e:
    # If an error occurred, print line number and error message
    import traceback, sys
    tb = sys.exc_info()[2]
    print "An error occured on line %i" % tb.tb_lineno
    print str(e)

except LicenseError:
    print("Network Analyst license is unavailable")
except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))
finally:
    # Check in the ArcGIS Network Analyst extension
    arcpy.CheckInExtension("Network")

