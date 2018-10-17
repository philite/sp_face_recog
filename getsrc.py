
import numpy as np
from src import webcamstream , Face

#webcam = webcamstream.WebCam()

#webcam.start()
#webcam.save()
face = Face.Face()
face.detect(['data/test1.jpg', 'data/test2.jpg', 'data/test3.jpg'])