import cv2
import numpy as np
img = np.zeros((500,500))
img[:,:] = 100
cv2.line(img,(100,100),(200,200),(255,0,0),2,cv2.LINE_AA)
cv2.imshow("img",img)
cv2.waitKey()
cv2.destroyAllWindows()
