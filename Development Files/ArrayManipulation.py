import cv2
import numpy as np

height = 720
width = 1280
depth = 1
step = 11
# img = np.zeros((height, width, depth), np.uint8)
# a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
# row1 = a[0, :]
# col1 = a[:, 0]
# a[1, 2] = 77
# print(a)

# row1 = img[0, :]
# col1 = img[:, 0]
# colC = len(col1)
# rowC = len(row1)

# for i in range(0, width , step):
#     cv2.line(img, (i,0), (i, height), (255), 1)

# for j in range(0, height , step):
#     cv2.line(img, (0, j), (width, j), (255), 1)

def scanLines(height, width, depth, step):
    img = np.zeros((height, width, depth), np.uint8)
    for i in range(0, width , step):
        cv2.line(img, (i,0), (i, height), (255), 1)

    for j in range(0, height , step):
        cv2.line(img, (0, j), (width, j), (255), 1)
    return img

#print(colC/3)
# for i in range(colC):
#     for j in range(rowC):
#         img[i,j] = [0,0,0] # [b,g,r]

# for i in range(0,int(colC / 3)):
#     img[i] = [[255,0,0]]* rowC
#     #for j in range(rowC):
#     #    img[i,j] = [255,0,0] # [b,g,r]

# for i in range(int(colC/3), int((colC / 3)*2)):
#     for j in range(rowC):
#         img[i,j] = [0,255,0] # [b,g,r]

# for i in range(int((colC / 3)*2), colC):
#     for j in range(rowC):
#         img[i,j] = [0,0,255] # [b,g,r]


# for y in range(colC):
#     for x in a[y, :]:

# for y in col1:
#     for x in img[:, y]:
#         print(a[x,y])
#print(col1)
# for y in img.rows:
#     for x in img.cols:
#         if (i > j):
#             img[]


# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

if __name__ == "__main__":
    height = 720
    width = 1280
    depth = 1

    output1 = scanLines(height, width, depth, 1)
    cv2.imshow('step=1', output1)
    output2 = scanLines(height, width, depth, 11)
    cv2.imshow('step=11', output2)
    output3 = scanLines(height, width, depth, 101)
    cv2.imshow('step=101', output3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

