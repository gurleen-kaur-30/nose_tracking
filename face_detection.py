import numpy as np
import cv2

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height
cnt = 10
while True:
    ret, img = cap.read()
    img = cv2.flip(img, 4)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,     
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(30, 30)
    )
    tracker = cv2.TrackerCSRT_create()
    if(cnt):
        print("hey")
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]  
            bbox = x+w/2 -20, y+h/2 - 20, 40, 40
    	    cv2.rectangle(img, bbox, (0,255,0), 2)
            tracker.init(img, bbox)
            cv2.imshow('video',img)
	    cnt = cnt - 1
    else:
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            ok, bbox = tracker.update(img)
            print(bbox)
            if ok:
                print("hello")
                (x, y, w, h) = [int(v) for v in bbox]
                cv2.rectangle(img, (x, y), (x + w, y + h),(0, 255, 0), 2)
            cv2.imshow('video',img)

            
        
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()


