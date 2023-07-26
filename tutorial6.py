# 灰階 高斯模糊 Canny dilate(膨脹) erode(侵蝕)
import cv2 as cv  
import numpy as np
img = cv.imread("data/jojo.jpg")
img = cv.resize(img,(0,0),fx=0.5,fy=0.5)
imgContour = img.copy() 

kernel = np.ones((5,5),np.uint8)
kernel1 = np.ones((5,5),np.uint8)


# Canny
canny = cv.Canny(img,50,100)
contours , hierarchy = cv.findContours(canny,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)

for  cnt in contours:
    cv.drawContours(imgContour,cnt,-1,(0,0,255),1)
    area = cv.contourArea(cnt)
    if area > 100:
        # print(cv.arcLength(cnt,True))
        peri = cv.arcLength(cnt,True)
        vertices = cv.approxPolyDP(cnt,peri * 0.02,True)
        corners = (len(vertices))
        print(corners)
        x,y,w,h = cv.boundingRect(vertices)
        cv.rectangle(imgContour,(x,y),(x+w,y+h),(0,0,255),2)
        if corners == 3:
            cv.putText(imgContour,'triangle',(x,y-5),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
        elif corners == 4:
            cv.putText(imgContour,'rectangle',(x,y-5),cv.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        elif corners == 5:
            cv.putText(imgContour,'pentagon',(x,y-5),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
        elif corners == 6:
            cv.putText(imgContour,'circle',(x,y-5),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2)



# 顯示圖片
cv.imshow("img",img)
cv.imshow("canny",canny)
cv.imshow('imgContour',imgContour)
cv.waitKey(0)