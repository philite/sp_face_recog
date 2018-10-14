
#import libraries
import cv2
import numpy as np

#call classifier for face and eyes detection
face_classifier = cv2.CascadeClassifier('C:/Users/ashur/Anaconda3/pkgs/opencv-3.4.3-py36h597e314_200/Library/etc/haarcascades/haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier('C:/Users/ashur/Anaconda3/pkgs/opencv-3.4.3-py36h597e314_200/Library/etc/haarcascades/haarcascade_eye.xml')

def face_detector(img, size=0.5):
    #convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if faces is ():
        return img
    #given coordinates to detect face and eyes location from ROI
    for (x, y, w, h) in faces:
        x = x - 100
        y = y - 100
        w = w + 100
        h = h + 100
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    roi_gray = gray[y: y+h, x: x+w]
    roi_color = img[y: y+h, x: x+w]
    eyes = eye_classifier.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 0, 255), 2)
        roi_color = cv2.flip(roi_color, 1)
    return roi_color

#webcam stream for face detection
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv2.imshow('Face Detected', face_detector(frame))
    if cv2.waitKey(1) == 13:
        break

#when everything done, close all windows
cap.release()
cv2.destroyAllWindows()