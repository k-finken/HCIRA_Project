import math
from tkinter import *
import os
import xml.etree.ElementTree as ET
from xml.dom import minidom
import csv
import numpy as np

# X and Y point class
class Point:
    # Initialize point
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # Get X
    def getX(self):
        return self.x
    # Get Y
    def getY(self):
        return self.y

# Class to Hold Drawn Canvas Points
class Shape:
    # Initialize Shape
    def __init__(self, points=[], label=""):
        self.points = points
        self.label = label
    # Get Points
    def getPoints(self):
        return self.points
    # Add Point
    def addPoint(self, x, y):
        self.points.append(Point(x, y))
    # Add Points
    def setPoints(self, points):
        self.points = points
    # Clear Points
    def clearPoints(self):
        self.points = []
    # Print Points
    def printPoints(self):
        for i in range(len(self.points)):
            print(self.points[i].getX(), self.points[i].getY())
    # Get Label
    def getLabel(self):
        return self.label
    # Set Label
    def setLabel(self, label):
        self.label = label
    # Export to XML
    def exportToXML(self, user, gesture, iteration, saveDir="dataset"):
        # Define file name
        name = gesture + str(iteration).zfill(2)
        # Create gesture root and add properties
        root = minidom.Document()
        gesture = root.createElement("Gesture")
        gesture.setAttribute("Name", name)
        gesture.setAttribute("Subject", str(user).zfill(2))
        gesture.setAttribute("Number", str(iteration).zfill(2))
        gesture.setAttribute("NumPts", str(len(self.points)))
        root.appendChild(gesture)
        # Write the points to the XML file
        T = 0 # Theoretical time value for future progrm
        for i in range(len(self.points)):
            point = root.createElement("Point")
            point.setAttribute("X", str(self.points[i].getX()))
            point.setAttribute("Y", str(self.points[i].getY()))
            point.setAttribute("T", str(T))
            gesture.appendChild(point)
            T += 1
        # Save
        directory = saveDir + "/s" + str(user).zfill(2) + "/"
        # Create directory if it doesn't exist
        if not os.path.exists(directory):
            os.makedirs(directory)
        # Write XML file
        with open(directory + name + ".xml", "w") as f:
            f.write(root.toprettyxml(indent="\t"))

def readXML(rootDir):
    outputArr = []
    for subdir, dirs, files in os.walk(rootDir, topdown=True):
        # Sorts order to ensure consistency across platforms
        dirs.sort(reverse=False)
        files.sort(reverse=False)
        for file in files:
            # Print path to file
            # print(os.path.join(subdir, file))
            # Read in as XML
            xmlFile = ET.parse(os.path.join(subdir, file))
            # Get root element
            root = xmlFile.getroot()
            # Get gesture label
            gestureLabel = root.get("Name") + "," + root.get("Subject")
            # Get Points
            points = []
            for child in root:
                # Store x variable of point in x
                x = int(child.get("X"))
                # story y variable of point in y
                y = int(child.get("Y"))
                # add point to array of points p
                points.append(Point(x, y))
            # Create shape
            s = Shape(points, gestureLabel)
            # Add shape to array
            outputArr.append(s)
    return outputArr

# Pass directory to load collected data
collectedData = readXML("data-collected")

print(len(collectedData))

for i in range(len(collectedData)):
    unparsedName = collectedData[i].getLabel()
    parsedName = unparsedName.split(",")
    # Get Seperate user and gesture labels
    userNum = parsedName[1]
    # Split gesture label
    gesture = parsedName[0]
    gestureName, gestureIteration = gesture[:-2], gesture[-2:]
    print(gestureName, gestureIteration, userNum)
    # Write to XML
    collectedData[i].exportToXML(userNum, gestureName, gestureIteration, "data-collected-timed")


