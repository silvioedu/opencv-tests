import cv2
import numpy as np


def get_contours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            draw_identification(cnt)


def draw_identification(cnt):
    peri = cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
    x, y, w, h = cv2.boundingRect(approx)

    object_type = what_object(len(approx), w / float(h))
    cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(imgContour, object_type,
                (x + (w // 2) - 35, y + (h // 2) + 10), cv2.FONT_HERSHEY_COMPLEX, 0.6,
                (0, 0, 0), 2)


def what_object(obj_sides, ratio):
    if obj_sides == 3:
        object_type = 'Triangle'
    elif obj_sides > 4:
        object_type = 'Circle'
    else:
        if 0.90 <= ratio <= 1.05:
            object_type = 'Square'
        else:
            object_type = 'Rectangle'

    return object_type


RESOURCE_PATH = '../resources/'
FILENAME = 'shapes.png'

# --[Defining image]--#
img = cv2.imread(RESOURCE_PATH + FILENAME)
# img = cv2.resize(img, (350, 364))
imgContour = img.copy()

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
imgBlank = np.zeros_like(img)

get_contours(imgCanny)

# --[Showing image]--#
cv2.imshow('Original image', img)
# cv2.imshow('Gray image', imgGray)
# cv2.imshow('Blur image', imgBlur)
# cv2.imshow('Canny image', imgBlur)
cv2.imshow('Contour image', imgContour)

cv2.waitKey()
