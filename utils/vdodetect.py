
import sys
import cv2
import dlib

file = 'test.mp4'
cap = cv2.VideoCapture(file)
detector = dlib.get_frontal_face_detector()
win = dlib.image_window()
while True:
    ret, frame = cap.read()
    dets = detector(frame, 1)
    print('Number of faces detected: {}'.format(len(dets)))
    #for i, d in enumerate(dets):
     #   print('Detection {}: Left: {} Top: {} Right: {} Bottom: {}'.format(i, d.left(), d.top(), d.right(), d.bottom()))
    win.clear_overlay()
    win.set_image(frame)
    win.set_title('Number of faces detected: {}'.format(len(dets)))
    win.add_overlay(dets, color=dlib.rgb_pixel(255,255,0))