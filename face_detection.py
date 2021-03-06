import numpy as np
import cv2

def getNose(x,y,w,h,img):
    centre_coordinates = (int(x+w/2), int(y+h/2 + 0.05*h))
    t = w/15
    l = h/4
    start_point = (int(x + w/2 - t), int(y + h/2 - 6 * l/10))
    end_point = (int(x + w/2 + t), int(y + h/2 + 4 * l/10))
    cv2.rectangle(img, start_point, end_point, (255, 0, 0), 1)
    cv2.circle(img, centre_coordinates, int(h/15), (255,0,0), 1)

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height
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
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]  
        getNose(x,y,w,h,img)
    cv2.imshow('video',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()


