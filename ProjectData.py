#ProjectData.py
#
#Projects raw XY values corresponding to photo coordinates to georeferenced
# coordinates by computing the offset relative to the upper left pixel location

#Import modules
import sys, os, arcpy

#Define function to project coordinate pairs
def projectXY(X,Y,ulX,ulY,cellSize):
    return

#Get the input files
dataFile = "data.txt"           #List of raw XY coordinates, separated by spaces
tifFile = "11ska625755.tif"    #TIF file from which XY coordinates were digitized
pixelSize = 0.3                 #Cell size, in meters, if pixels in TIF file
outFile = "utmCoords.csv"

#Get the upper left coordinate from the tiff tile
tifInfo = arcpy.Describe(tifFile)
theExtent = tifInfo.Extent
upperleftX = theExtent.upperLeft.X
upperleftY = theExtent.upperLeft.Y

#Open the output file
outputData = open(outFile,'w')

#Write the header line of the output file
outputData.write("rawX, rawY, UTMX, UTMY\n")

#Open the data file
inputData = open(dataFile,'r')

#Read/skip the header line
headerString = inputData.readline()

#Loop through the remaining data lines
dataString = inputData.readline()
while dataString:
    #Get the values as a list
    dataList = dataString.split()
    #Convert the X and Y items to floating point numbers
    x = float(dataList[0])
    y = float(dataList[1])
    #Convert raw coordinates to projected coordinates
    adjustedX = (x * pixelSize) + upperleftX
    adjustedY = upperleftY - (y * pixelSize)
    #Write to a file
    outputData.write("{},{},{},{}\n".format(x,y,adjustedX,adjustedY))
    #Move to the next line
    dataString = inputData.readline()

#Close the files
inputData.close()
outputData.close()
