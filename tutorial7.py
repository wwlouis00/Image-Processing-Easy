# 灰階 高斯模糊 Canny dilate(膨脹) erode(侵蝕)
import cv2 as cv  
import numpy as np
img = cv.imread("data/jojo.jpg")
img = cv.resize(img,(0,0),fx=0.5,fy=0.5)

faceCascade = cv.CascadeClassifier('face_detect.xml')
faceRect = faceCascade.detectMultiScale(img,1.1,7)
print(len(faceRect))

for (x,y,w,h) in faceRect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    cv.putText(img,'HumanFace',(x,y-10),cv.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2)

# 顯示圖片
cv.imshow("img",img)
cv.waitKey(0)