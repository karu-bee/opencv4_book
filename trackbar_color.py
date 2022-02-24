import cv2
import numpy as np

def nothing(x):
    pass

img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)

cv2.createTrackbar('Blue', 'image', 0, 255, nothing)
cv2.createTrackbar('Green', 'image', 0, 255, nothing)
cv2.createTrackbar('Red', 'image', 0, 255, nothing)

cv2.createTrackbar('Hue', 'image', 0, 179, nothing)
cv2.createTrackbar('Saturation', 'image', 0, 255, nothing)
cv2.createTrackbar('Value', 'image', 0, 255, nothing)

cv2.createTrackbar('switch', 'image', 0, 1, nothing)

while True:
    switch = cv2.getTrackbarPos('switch', 'image')

    if switch == 1:
        b = cv2.getTrackbarPos('Blue', 'image')
        g = cv2.getTrackbarPos('Green', 'image')
        r = cv2.getTrackbarPos('Red', 'image')
        img[:] = [b, g, r]
    else:
        h = cv2.getTrackbarPos('Hue', 'image')
        s = cv2.getTrackbarPos('Saturation', 'image')
        v = cv2.getTrackbarPos('Value', 'image')
        img[:] = [h,s,v]
        img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('c'):
        if switch == 1:
            value = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            print(value[0,0])
        else:
            print(img[0,0])
    elif k == ord('q'):
        break
    cv2.imshow('image', img)
cv2.destroyAllWindows()