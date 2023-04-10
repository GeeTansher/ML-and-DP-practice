import cv2
import numpy as np

mode = True
draw = False
# a=-1
# b=-1

def onChange(value):
    global mode
    if(value==0):
        mode = True
    elif(value==1):
        mode = False

def drawShape(event, x, y, flags, params):
    global draw,mode,a,b
    if(event == cv2.EVENT_LBUTTONDOWN):
        draw = True
        a,b = x,y  
        
    elif(event == cv2.EVENT_MOUSEMOVE):
        if(draw == True):
            if(mode == True):
                cv2.rectangle(img,(a,b),(x,y),(0,255,0),-1)
            else:
                cv2.circle(img,(x,y),abs(a-x),(255,0,0),-1)
            
    elif(event == cv2.EVENT_LBUTTONUP):
        draw = False  
        if(mode == True):
            cv2.rectangle(img,(a,b),(x,y),(0,255,0),-1)
        else:
            cv2.circle(img,(x,y),abs(a-x),(255,0,0),-1)
        
    

img = np.zeros((500,500,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',drawShape)
cv2.namedWindow('track')
cv2.createTrackbar('shape', 'track', 0,1,onChange)
while(True):
    cv2.imshow('image',img)
    k = cv2.waitKey(10)
    if(k==ord('m')):
        mode = not mode
    elif(k==27):
        break
    
cv2.destroyAllWindows()