import cv2
img = cv2.imread('fantom.jpg')
print("img.shape=",img.shape)
cv2.imwrite('read_write.jpg', img)