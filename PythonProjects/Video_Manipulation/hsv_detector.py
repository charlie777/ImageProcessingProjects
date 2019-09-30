#Colours

import numpy as np
import cv2

def nothing(x) :
	pass

cap = cv2.VideoCapture(0)

#hsv = cv2.cvtColor(frame,cv2.COLOR_GRAY2HSV)

cv2.namedWindow("image",cv2.WINDOW_NORMAL)

cv2.createTrackbar('Hue low','image',0,179,nothing)
cv2.createTrackbar('Sat low','image',0,255,nothing)
cv2.createTrackbar('Val low','image',0,255,nothing)
cv2.createTrackbar('Hue high','image',0,179,nothing)
cv2.createTrackbar('Sat high','image',0,255,nothing)
cv2.createTrackbar('Val high','image',0,255,nothing)

'''
while(1) :
	ret, frame = cap.read()
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

	hl = cv2.getTrackbarPos('Hue low','image')
	sl = cv2.getTrackbarPos('Sat low','image')
	vl = cv2.getTrackbarPos('Val low','image')
	hh = cv2.getTrackbarPos('Hue high','image')
	sh = cv2.getTrackbarPos('Sat high','image')
	vh = cv2.getTrackbarPos('Val high','image')
	
	ran = cv2.inRange(hsv,(hl,sl,vl),(hh,sh,vh))
	
	cv2.imshow("image",ran)

	if cv2.waitKey(1) == 27 :
		break
'''

img = cv2.imread("D:/Programming/Python/Project5/devnagri-test.jpg", cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE)
while True :
	hl = cv2.getTrackbarPos('Hue low', 'image')
	sl = cv2.getTrackbarPos('Sat low', 'image')
	vl = cv2.getTrackbarPos('Val low', 'image')
	hh = cv2.getTrackbarPos('Hue high', 'image')
	sh = cv2.getTrackbarPos('Sat high', 'image')
	vh = cv2.getTrackbarPos('Val high', 'image')

	ran = cv2.inRange(hsv, (hl, sl, vl), (hh, sh, vh))
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
	opening0 = cv2.morphologyEx(ran, cv2.MORPH_OPEN, kernel)
	closing0 = cv2.morphologyEx(opening0, cv2.MORPH_CLOSE, kernel)
	opening = cv2.morphologyEx(closing0, cv2.MORPH_OPEN, kernel)
	closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
	thresh = closing

	cv2.imshow("image", thresh)
	if cv2.waitKey(1) == 27 :
		break

cv2.destroyAllWindows()

print ("hl = {}".format(hl))
print ("hh = {}".format(hh))
print ("sl = {}".format(sl))
print ("sh = {}".format(sh))
print ("vl = {}".format(vl))
print ("vh = {}".format(vh))
