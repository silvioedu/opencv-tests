import cv2

RESOURCE_PATH = '../resources/'
FILENAME = 'photo-small.jpg'
CONFIG_CASCADE = 'haarcascade_frontalface_default.xml'

face_cascade = cv2.CascadeClassifier(RESOURCE_PATH + CONFIG_CASCADE)

#--[Defining image]--#
img = cv2.imread(RESOURCE_PATH + FILENAME)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(imgGray, 1.1, 4)

for x,y,w,h in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
#--[Showing image]--#
cv2.imshow('Result', img)
cv2.waitKey()