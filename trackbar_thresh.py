import cv2

def nothing(x):
    pass

gray = cv2.imread('fantom.jpg', cv2.IMREAD_GRAYSCALE)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.createTrackbar('thresh', 'image', 0, 255, nothing)
cv2.createTrackbar('type', 'image', 0, 4, nothing)

while True:
    thresh_num = cv2.getTrackbarPos('thresh', 'image')
    thresh_type = cv2.getTrackbarPos('type', 'image')
    ret, img = cv2.threshold(gray, thresh_num, 255, thresh_type)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break
    cv2.imshow('image', img)
cv2.destroyAllWindows()