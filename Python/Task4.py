import random
import cv2


def add_noise(img):

   row, col = img.shape
   number_of_pixels = random.randint(300, 10000)
   for i in range(number_of_pixels):

       y_coord = random.randint(0, row - 1)
       x_coord = random.randint(0, col - 1)
       img[y_coord][x_coord] = 255

   number_of_pixels = random.randint(300, 10000)
   for i in range(number_of_pixels):

       y_coord = random.randint(0, row - 1)
       x_coord = random.randint(0, col - 1)
       img[y_coord][x_coord] = 0

   return img

img = cv2.imread('Image.jpg', cv2.IMREAD_GRAYSCALE)


cv2.imwrite('salt-and-pepper-example.jpg', add_noise(img))


img2 = cv2.imread('salt-and-pepper-example.jpg')

median = -cv2.medianBlur(src = img2, ksize=5)

cv2.imwrite('median.jpg',median)

gaussian_blur = cv2.GaussianBlur(src=img2, ksize=(5,5), sigmaX = 0, sigmaY=0)

cv2.imwrite('gaussian.jpg',gaussian_blur)

bilateral_filter = cv2.bilateralFilter(src=img2, d=9, sigmaColor=75, sigmaSpace=75)

cv2.imwrite('bilateral.jpg',bilateral_filter)
