import cv2
import numpy as np

def empty(a):
    ...

RESOURCE_PATH = '../resources/'
FILENAME = 'photo-car-small.jpg'

#--[Creating a track bar]--#
TRACK_BAR = 'TrackBars'
HUE_MIN, HUE_MAX = 'Hue Min', 'Hue Max'
SAT_MIN, SAT_MAX = 'Sat Min', 'Sat Max'
VAL_MIN, VAL_MAX = 'Val Min', 'Val Max'

cv2.namedWindow(TRACK_BAR)
cv2.resizeWindow(TRACK_BAR, 640, 240)
cv2.createTrackbar(HUE_MIN, TRACK_BAR,  68, 179, empty)
cv2.createTrackbar(HUE_MAX, TRACK_BAR, 110, 179, empty)
cv2.createTrackbar(SAT_MIN, TRACK_BAR,  56, 255, empty)
cv2.createTrackbar(SAT_MAX, TRACK_BAR, 255, 255, empty)
cv2.createTrackbar(VAL_MIN, TRACK_BAR, 133, 255, empty)
cv2.createTrackbar(VAL_MAX, TRACK_BAR, 255, 255, empty)

while True:
    #--[Defining image]--#
    img = cv2.imread(RESOURCE_PATH + FILENAME)

    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hue_min = cv2.getTrackbarPos(HUE_MIN, TRACK_BAR)
    hue_max = cv2.getTrackbarPos(HUE_MAX, TRACK_BAR)
    sat_min = cv2.getTrackbarPos(SAT_MIN, TRACK_BAR)
    sat_max = cv2.getTrackbarPos(SAT_MAX, TRACK_BAR)
    val_min = cv2.getTrackbarPos(VAL_MIN, TRACK_BAR)
    val_max = cv2.getTrackbarPos(VAL_MAX, TRACK_BAR)
    #print(hue_min, hue_max, sat_min, sat_max, val_min, val_max)

    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])
    mask = cv2.inRange(imgHSV, lower, upper)

    imgResult = cv2.bitwise_and(img, img, mask=mask)

    #--[Showing image]--#
    cv2.imshow('Original image', img)
    cv2.imshow('HSV image', imgHSV)
    cv2.imshow('Mask image', mask)
    cv2.imshow('Result image', imgResult)

    cv2.waitKey(1)