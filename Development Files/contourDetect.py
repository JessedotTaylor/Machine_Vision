import cv2
import numpy as np

height = 640
width = 480

img = np.ones((height,width,3), np.uint8) #Setting image to colour by setting 3D array
img = np.full((height, width, 3), (0,0,0), np.uint8) # Equivalent to above, but can set colour
cv2.circle(img, (int(width /2), int(height /2)),50, (128,0,0), -1)
cv2.imshow('image', img)
cv2.waitKey(0)

imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

th1 = cv2.inRange(imgHSV, (115,0,0),(125,255,255))
contours, hierarchy = cv2.findContours(th1,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print(len(contours))
for x in range(len(contours)):
    cv2.drawContours(img, contours, x, (0,0,255), 2, 8, hierarchy)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()