import cv2
import numpy as np

RESOURCE_PATH = '../resources/'
FILENAME = 'photo-small.jpg'


#--[Defining image]--#
imgOriginal = cv2.imread(RESOURCE_PATH + FILENAME)
imgGray = cv2.cvtColor(imgOriginal, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
imgCanny = cv2.Canny(imgOriginal, 80, 80)
imgDilate = cv2.dilate(imgCanny, np.ones((5,5), np.uint8), iterations=1)
imgErode = cv2.erode(imgDilate, np.ones((5,5), np.uint8), iterations=1)

#--[Showing images]--#
cv2.imshow('Original image', imgOriginal)
cv2.imshow('Gray image', imgGray)
cv2.imshow('Blur image', imgBlur)
cv2.imshow('Canny image', imgCanny)
cv2.imshow('Dilate image', imgDilate)
cv2.imshow('Erode image', imgErode)

cv2.waitKey()