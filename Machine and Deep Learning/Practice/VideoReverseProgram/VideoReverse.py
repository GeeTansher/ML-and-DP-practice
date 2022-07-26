import cv2

cap = cv2.VideoCapture('./Other/VideoReverseProgram/Video.mp4')

forec = cv2.VideoWriter_fourcc(*'MJPG')

h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
fps = cap.get(cv2.CAP_PROP_FPS)

print("Height - {} \nWidth - {} \nFPS - {}".format(h,w,fps))
lastFrame = cap.get(cv2.CAP_PROP_FRAME_COUNT)

out = cv2.VideoWriter('./Other/VideoReverseProgram/Reverse.avi',forec,fps,(int(w) , int(h)))

lastFrame = lastFrame-1

if cap.isOpened():
    while(lastFrame !=0):
        cap.set(cv2.CAP_PROP_POS_FRAMES, lastFrame)
        ret, frame = cap.read()
        # frame = cv2.resize(frame,(int(w*0.5),int(h*0.5))) # To reduce frame of size if you want (also change above in out if used)
        if ret==True:
            out.write(frame)
            lastFrame = lastFrame-1
        if(lastFrame%10 == 0):
            print(lastFrame)
            
print("Reversed Video Saved successfully.")
out.release()
cap.release()
cv2.destroyAllWindows()