import cv2
import numpy as np

def frameDiff(prev, curr, nextF):
    diff1 = cv2.absdiff(prev, curr)
    diff2 = cv2.absdiff(curr, nextF)
    return cv2.bitwise_and(diff1, diff2)

def getFrame(cap, scale = 0.8):
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
    return cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    prevFrame = getFrame(cap)
    currFrame = getFrame(cap)
    nextFrame = getFrame(cap)
    
    while(True):
        frameDifference = frameDiff(prevFrame, currFrame, nextFrame)
        
        _,fThresh = cv2.threshold(frameDifference, 0,255, cv2.THRESH_TRIANGLE)
        
        cv2.imshow("Frame Diff", frameDifference)
        cv2.imshow("Thresh", fThresh)
        
        # Update Frames
        prevFrame = currFrame
        currFrame = nextFrame
        nextFrame = getFrame(cap)
        
        k=cv2.waitKey(5)
        if k==27:
            break
    
    cap.release()
    cv2.destroyAllWindows()
        