import cv2
from cv2 import CAP_PROP_FRAME_WIDTH, CAP_PROP_FRAME_HEIGHT

WINDOW_NAME = 'Video'
CAM_NUMBER = 0

#--[Defining image]--#
video = cv2.VideoCapture(CAM_NUMBER)

#--[https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html#ggaeb8dd9c89c10a5c63c139bf7c4f5704da6223452891755166a4fd5173ea257068]--#
video.set(CAP_PROP_FRAME_WIDTH, 640)
video.set(CAP_PROP_FRAME_HEIGHT, 480)

#--[Defining window position]--#
cv2.namedWindow(WINDOW_NAME)
cv2.moveWindow(WINDOW_NAME, 40,30)

#--[Showing video]--#
while True:
    success, img = video.read()
    cv2.imshow(WINDOW_NAME, img)

    #--[Close window when press 'q']--#
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


