import cv2
from PIL import ImageGrab
import numpy as np

class ScreenCapture:

    def __init__(self, x_ul, y_ul, x_br, y_br): 
        self.x_ul = x_ul
        self.y_ul = y_ul
        self.x_br = x_br
        self.y_br = y_br

    def image_grab(self):
        screen =  np.array(ImageGrab.grab(bbox=(self.x_ul,self.y_ul,self.x_br,self.y_br)))
        screen = cv2.cvtColor(screen,cv2.COLOR_RGB2BGR)
        return screen

if __name__ == "__main__": # Testing this file
    obj = ScreenCapture(0,0,640,480)
    from save_image import SaveImage
    save_obj = SaveImage('../game_dataset/')
    print(save_obj.get_image_name())

    flag = 0
    while(flag == 0):
        screen = obj.image_grab()

        cv2.namedWindow('scanned image',cv2.WINDOW_NORMAL)
        cv2.imshow('scanned image', screen)
        cv2.resizeWindow('scanned image', obj.x_br-obj.x_ul, obj.y_br-obj.y_ul)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            flag = 1
