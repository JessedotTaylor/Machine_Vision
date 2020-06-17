import cv2
import numpy as np
from datetime import datetime


def main(img, step):
    output = img.copy()
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    height, width, depth = imgHSV.shape
    #print(height, width, depth)


    upper_blue = np.array([120, 255, 255])
    lower_blue = np.array([50, 80, 40])

    th1 = cv2.inRange(imgHSV, lower_blue, upper_blue)

    elementSize = 15 
    element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*elementSize+1,2*elementSize+1), (elementSize, elementSize))
    th1 = cv2.erode(th1, element)
    # cv2.imshow('th1', th1)
    # cv2.waitKey(0)

    maxX = 0
    minX = width
    maxY = 0
    minY = height

    # avgSize = 1
    # maxX = [0] * avgSize
    # minX = [height] * avgSize
    # maxY = [0] * avgSize
    # minY = [width] * avgSize

    # def addTo(l, item):
    #     l.pop(0)
    #     l = l.append(item)

    # def getSmallest(l):
    #     return min(l)

    # def getBiggest(l):
    #     return max(l)

    # print(th1[400, 230])
    # cv2.line(th1, (400,230), (400,230), 0, 10)
    # cv2.imshow('output', output)
    # cv2.waitKey(0)


    #start = datetime.now()
    # for i in range(height):
    #     currMin = next((j for j in range(width) if th1[i,j] == 255), None)
    #     if currMin != None:
    #         if currMin < getBiggest(minX): 
    #             addTo(minX, currMin)
    #             #minX = currMin
    #         if i > getSmallest(maxY):
    #             addTo(maxY, i)
    #             #maxY = i
    #         if i < getBiggest(minY):
    #             addTo(minY, i)
    #             #minY = i 
    #     currMax = next((j for j in range(width-1,0,-1) if th1[i,j] == 255), None)
    #     if currMax != None:
    #         if currMax > getSmallest(maxX): 
    #             addTo(maxX, currMax) 
    #             #maxX = currMax            
    #print(datetime.now() - start)
    start = datetime.now()
    for i in range(0, height, step):
        currMin = next((j for j in range(0,width,step) if th1[i,j] == 255), None)
        if currMin != None:
            if currMin < minX: 
                minX = currMin
            if i > maxY:
                maxY = i
            if i < minY:
                minY = i 
        currMax = next((j for j in range(width-1,0,-1 * step) if th1[i,j] == 255), None)
        if currMax != None:
            if currMax > maxX: 
                maxX = currMax           

    #print(maxX, minX, maxY, minY)

    # maxX = int(sum(maxX) / avgSize)
    # minX = int(sum(minX) / avgSize)
    # maxY = int(sum(maxY) / avgSize)
    # minY = int(sum(minY) / avgSize)

    print(maxX, minX, maxY, minY, (datetime.now() - start))


    cv2.rectangle(output, (minX, minY), (maxX, maxY), (255,0,0), 3)
    return output

if __name__ == "__main__":

    img = cv2.imread('Reference Images/10.png', -1)
    output = main(img, 1)
    cv2.imshow('step = 1', output)
    output2 = main(img, 11)
    cv2.imshow('step = 11', output2)
    output3 = main(img, 101)
    cv2.imshow('step = 101', output3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
