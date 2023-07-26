# 開啟相機
import cv2 as cv  

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret:
        frame = cv.resize(frame,(0,0),fx=1.2,fy=1.2)
        cv.imshow('vidoe',frame)
    else:
        break
    if cv.waitKey(10) == ord('q'):
        break