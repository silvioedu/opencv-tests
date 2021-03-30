import cv2
import numpy as np

WINDOW_NAME = 'Image'

# 0 -> black
# 1 -> white
img = np.zeros((512, 512, 3), np.uint8) # black image
# img [:] = 255, 0, 0 # blue image
# img[200:300, 100:300] = 255, 0, 0 # blue rectangle in black window

#--[Drawing on image]--#
cv2.line(img, (0,0), (img.shape[0], img.shape[1]), (0, 255, 0), 2)
cv2.rectangle(img, (0,0), (250, 350), (0, 0, 255), cv2.FILLED)
cv2.circle(img, (400, 50), 30, (255,255,0), 5)
cv2.putText(img, 'OpenCV Tests', (280, 200), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 150, 0), 2)

#--[Showing image]--#
cv2.imshow(WINDOW_NAME, img)
cv2.waitKey()