import cv2

RESOURCE_PATH = '../resources/'
FILENAME = 'video-small.mp4'
WINDOW_NAME = 'Showing video'

#--[Defining image]--#
video = cv2.VideoCapture(RESOURCE_PATH + FILENAME)

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
