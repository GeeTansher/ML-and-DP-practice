import cv2
img = cv2.imread('Machine and Deep Learning/Practice/images/1.jpg')

img = img[0:150,:]
print(img.shape)
cv2.imshow("img",img)
cv2.waitKey()
