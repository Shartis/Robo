import cv2 as cv
import numpy as np

image = cv.imread('Image.jpg')  # reading image from directory


#  function for circle drawing
def draw_circle(event, x, y, flags, param):
    global mouse_x, mouse_y, print_status, Step
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(image, (x, y), 3, (255, 255, 0), -1)
        mouse_x, mouse_y = x, y
        Step += 1
        print_status = True


global Step
Step = 0
Flag = 0
cv.imshow("img_warp", image)
cv.setMouseCallback('img_warp', draw_circle)

global print_status
print_status = False

while True:
    cv.imshow('img_warp', image)
    k = cv.waitKey(20) & 0xFF
    if Step == 4 and Flag == 1:
        break
    if Step == 1:
        x1 = mouse_x, mouse_y
        if print_status:
            print_status = False
    if Step == 2:
        x2 = mouse_x, mouse_y
        if print_status:
            print_status = False
    if Step == 3:
        x3 = mouse_x, mouse_y
        if print_status:
            print_status = False
    if Step == 4:
        x4 = mouse_x, mouse_y
        if print_status:
            print_status = False
        Flag = 1


pts1 = np.float32([[x1], [x2], [x3], [x4]])
pts2 = np.float32([[0, 0], [500, 0], [0, 500], [500, 500]])
matrix = cv.getPerspectiveTransform(pts1, pts2)
image_output = cv.warpPerspective(image, matrix, (500, 500))

cv.imshow('image_output', image_output)
cv.waitKey(0)
