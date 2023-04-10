from math import radians
import cv2
import numpy as np

def changeRadius(r):
    global radius
    radius = r
    
def changeFocus(f):
    global focus
    focus = f  
    
    
img = cv2.imread('./images/flower.jpg')
rows, cols = img.shape[:2]
focus = 1
radius = 150
mask = np.zeros((int(rows*(focus*0.1+1)),int(cols*(focus*0.1+1))))
     
cv2.namedWindow("TrackBar")
cv2.createTrackbar("Radius",'TrackBar',150,500,changeRadius)
# Learb how to add -ve value in focus track bar
cv2.createTrackbar("Focus",'TrackBar',1,10,changeFocus)



while(1):
    # Getting kernel according to focus
    kernel_x = cv2.getGaussianKernel(int(cols*(0.1*focus+1)),radius)
    kernel_y = cv2.getGaussianKernel(int(rows*(0.1*focus+1)),radius)
    # kernel_x = cv2.getGaussianKernel(int(cols*(focus+1)),radius)
    # kernel_y = cv2.getGaussianKernel(int(rows*(focus+1)),radius)
    
    # for -ve focus but something is not right
    # kernel_x = cv2.getGaussianKernel(int(cols*(0.1*abs(focus)+1)),radius)
    # kernel_y = cv2.getGaussianKernel(int(rows*(0.1*abs(focus)+1)),radius)
    
    kernel = kernel_y * kernel_x.T
    
    kernel = kernel/np.linalg.norm(kernel)
    
    mask = 255 * kernel
    output = np.copy(img)
    
    # Resizing mask of image size
    mask_impose = mask[int(0.1*focus*rows):,int(0.1*focus*cols):]
    # # mask_impose = mask[int(focus*rows):,int(focus*cols):,]
    
    # # for -ve focus
    # if focus>=0:
    #     mask_impose = mask[int(0.1*focus*rows):,int(0.1*focus*cols):]
    
    # else:
    #     mask_impose = mask[:int(0.1*focus*rows),:int(0.1*focus*cols)]
    
    for i in range(3):
        output[:,:,i] = output[:,:,i] * mask_impose
        
    cv2.imshow("original", img)
    cv2.imshow("vignette", output)
    k=cv2.waitKey(20)
    if(k==ord('q')):
        break
    elif(k==ord('x')):
        print(kernel_x.shape)
    elif(k==ord('y')):
        print(kernel_y.shape)
    elif(k==ord('i')):
        print(mask_impose.shape)
    elif(k==ord('k')):
        print(kernel.shape)
    
cv2.destroyAllWindows()
cap.release()