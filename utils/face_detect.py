
import sys
import cv2
import dlib

detector = dlib.get_frontal_face_detector()
win = dlib.image_window()
path = [] #['data/test.jpg', 'data/1.jpg', 'data/2.jpg', 'data/3.jpg', 'data/4.jpg', 'data/5.jpg', 'data/6.jpg', 'data/7.jpg', 'data/8.jpg']

if len(sys.argv) > 1:
    for f in sys.argv[1:]:
        print('Processing image {}'.format(f))
        img = dlib.load_rgb_image(f)
        #img = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
        #img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        dets = detector(img, 1)
        print('Number of faces detected: {}'.format(len(dets)))
        for i, d in enumerate(dets):
            print('Detection {}: Left: {} Top: {} Right: {} Bottom: {}'.format(i, d.left(), d.top(), d.right(), d.bottom()))
        win.clear_overlay()
        win.set_image(img)
        win.set_title('Number of faces detected: {}'.format(len(dets)))
        win.add_overlay(dets, color=dlib.rgb_pixel(255,255,0))
        dlib.hit_enter_to_continue()

else:
    for f in path:
        print('Processing image {}'.format(f))
        img = dlib.load_rgb_image(f)
        #img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        #img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        dets = detector(img, 1)
        print('Number of faces detected: {}'.format(len(dets)))
        for i, d in enumerate(dets):
            print('Detection {}: Left: {} Top: {} Right: {} Bottom: {}'.format(i, d.left(), d.top(), d.right(), d.bottom()))
        win.clear_overlay()
        win.set_image(img)
        win.set_title('Number of faces detected: {}'.format(len(dets)))
        win.add_overlay(dets, color=dlib.rgb_pixel(255,255,0))
        dlib.hit_enter_to_continue()
