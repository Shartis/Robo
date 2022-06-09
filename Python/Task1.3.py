import cv2 as cv2

import time


Capture = cv2.VideoCapture(0)

out = cv2.VideoWriter('video.mp4', cv2.VideoWriter_fourcc(*'XVID'), 30.0, (640,480))

i = 0
while True:
	ret, frame = Capture.read()
	out.write(frame)
	time.sleep(0.05)
	i = i + 1
	if i > 50:
		break

Capture.release()


cv2.destroyAllWindows()