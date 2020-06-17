import cv2
import numpy as np 
import random, math

white = [255,255,255]
red = [0,0,255]
blue = [255,0,0]
green = [0,255,0]
yellow = [0,255,255]
cyan = [255,255,0]
mag = [255,0,255]
black = [0,0,0]
colourList = [white, red, blue, green, yellow, cyan, mag]
lenColourList = len(colourList)

def getColour(x):
    if x >= lenColourList:
        x = x % lenColourList
    return colourList[x]

def getDist(targ, org):
    return(math.sqrt(((targ[0] - org[0]) **2)  + (targ[1] - org[1]) **2))

height, width, depth = 480, 640, 3
img = np.full((height,width, depth),(255,255,255), np.uint8)


maxXValue = height
maxYValue = width
thickness = 5
noPoints = 10
center = (random.randint(int(height /3), int(height /3) * 2), random.randint(int(width /3), int(width /3) * 2))
distance = 300

x = np.random.randint(center[0], center[0] + distance, size=(int(noPoints * 0.8,)))
x = np.append(x, [random.randrange(0,maxXValue) for i in range(int(noPoints* 0.2))])
y = np.random.randint(center[1], center[1] + distance, size=(int(noPoints * 0.8,)))
y = np.append(y, [random.randrange(0,maxYValue) for i in range(int(noPoints* 0.2))])

for i in range(noPoints):
    cv2.line(img, (x[i],y[i]),(x[i],y[i]) , (0,0,0), thickness)

centroid = (int(sum(x) / noPoints), int(sum(y) / noPoints))
#print(centroid)
cv2.line(img, centroid,centroid, (255,0,0), thickness)

deltaX = 10
deltaY = 10

while deltaX > 5 or deltaY > 5:
    currMax = 0
    largestInd = 0
    for i in range(noPoints):
        dist = getDist((x[i], y[i]), centroid)
        if dist > currMax:
            currMax = dist
            largestInd = i

    tempX = x[largestInd]
    tempY = y[largestInd]
    x = np.delete(x, largestInd)   
    y = np.delete(y, largestInd) 
    noPoints -= 1

    newCentroid = (int(sum(x) / noPoints), int(sum(y) / noPoints))
    deltaX = centroid[0] - newCentroid[0]
    deltaY = centroid[1] - newCentroid[1]
    centroid = newCentroid

    cv2.line(img, (tempX, tempY), (tempX, tempY), (0,0,255), thickness)
    cv2.line(img, centroid, centroid, (255,0,0), thickness)
    cv2.imshow('img', img)
    cv2.waitKey(0)

np.append(x, tempX)
np.append(y, tempY)
noPoints += 1

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
