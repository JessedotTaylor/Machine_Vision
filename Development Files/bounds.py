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

height, width, depth = 480, 640, 3
img = np.full((height,width, depth),(255,255,255), np.uint8)

#random.seed(4)

maxXValue = height
maxYValue = width
thickness = 5
noPoints = 10
center = (random.randint(int(height /3), int(height /3) * 2), random.randint(int(width /3), int(width /3) * 2))
distance = 300
#print(center, distance)


# x = [random.randrange(0,maxXValue) for i in range(noPoints)]
# y = [random.randrange(0,maxYValue) for i in range(noPoints)]

x = np.random.randint(center[0], center[0] + distance, size=(int(noPoints * 0.8,)))
x = np.append(x, [random.randrange(0,maxXValue) for i in range(int(noPoints* 0.2))])
y = np.random.randint(center[1], center[1] + distance, size=(int(noPoints * 0.8,)))
y = np.append(y, [random.randrange(0,maxYValue) for i in range(int(noPoints* 0.2))])
# x = [10,10,50, 10,10,50, 469,469,424, 469,469,424]
# y = [10,50,10, 629,594,629, 10,50,10, 629,594,629]

for i in range(noPoints):
    cv2.line(img, (y[i],x[i]),(y[i],x[i]) , (0,0,0), thickness)


# def getDist(points, x):
#     return [math.sqrt(x**2 + i**2) for i in points]

# def avgDist(points, x, noPoints):
#     return sum(getDist(points, x)) / noPoints
        

# # startX = random.randint(0, maxXValue)
# startY = random.randint(0, maxYValue)
# #cv2.line(img, (startY,startX),(startY+1,startX+1) , (255,0,0), thickness)


# workingX = height
# step = height / 2
# oldavgDist = avgDist(x, workingX, noPoints)
# change = 1

def getDist(targ, org):
    return(math.sqrt(((targ[0] - org[0]) **2)  + (targ[1] - org[1]) **2))

centroid = (int(sum(y) / noPoints), int(sum(x) / noPoints))
#print(centroid)
cv2.line(img, centroid,centroid, (255,0,0), thickness)

deltaX = 10
deltaY = 10

while deltaX > 5 or deltaY > 5:
    currMax = 0
    largestInd = 0
    for i in range(noPoints):
        dist = getDist((y[i], x[i]), centroid)
        if dist > currMax:
            currMax = dist
            largestInd = i

    tempX = x[largestInd]
    tempY = y[largestInd]
    x = np.delete(x, largestInd)   
    y = np.delete(y, largestInd) 
    #print(tempX, tempY)
    noPoints -= 1

    newCentroid = (int(sum(y) / noPoints), int(sum(x) / noPoints))
    deltaX = centroid[1] - newCentroid[1]
    deltaY = centroid[0] - newCentroid[0]
    centroid = newCentroid

    #print(deltaX, deltaY)
    cv2.line(img, (tempY, tempX), (tempY, tempX), (0,0,255), thickness)
    cv2.line(img, centroid, centroid, (255,0,0), thickness)
    cv2.imshow('img', img)
    cv2.waitKey(0)




np.append(x, tempX)
np.append(y, tempY)
noPoints += 1




# sortedX = x.sort()
# lowerBound = 0
# upperBound = len(x)
# step = upperBound / 2



# while change > 0.01:
#     workingX -= step
#     newAvgDist = avgDist(x, workingX, noPoints)
#     if oldavgDist < newAvgDist:
#         step = -step
#     step = step / 2
#     change = abs(oldavgDist - newAvgDist)
#     oldavgDist = newAvgDist
#     print(step, change, newAvgDist, workingX, startY)
    
#     cv2.line(img, (startY,int(workingX)),(startY+1,int(workingX)+1) , (255,0,0), thickness)
    #cv2.putText(img, str(change) ,(startY,int(workingX)), cv2.FONT_HERSHEY_COMPLEX, .5, (255,0,0))


cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



#print(getDist(x, startX))



#print(x)

# plt.axis("off")
# plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2HSV))
# plt.show()