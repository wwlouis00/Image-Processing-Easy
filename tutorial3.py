# 灰階 高斯模糊 Canny dilate(膨脹) erode(侵蝕)
import cv2 as cv  
import numpy as np
img = cv.imread("data/jojo.jpg")

kernel = np.ones((5,5),np.uint8)
kernel1 = np.ones((5,5),np.uint8)

# 灰階
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# 高斯模糊
blur = cv.GaussianBlur(img,(15,15),10)
# Canny
canny = cv.Canny(img,50,100)

# dilate膨脹
dilate = cv.dilate(canny,kernel,iterations=1)
# erode侵蝕
erode = cv.erode(dilate,kernel1,iterations=1)

# 顯示圖片
cv.imshow("img",img)
cv.imshow("gray",gray)
cv.imshow("blur",blur)
cv.imshow("canny",canny)
cv.imshow("dilate",dilate)
cv.imshow("erode",erode)
cv.waitKey(0)