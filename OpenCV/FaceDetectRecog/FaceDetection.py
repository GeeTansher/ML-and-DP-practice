import cv2

cap = cv2.VideoCapture(0)
# PATH = os.path.join('Practice', 'images')
# os.makedirs(PATH)
cascade_classifier = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

while cap.isOpened():
    ret,frame=cap.read()
    cv2.imshow('frame',frame)
    
    if ret:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        detections = cascade_classifier.detectMultiScale(gray,1.3,9)
        
        if(len(detections)>0):
            (x,y,w,h)=detections[0]        
            frame = cv2.rectangle(frame,(x,y),(x+w,w+h),(0,255,0),2)
            img_crop=frame[y:y+h,x:x+w]
            img_crop=cv2.resize(img_crop,(255,255))
            
        cv2.imshow('frame',frame)
            
        if cv2.waitKey(1) & 0XFF == ord('a'):
            cv2.imwrite("images/"+str(1)+".jpg",img_crop)
    
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()