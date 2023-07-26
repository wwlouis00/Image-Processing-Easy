import numpy as np
import cv2 as cv
import random

img = cv.imread("data/jojo.jpg")
for row in range(300):
    for col in range(img.shape[1]):
        # img[row][col] = [255,0,0] # blue
        img[row][col] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

## 分割圖片
newimg = img[:150,200:400]

## 圖片顯示
cv.imshow('img',img)
cv.imshow('newimg',newimg)
cv.waitKey(0)
# if ord('q'):
#     break