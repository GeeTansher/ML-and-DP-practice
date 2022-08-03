import cv2
import numpy as np

def setValue(x):
    pass

cv2.namedWindow("Color Detector")
cv2.createTrackbar("Upper Hue", "Color Detector", 150, 180, setValue)
cv2.createTrackbar("Upper Saturation", "Color Detector", 255, 255, setValue)
cv2.createTrackbar("Upper Value", "Color Detector", 255, 255, setValue)
cv2.createTrackbar("Lower Hue", "Color Detector", 64, 180, setValue)
cv2.createTrackbar("Lower Saturation", "Color Detector", 72, 255, setValue)
cv2.createTrackbar("Lower Value", "Color Detector", 49, 255, setValue)

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    
    while(cap.isOpened()):
        ret, frame = cap.read()
        frame = cv2.resize(frame, None, fx=0.8, fy=0.8, interpolation=cv2.INTER_AREA)
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        uh = cv2.getTrackbarPos("Upper Hue", "Color Detector")
        us = cv2.getTrackbarPos("Upper Saturation", "Color Detector")
        uv = cv2.getTrackbarPos("Upper Value", "Color Detector")
        lh = cv2.getTrackbarPos("Lower Hue", "Color Detector")
        ls = cv2.getTrackbarPos("Lower Saturation", "Color Detector")
        lv = cv2.getTrackbarPos("Lower Value", "Color Detector")
        
        upperHSV = np.array([uh,us,uv])
        lowerHSV = np.array([lh,ls,lv])
        
        mask = cv2.inRange(hsv, lowerHSV, upperHSV)
        
        result = cv2.bitwise_and(frame, frame, mask=mask)
        result = cv2.medianBlur(result, 3)
        
        cv2.imshow("Image", result)
        # cv2.imshow('mask',mask)
        k=cv2.waitKey(1)
        if k==27:
            break
        
    cv2.destroyAllWindows()
    cap.release()
        