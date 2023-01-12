import cv2
import numpy as np

# Read image
img = cv2.imread(r'D:\ML-and-DP-practice\Machine and Deep Learning\Practice\ImageToWaterPaint\scene.jpgq')

# Resize image
img_resize = cv2.resize(img,None,fx=1,fy=1)

# Removing impurities
for i in range(2):
    img_clear = cv2.medianBlur(img_resize,3)
    
# It will constant the color variation in th image, blend with neighbors
img_clear = cv2.edgePreservingFilter(img_clear, sigma_s=4)

# Bilateral Filtering
img_filter = cv2.bilateralFilter(img_clear,3,10,10)

for i in range(2):
    img_filter = cv2.bilateralFilter(img_filter,3,20,20)
    
for i in range(2):
    img_filter = cv2.bilateralFilter(img_filter,5,30,30)
    
# for i in range(3):
#     img_filter = cv2.bilateralFilter(img_filter,3,40,5)
    
# for i in range(3):
#     img_filter = cv2.bilateralFilter(img_filter,5,40,10)

# Sharpen the image
gaussian_mask = cv2.GaussianBlur(img_filter,(9,9),2)
img_sharp = cv2.addWeighted(img_filter, 1.5, gaussian_mask, -0.5, 0)
img_sharp = cv2.addWeighted(img_sharp, 1.4, gaussian_mask, -0.4, 10)
img_sharp = cv2.addWeighted(img_sharp, 1.3, gaussian_mask, -0.3, 4)

cv2.imshow("img",img)
# cv2.imshow("clear",img_clear)
# cv2.imshow("filter",img_filter)
cv2.imshow("sharp",img_sharp)
cv2.waitKey()
cv2.destroyAllWindows()