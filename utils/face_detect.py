
import sys
import cv2
import dlib

detector = dlib.get_frontal_face_detector()
win = dlib.image_window()
path = 'test.jpg'
if len(sys.argv) >= 1:
    for f in sys.argv[1:]:
        print('Processing image {}'.format(f))
        img = dlib.load_rgb_image(f)
        #img = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
        #img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        dets = detector(img, 1)
        print('Number of faces detected: {}'.format(len(dets)))
        for i, d in enumerate(dets):
            print('Detection {}: Left: {} Top: {} Right: {} Bottom: {}'.format(i, d.left(), d.top(), d.right(), d.bottom()))
else:
    print('Processing image {}'.format(path))
    img = dlib.load_rgb_image(path)
    #img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    #img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    dets = detector(img, 1)
    print('Number of faces detected: {}'.format(len(dets)))
    for i, d in enumerate(dets):
        print('Detection {}: Left: {} Top: {} Right: {} Bottom: {}'.format(i, d.left(), d.top(), d.right(), d.bottom()))


    win.clear_overlay()
    win.set_image(img)
    win.add_overlay(dets)
    dlib.hit_enter_to_continue()
