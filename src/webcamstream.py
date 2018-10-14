
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
            color = cv2.cvtColor(frame, cv2.COLOR_RGB2RGBA)

            #display the resulting frame
            cv2.imshow('WebCam', color)
            #self.save(ret, frame)
            if cv2.waitKey(1) & 0xFF == ord('s'):
                self.save()
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.cap.release()
        cv2.destroyAllWindows()
    
    def save(self):
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('D:/output.avi', fourcc, 25, (640, 480))
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret==True:
                frame = cv2.flip(frame, 1)
                #write the flipped frame
                out.write(frame)
                cv2.imshow('Saving video from Webcam...', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else: 
                break
        self.cap.release()
        out.release()
        cv2.destroyAllWindows()