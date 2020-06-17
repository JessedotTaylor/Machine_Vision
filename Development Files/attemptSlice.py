import cv2
import numpy as np 
from datetime import datetime

img = cv2.imread('thAreasCross.png', cv2.IMREAD_GRAYSCALE)
height, width = img.shape
output = np.zeros((height,width), np.uint8)

lineLength = 100
jumpSize = 1

def multiCompare(in1, in2):
    return in1[0] == in2[0] and in1[1] == in2[1]

contours, heirarchy = cv2.findContours(img,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(output, contours, -1, (255), -1)

for i in contours:
    pointIndex = 0
    
    
    lenI = len(i)
    eyes = [list(i[x][0]) for x in range(lenI)]
    start = datetime.now()
    for point in eyes:
        S = next(((point[0], y) for y in range(point[1] + lineLength, point[1], -1) if (point[0], y) in eyes), None)
        print(point[0] in eyes)
        # cv2.line(output, tuple(point), (point[0], point[0] + lineLength), (255), 1)
        # cv2.imshow('output',output)
        # cv2.waitKey(0)
        # if S != None:
        #     cv2.line(output, tuple(point), S, (255), 1)
        #     cv2.imshow('output',output)
        #     cv2.waitKey(0)

    # while pointIndex < lenI:
    #     # point = i[pointIndex][0]
    #     # N = next(((point[0], y) for y in range(point[1] + lineLength, point[1] + 1, -1) if (point[0], y) in i), None)
    #     # if N != None:
    #     #     cv2.line(img, tuple(point), tuple(N), (0), 1)

    #     # E = next(((x, point[1]) for x in range(point[0] + lineLength, point[0] + 1, -1) if (x, point[1]) in i), None)
    #     # if E != None:
    #     #     cv2.line(img, tuple(point), tuple(E), (0), 1)

    #     # S = next(((point[0], y) for y in range(point[1] - 1, point[1] - lineLength, -1) if (point[0], y) in i), None)
    #     # if S != None:
    #     #     cv2.line(img, tuple(point), tuple(S), (0), 1)
        
    #     # W = next(((x, point[1]) for x in range(point[0] - 1, point[0] - lineLength, -1) if (x, point[1]) in i), None)
    #     # if W != None:
    #     #     cv2.line(img, tuple(point), tuple(W), (0), 1)

    #     point = i[pointIndex][0]
    #     N = next(((point[0], y) for y in range(point[1] - lineLength, point[1] - 1, 1) if (point[0], y) in eyes), None)
    #     #N = next(((point[0], y) for y in range(point[1] - 1, point[1] - lineLength, -1) if (point[1], y) in i), None)

    #     print(point[1] - lineLength, point[1] - 1)
    #     #print(point[1] - 1, point[1] - lineLength)
    #     print(point, N)
    #     if N != None:
    #         cv2.line(output, tuple(point), tuple(N), (255), 1)
    #         cv2.imshow('output',output)
    #         cv2.waitKey(0)
    #     # else:

    #     #     E = next(((x, point[1]) for x in range(point[0] + lineLength, point[0] + 1, -1) if (x, point[1]) in i), None)
    #     #     if E != None:
    #     #         cv2.line(output, tuple(point), tuple(E), (255), 1)
    #     #     else:
    #     #         S = next(((point[0], y) for y in range(point[1] + lineLength, point[1] + 1, -1) if (point[0], y) in i), None)
    #     #         if S != None:
    #     #             cv2.line(output, tuple(point), tuple(S), (255), 1)
        
    #     # W = next(((x, point[1]) for x in range(point[0] - 1, point[0] - lineLength, -1) if (x, point[1]) in i), None)
    #     # if W != None:
    #     #     cv2.line(output, tuple(point), tuple(W), (255), 1)
        
    #     pointIndex += jumpSize
    print(datetime.now() - start)
# (439, 161)
'''[439 161]]

 [[439 165]]

 [[438 166]]

 [[438 167]]

 [[437 168]]'''


cv2.imshow('output',output)
cv2.waitKey(0)
cv2.destroyAllWindows()
