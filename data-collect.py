import math
from tkinter import *
import os
# import xml.etree.ElementTree as ET
from xml.dom import minidom
import csv
import numpy as np

# GLOBAL VARIABLES
gestureNames = ['arrow','caret','check','circle','delete_mark','left_curly_brace','left_sq_bracket','pigtail','zigzag','rectangle','right_curly_brace','right_sq_bracket','star','triangle','v','x']
currentGestureIndex = 0
gestureIteration = 1
# Change this depending on previously collected data
currentUserNum = 1

# Base Classes
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
    def exportToXML(self, user, gesture, iteration):
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
        for i in range(len(self.points)):
            point = root.createElement("Point")
            point.setAttribute("X", str(self.points[i].getX()))
            point.setAttribute("Y", str(self.points[i].getY()))
            gesture.appendChild(point)
        # Save
        directory = "dataset/" + "s" + str(user).zfill(2) + "/"
        # Create directory if it doesn't exist
        if not os.path.exists(directory):
            os.makedirs(directory)
        # Write XML file
        with open(directory + name + ".xml", "w") as f:
            f.write(root.toprettyxml(indent="\t"))

# Initialize GUI
app = Tk()
app.title("Project 1 Canvas")
app.geometry("400x400")
drawnShape = Shape()

# Event Handler Functions
def clear(event):
    canvas.delete('all')
    drawnShape.clearPoints()
    canvas.create_text(5, 10, text="Hello User #" + str(currentUserNum), fill="black", font=('Helvetica 10 bold'),anchor=NW)
    canvas.create_text(5, 25, text="Please draw a " + gestureNames[currentGestureIndex] + " without releasing the left mouse button.", fill="black", font=('Helvetica 8 bold'),anchor=NW)
    canvas.create_text(5, 40, text="Submit by pressing the ENTER/RETURN button. Clear by pressing TAB.", fill="black",font=('Helvetica 8 bold'), anchor=NW)
    canvas.create_text(5, 55, text=str(11 - gestureIteration) + " trials remaining.", fill="black",font=('Helvetica 8 bold'), anchor=NW)
def get_x_and_y(event):
    global curx, cury
    curx, cury = event.x, event.y

def draw(event):
    global curx, cury
    canvas.create_line((curx, cury, event.x, event.y), fill='red', width=2)
    curx, cury = event.x, event.y
    # Store location of point
    drawnShape.addPoint(curx, cury)

def saveXML(event):
    global currentGestureIndex, gestureIteration, currentUserNum
    drawnShape.exportToXML(currentUserNum, gestureNames[currentGestureIndex], gestureIteration)
    # Update after drawing
    gestureIteration += 1
    if gestureIteration == 11:
        gestureIteration = 1
        currentGestureIndex += 1
        if currentGestureIndex == len(gestureNames):
            currentGestureIndex = 0
            currentUserNum += 1
            if currentUserNum == 11:
                currentUserNum = 1
    # Clear canvas
    canvas.delete('all')
    drawnShape.clearPoints()
    # Update Title
    canvas.create_text(5, 10, text="Hello User #" + str(currentUserNum), fill="black", font=('Helvetica 10 bold'), anchor=NW)
    canvas.create_text(5, 25, text="Please draw a " + gestureNames[currentGestureIndex] + " without releasing the left mouse button.", fill="black", font=('Helvetica 8 bold'), anchor=NW)
    canvas.create_text(5, 40, text="Submit by pressing the ENTER/RETURN button. Clear by pressing TAB.", fill="black", font=('Helvetica 8 bold'), anchor=NW)
    canvas.create_text(5, 55, text= str(11 - gestureIteration) + " trials remaining.", fill="black", font=('Helvetica 8 bold'), anchor=NW)

# Handle Canvas
canvas = Canvas(app, bg='grey')
canvas.pack(anchor='nw', fill='both', expand=1)

# Instructions
canvas.create_text(5, 10, text="Hello User #" + str(currentUserNum), fill="black", font=('Helvetica 10 bold'), anchor=NW)
canvas.create_text(5, 25, text="Please draw a " + gestureNames[currentGestureIndex] + " without releasing the left mouse button.", fill="black", font=('Helvetica 8 bold'), anchor=NW)
canvas.create_text(5, 40, text="Submit by pressing the ENTER/RETURN button. Clear by pressing TAB.", fill="black", font=('Helvetica 8 bold'), anchor=NW)
canvas.create_text(5, 55, text= str(11 - gestureIteration) + " trials remaining.", fill="black", font=('Helvetica 8 bold'), anchor=NW)

canvas.bind("<Button-1>", get_x_and_y)
canvas.bind("<B1-Motion>", draw)
app.bind("<Tab>", clear) # Tab to clear
app.bind("<Return>", saveXML) # Enter to record gesture
app.mainloop()