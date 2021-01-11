import cv2

image = cv2.imread('wami.jpg')
try:
    resize = cv2.resize(image, (64,64))
except cv2.error as e:
    print('Invalid frame!')
cv2.waitKey()