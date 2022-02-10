HCIRA Project 1

1/20

//**HOW TO USE**//
To run, open the executable located in the dist folder.
Once the canvas is open you can go ahead and draw and the $1 algorithms guess will pop up following your single-stroke drawing.
Following your drawing clear the canvas using the TAB key and then you are free to draw again.

1/27

//**COMPONENTS**//
1. Resampling:
Resample(points, n) function begins on line 131 and ends on line 150 and utilizes the point class which holds an x and y value in each point object and is defined on 10-20.
This function also utilizes the pathLength(points) function that is defined on lines 125-129

2. Rotation:
This component utilizes 3 functions: centroid(points), rotateBy(points, theta), and rotateToZero(points).
These functions are defined from lines 154-175, and also utilize the point class.

3. Scaling+Translation:
This component utilizes 3 functions: boundingBox(points), scaleToSquare(points,size), and translateToOrigin(points)
These functions are defined from lines 178-208, and also utilize the point class.

4. Matching Process:
This component utilizes 4 functions: pathDistance(pointsA, pointsB), distanceAtBestAngle(points, T, thetaA, thetaB, threshold), recognize(points, templates), and distanceAtAngle(points, T, theta)
These functions are defined from lines 212-255, and also utilize the point class as well as the constant PHI which is defined on line 117.

2/3

//**COMPONENTS**//
1. Read in Dataset:
Function readXML(rootDir) on line 53 serves to read in all the data from the folder labeled xml. This iterative process goes through each file in a top down approach and creates Shape() objects from the provided points. Later after resampling, the data is separated on lines 349-374 by user, speed, gesture, and trial (NOTE: this part of the code is currently bugged, the users[] array presents differently in the loop where data is added vs outside of the loop)

2. Connect to Recognizer:
Lines 330-340 serve to resample the input data. The data is then run through the recognizer on line 485 during the loop over the dataset.

3. Loop over Dataset:
Lines 385-420 serve to recreate the random-100 loop that was covered in class.

4. Output the Result:
Currently, the result of the looped tests are printed to the console on lines 413-417. CSV exporting functionality is being implemented following line 420.