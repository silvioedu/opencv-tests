import cv2

RESOURCE_PATH = '../resources/'
FILENAME = 'photo-small.jpg'

#--[Defining image]--#
img = cv2.imread(RESOURCE_PATH + FILENAME)
print(f'Original Image Shape: {img.shape}')

#--[Resizing]--#
imgResize = cv2.resize(img, (300, 200))
print(f'Resize Image Shape: {imgResize.shape}')

#--[Cropping]--#
imgCrop = img[10:200, 150:450]

#--[Showing image]--#
cv2.imshow('Original image', img)
cv2.imshow('Resize image', imgResize)
cv2.imshow('Crop image', imgCrop)

cv2.waitKey()