#Jesse Taylor
#16042846

import cv2
import numpy as np
from datetime import datetime
import glob

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

def main(img, step,verbose=False, boundVal=None):
    start = datetime.now()
    apples = 0
    output = img.copy()
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    height, width, depth = imgHSV.shape


    upper_blue = np.array([120, 255, 255])
    lower_blue = np.array([50, 80, 10])

    th1 = cv2.inRange(imgHSV, lower_blue, upper_blue)

    elementSize = 15 
    
    element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*elementSize+1,2*elementSize+1), (elementSize, elementSize))
    th1 = cv2.erode(th1, element)

    global maxX, maxY, minX, minY
    maxX = 0
    minX = width
    maxY = 0
    minY = height
    
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

    cv2.rectangle(output, (minX, minY), (maxX, maxY), (255,0,0), 3)

    imgHSV = imgHSV[(minY) : (maxY), (minX ) : (maxX)]
    thAreas = np.zeros((maxY - minY +step,maxX - minX+step,1), np.uint8)

    upper = np.array([90, 255, 255])
    lower = np.array([0, 60, 50])
    mask0 = cv2.inRange(imgHSV, lower, upper)

    upper = np.array([180, 255, 255])
    lower = np.array([150, 80, 80])
    mask1 = cv2.inRange(imgHSV, lower, upper)

    th1 = mask0 + mask1
    mask = th1

    contours, hierarchy = cv2.findContours(th1,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    hull = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area < 10000:
            hull.append(cv2.convexHull(contour))
    contours = np.append(contours, hull)
    cv2.drawContours(th1, contours, -1, (255), -1)
    contours, hierarchy = cv2.findContours(th1,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(th1, contours, -1, (255), -1)


    i = 0
    elementSize = 10
    element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*elementSize+1,2*elementSize+1), (elementSize, elementSize))
    while 255 in th1: 

        if verbose:
            thAreas = np.zeros((maxY-minY,maxX-minX,1), np.uint8)

        contours, hierarchy = cv2.findContours(th1,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for x in range(len(contours)):
            cnt = contours[x]
            area = cv2.contourArea(cnt)
            M = cv2.moments(cnt)
            if area > (400 - 50*i) and area < (10000 - i*500):
                if M['m00'] != 0:
                    cx = int(M['m10']/ M['m00'])
                    cy = int(M['m01']/ M['m00'])
                    if mask[cy,cx] == 255: 
                        cv2.circle(output, (cx+minX,cy+minY), 5,  white, 2)
                        cv2.circle(output, (cx+minX,cy+minY), 80 ,  white, 2)
                        cv2.drawContours(th1, contours, x , (0), -1)
                        apples += 1

        th1 = cv2.erode(th1, element)

        if verbose:
            cv2.imshow('thAreas', thAreas)
            cv2.imshow('th1', th1)
            cv2.imshow('output', output)
            cv2.waitKey(0)

        if i > 10:
            print('i > 10, breaking')
            break
        i += 1

    end = datetime.now() - start
    cv2.putText(output, str("Number of Apples: {}".format(apples)) ,(0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, red, thickness=2)
    #cv2.putText(output, str("{}".format(end)) ,(0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, red, thickness=2)
    return output, apples

if __name__ == "__main__":
    pth = 'data\\'
    extensions = ['*.png', '*.jpeg','*.jpg']
    for extension in extensions:
        for name in glob.glob(pth + extension):
            img = cv2.imread(name, cv2.IMREAD_COLOR)
            if img is None or not img.data:
                print("Error reading file", name)
                raise FileNotFoundError
            output, apples = main(img, 11, verbose=False)
            name = name.split('\\')[-1]
            imgName, extension = name.split('.')
            outStr = pth, imgName, "_Detected_Apples_", str(apples), ".",extension
            outStr = ''.join(outStr)
            cv2.imwrite(outStr, output)
    