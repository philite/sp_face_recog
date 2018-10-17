import dlib
class Face(object):
    def __init__(self):
            self.detector = dlib.get_frontal_face_detector()
            self.win = dlib.image_window()

    def detect(self, file_):
        self.file = file_
        for img in self.file:
            print('Processing image {}'.format(img))
            img = dlib.load_rgb_image(img)
            dets = self.detector(img, 1)
            print('Number of faces detected: {}'.format(len(dets)))
            self.win.clear_overlay()
            self.win.set_image(img)
            self.win.set_title('Number of faces detected: {}'.format(len(dets)))
            self.win.add_overlay(dets, color=dlib.rgb_pixel(0, 0, 255), )
            dlib.hit_enter_to_continue()

if __name__ == '__main__':
        Face()