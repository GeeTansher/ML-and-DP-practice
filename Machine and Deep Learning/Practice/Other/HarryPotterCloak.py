import cv2
import numpy as np

# color_dict_HSV = {'black': [[180, 255, 30], [0, 0, 0]],
#               'white': [[180, 18, 255], [0, 0, 231]],
#               'red1': [[180, 255, 255], [159, 50, 70]],
#               'red2': [[9, 255, 255], [0, 50, 70]],
#               'green': [[89, 255, 255], [36, 50, 70]],
#               'blue': [[128, 255, 255], [90, 50, 70]],
#               'yellow': [[35, 255, 255], [25, 50, 70]],
#               'purple': [[158, 255, 255], [129, 50, 70]],
#               'orange': [[24, 255, 255], [10, 50, 70]],
#               'gray': [[180, 18, 230], [0, 0, 40]]}

def setValue(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow("Color Detector")
cv2.createTrackbar("Upper Hue", "Color Detector", 158, 180, setValue)
cv2.createTrackbar("Upper Saturation", "Color Detector", 255, 255, setValue)
cv2.createTrackbar("Upper Value", "Color Detector", 255, 255, setValue)
cv2.createTrackbar("Lower Hue", "Color Detector", 129, 180, setValue)
cv2.createTrackbar("Lower Saturation", "Color Detector", 50, 255, setValue)
cv2.createTrackbar("Lower Value", "Color Detector", 70, 255, setValue)

init_frame = None
def takeInitFrame():
    global init_frame
    while(True):
        cv2.waitKey(1000)
        ret, init_frame = cap.read()
        if ret:
            break
    

takeInitFrame()
# init_frame = cv2.imread("D:/ML-and-DP-practice/Machine and Deep Learning/Practice/images/flower.jpg")
# init_frame = cv2.resize(init_frame,(640,480))
# print(init_frame.shape)

while(True):
    ret, frame = cap.read()
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    uh = cv2.getTrackbarPos("Upper Hue", "Color Detector")
    us = cv2.getTrackbarPos("Upper Saturation", "Color Detector")
    uv = cv2.getTrackbarPos("Upper Value", "Color Detector")
    lh = cv2.getTrackbarPos("Lower Hue", "Color Detector")
    ls = cv2.getTrackbarPos("Lower Saturation", "Color Detector")
    lv = cv2.getTrackbarPos("Lower Value", "Color Detector")
    
    upperHSV = np.array([uh,us,uv])
    lowerHSV = np.array([lh,ls,lv])
    
    kernel = np.ones((3,3),np.uint8)
    
    mask = cv2.inRange(hsv, lowerHSV, upperHSV)
    mask = cv2.medianBlur(mask, 3)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask_inv = 255-mask
    
    b = frame[:,:,0]
    g = frame[:,:,1]
    r = frame[:,:,2]
    b = cv2.bitwise_and(b,mask_inv)
    g = cv2.bitwise_and(g,mask_inv)
    r = cv2.bitwise_and(r,mask_inv)
    backFrame = cv2.merge((b,g,r))
    
    b = init_frame[:,:,0]
    g = init_frame[:,:,1]
    r = init_frame[:,:,2]
    b = cv2.bitwise_and(b,mask)
    g = cv2.bitwise_and(g,mask)
    r = cv2.bitwise_and(r,mask)
    blanketFrame = cv2.merge((b,g,r))
    
    fullFrame = cv2.bitwise_or(backFrame, blanketFrame)
    
    cv2.imshow("Final",fullFrame)
    # cv2.imshow("mask",mask)
    
    if(cv2.waitKey(3)==27):
        break
    elif(cv2.waitKey(3)==ord('n')):
        takeInitFrame()
    
cap.release()
cv2.destroyAllWindows()
