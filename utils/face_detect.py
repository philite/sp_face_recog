
import sys
import dlib
import scipy

detector = dlib.get_frontal_face_detector()
win = dlib.image_window()
path = ""
if len(sys.argv) >= 1:
    for f in sys.argv[1:]:
        print('Processing image {}'.format(f))
        img = dlib.load_rgb_image(f)
        dets = detector(img, 1)
        print('Number of faces detected: {}'.format(len(dets)))
        for i, d in enumerate(dets):
            print('Detection {}: Left: {} Top: {} Right: {} Bottom: {}'.format(i, d.left(), d.top(), d.right(), d.bottom()))

    win.clear_overlay()
    win.set_image(img)
    win.add_overlay(dets)
    dlib.hit_enter_to_continue()