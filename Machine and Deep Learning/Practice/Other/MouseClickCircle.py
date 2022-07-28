import cv2
import numpy as np

def drawCircle(event, x, y, flags, params):
    if(event == cv2.EVENT_LBUTTONDBLCLK):
        cv2.circle(img, (x,y), 20, (255,0,0), 2)
        
img = np.zeros((500,500,3))
# img[:] = [255, 255, 255]

cv2.namedWindow("image")
cv2.setMouseCallback("image",drawCircle)
while(1):
    cv2.imshow("image",img)
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()