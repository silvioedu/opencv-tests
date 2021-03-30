import cv2
import numpy as np

RESOURCE_PATH = '../resources/'
FILENAME = 'photo-small.jpg'

#--[Defining image]--#
img = cv2.imread(RESOURCE_PATH + FILENAME)
img1 = cv2.resize(img, (300, 200))

#--[Joining images]--#
imgHorizontal = np.hstack((img1, img1))
imgVertical = np.vstack((img1, img1))

#--[Showing image]--#
cv2.imshow('Horizontal image', imgHorizontal)
cv2.imshow('Vertical image', imgVertical)
cv2.waitKey()