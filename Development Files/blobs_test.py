import cv2
import numpy as np 

#img = cv2.imread('Reference Images/0.png', cv2.IMREAD_GRAYSCALE)
img = cv2.imread('contourFill.png', cv2.IMREAD_GRAYSCALE)
#img = ~ img

_, th1 = cv2.threshold(img,175,255,cv2.THRESH_BINARY)
cv2.imshow("imageThreshold", th1)

detector = cv2.SimpleBlobDetector_create()


keypoints = detector.detect(th1)

img_with_keyPoints = cv2.drawKeypoints(img, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("Keypoints", img_with_keyPoints)
cv2.waitKey(0)
cv2.destroyAllWindows()