import cv2
import numpy as np

RESOURCE_PATH = '../resources/'
FILENAME = 'photo-cards-small.jpg'

#--[Defining image]--#
img = cv2.imread(RESOURCE_PATH + FILENAME)

#--[Defining parameters do cut de image]--#
width, height = 250, 350
pts1 = np.float32([[295,73],[500,205],[78,325],[285,495]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgWarp = cv2.warpPerspective(img, matrix, (width, height))


#--[Showing image]--#
cv2.imshow('Original image', img)
cv2.imshow('Warp image', imgWarp)
cv2.waitKey()