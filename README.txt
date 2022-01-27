HCIRA Project 1


//**HOW TO USE**//
To run, open the executable located in the dist folder.
Once the canvas is open you can go ahead and draw and the $1 algorithms guess will pop up following your single-stroke drawing.
Following your drawing clear the canvas using the TAB key and then you are free to draw again.

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

