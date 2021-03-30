import cv2

RESOURCE_PATH = '../resources/'
FILENAME = 'photo-small.jpg'
WINDOW_NAME = 'Showing image'

#--[Defining image]--#
img = cv2.imread(RESOURCE_PATH + FILENAME)

#--[Defining window position]--#
cv2.namedWindow(WINDOW_NAME)
cv2.moveWindow(WINDOW_NAME, 40,30)

#--[Showing image]--#
cv2.imshow(WINDOW_NAME, img)
cv2.waitKey()