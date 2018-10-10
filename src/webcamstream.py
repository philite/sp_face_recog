
import numpy as np
import cv2

class WebCam():
    def __init__(self):
        #initiate videocapture
        self.cap = cv2.VideoCapture(0)

    def start(self):
        while True:
            #capture frame by frame
            ret, frame = self.cap.read()

            #operation on the frame
            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2RGBA)

            #display the resulting frame
            cv2.imshow('frame', gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.cap.release()
        cv2.destroyAllWindows()
        
