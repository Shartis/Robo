import cv2 as cv
import math

route = []
isDrawing = True
map_ratio = 1.478
route_length = 0.0


def calculate_distance(a, b):
   return math.sqrt(((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2))


def mouse_click_event(event, x, y, flags, param):
   global route, route_length

   if event == cv.EVENT_LBUTTONDOWN and isDrawing:
       cv.circle(map_, (x, y), 3, (0, 0, 255), -1)
       route.append((x, y))

       if route:
           cv.line(map_, route[len(route) - 1], route[len(route) - 2], (255, 221, 28), 2)
           route_length += calculate_distance(route[len(route) - 1], route[len(route) - 2])


map_ = cv.imread('Map.jpg')

cv.imshow('map', map_)
cv.setMouseCallback('map', mouse_click_event)

while True:
   cv.imshow('map', map_)

   key = cv.waitKey(1)

   if cv.waitKey(1) == 27 and isDrawing:
       isDrawing = False
       print("Length = ", str(int(route_length * map_ratio)), " m")

       cv.destroyAllWindows()
       break
