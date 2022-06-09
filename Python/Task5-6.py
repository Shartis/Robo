import cv2 as cv
import numpy as np

def nothing(x):
    pass

def salt_pepper_noise(input_image, probability):

    output_noise_img = input_image.copy()
    if len(input_image.shape) == 2:
        black = 0
        white = 255
    else:
        colorspace = input_image.shape[2]
        if colorspace == 3:
            black = np.array([0, 0, 0])
            white = np.array([255, 255, 255])
        else:
            black = np.array([0, 0, 0, 255])
            white = np.array([255, 255, 255, 255])
    probs = np.random.random(output_noise_img.shape[:2])
    output_noise_img[probs < (probability / 2)] = black
    output_noise_img[probs > 1 - (probability / 2)] = white
    return output_noise_img

source_image = cv.imread('image3.jpg')

scale_percent = 25

width = int(source_image.shape[1]  / 2)
height = int(source_image.shape[0]  / 2)
dim = (width, height)

image = cv.resize(source_image, dim, interpolation=cv.INTER_AREA)

prob = 0
last_prob = 1

ddepth = cv.CV_16S
scale = 1
delta = 0

cv.namedWindow('source_image')
cv.createTrackbar('Prob', 'source_image', 0, 90, nothing)

while True:
    prob = cv.getTrackbarPos('Prob', 'source_image')

    k = cv.waitKey(1)

    if prob != last_prob:
        cv.imshow('source_image', image)
        noise_image = salt_pepper_noise(image, float(prob) / 100)
        gray_noise = cv.cvtColor(noise_image, cv.COLOR_BGR2GRAY)

        img_blur = cv.medianBlur(gray_noise, ksize=15)

        laplacian_filter = cv.Laplacian(img_blur, ddepth, ksize=5)
        laplacian_filter = cv.convertScaleAbs(laplacian_filter)

        sobel_x = cv.Sobel(img_blur, ddepth, dx=1, dy=0, ksize=5, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
        sobel_x = cv.convertScaleAbs(sobel_x)

        sobel_y = cv.Sobel(img_blur, ddepth, dx=0, dy=1, ksize=5, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
        sobel_y = cv.convertScaleAbs(sobel_y)

        sobel_xy = cv.Sobel(img_blur, ddepth, dx=1, dy=1, ksize=5, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
        sobel_xy = cv.convertScaleAbs(sobel_xy)

        sobel_x_canny = cv.Canny(image=sobel_x, threshold1=100, threshold2=200)
        sobel_y_canny = cv.Canny(image=sobel_y, threshold1=100, threshold2=200)
        sobel_xy_canny = cv.Canny(image=sobel_xy, threshold1=100, threshold2=200)

        scharr_x = cv.Scharr(img_blur, ddepth, dx=1, dy=0, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
        scharr_x = cv.convertScaleAbs(scharr_x)

        scharr_y = cv.Scharr(img_blur, ddepth, dx=0, dy=1, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
        scharr_y = cv.convertScaleAbs(scharr_y)

        cv.imshow('noise_image', noise_image)

        cv.imshow('sobel_x_canny', sobel_x_canny)
        cv.imshow('sobel_y_canny', sobel_y_canny)
        cv.imshow('sobel_xy_canny', sobel_xy_canny)

    last_prob = prob

    if k == ord('q'):
        cv.destroyAllWindows()
        break