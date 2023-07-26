# 灰階 高斯模糊 Canny dilate(膨脹) erode(侵蝕)
import cv2 as cv  
import numpy as np

img = np.zeros((600,600,3),np.uint8)
# 畫綠線
cv.line(img,(0,0),(img.shape[1],img.shape[0]),(70,215,90),2)

# 畫方形 
cv.rectangle(img,(0,0),(400,300),(30,70,155),cv.FILLED)

# 畫圓形
cv.circle(img,(300,400),30,(255,71,80),cv.FILLED)

# 寫字(不支援中文)
cv.putText(img,'LOUIS WANG',(100,500),cv.FONT_HERSHEY_SIMPLEX,2,(255,255,255),3)

# 顯示圖片
cv.imshow("img",img)

cv.waitKey(0)