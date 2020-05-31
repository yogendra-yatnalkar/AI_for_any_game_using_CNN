import cv2
import PIL
import numpy as np

class CaptureScreen:

    x_cord, y_cord = None, None

    def __init__(self, x_cord, y_cord): # Screen Capture will always start from the top-left corner
        self.x_cord = x_cord
        self.y_cord = y_cord

    def image_grab(self):
        screen =  np.array(PIL.ImageGrab.grab(bbox=(0,0,self.x_cord,self.y_cord)))
        screen = cv2.cvtColor(screen,cv2.COLOR_RGB2BGR)
        return screen

if __name__ == "__main__": # Testing this file
    