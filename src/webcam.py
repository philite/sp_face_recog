
import cv2
import dlib

class Webcam(object):
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.detector = dlib.get_frontal_face_detector()
        self.detect()
    
    def detect(self):
        while True:
            ret, frame = self.cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            dets = self.detector(gray, 1)
            img = cv2.rectangle(frame, (dets.left(), dets.bottom()), (dets.right(), dets.top()),(255, 255, 0), 2)
            cv2.imshow('test', img)
            if cv2.waitKey(0) & 0xFF == 'q':
                break
