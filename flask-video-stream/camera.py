import time
import cv2

class Camera(object):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""

    def __init__(self):
	self.cam = cv2.VideoCapture(0) 	
	self.cam.set(3, 800)
	self.cam.set(4, 600)
	time.sleep(1)

    def get_frame(self):
	ret, img = self.cam.read()
	ret2, jpeg = cv2.imencode('.jpg', img)
	return jpeg.tostring() 

    def __del__(self):
	self.cam.release()
