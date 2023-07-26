import cv2 as cv  
import numpy as np

def empty(y):
    pass
# img = cv.imread("data/jojo.jpg")
# img = cv.resize(img,(0,0),fx=0.5,fy=0.5)

cv.namedWindow('TrackBar')
cv.resizeWindow('TrackBar',640,320)

cv.createTrackbar('Hue Min','TrackBar',0,179,empty)
cv.createTrackbar('Hue Max','TrackBar',179,179,empty)
cv.createTrackbar('Sat Min','TrackBar',0,255,empty)
cv.createTrackbar('Sat Max','TrackBar',255,255,empty)
cv.createTrackbar('Val Min','TrackBar',0,255,empty)
cv.createTrackbar('Val Max','TrackBar',255,255,empty)

# hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cap = cv.VideoCapture(0)
while True:
    h_min = cv.getTrackbarPos('Hue Min','TrackBar')
    h_max = cv.getTrackbarPos('Hue Max','TrackBar')
    s_min = cv.getTrackbarPos('Sat Min','TrackBar')
    s_max = cv.getTrackbarPos('Sat Max','TrackBar')
    v_min = cv.getTrackbarPos('Val Min','TrackBar')
    v_max = cv.getTrackbarPos('Val Max','TrackBar')
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    
    ret, img = cap.read()
    hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])

    # mask = cv.inRange(hsv,lower,upper)
    # result = cv.bitwise_and(img,img,mask=mask)
    mask = cv.inRange(hsv,lower,upper)
    result = cv.bitwise_and(img,img,mask=mask)

    cv.imshow("img",img)
    # cv.imshow("hsv",hsv)
    cv.imshow("mask",mask)
    cv.imshow("result",result)
    cv.waitKey(1)