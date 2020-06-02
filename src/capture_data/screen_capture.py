import cv2
from PIL import ImageGrab
import numpy as np

class ScreenCapture:

    x_origin, y_origin = 0,0
    x_cord, y_cord = None, None

    def __init__(self, x_cord, y_cord): # Screen Capture will always start from the top-left corner
        self.x_cord = x_cord
        self.y_cord = y_cord

    def change_origin(self, x,y):
        self.x_origin = x
        self.y_origin = y

    def image_grab(self):
        screen =  np.array(ImageGrab.grab(bbox=(self.x_origin,self.y_origin,self.x_cord,self.y_cord)))
        screen = cv2.cvtColor(screen,cv2.COLOR_RGB2BGR)
        return screen

if __name__ == "__main__": # Testing this file
    obj = ScreenCapture(640,480)
    from save_image import SaveImage
    save_obj = SaveImage('../game_dataset/')
    print(save_obj.get_image_name())

    flag = 0
    while(flag == 0):
        screen = obj.image_grab()

        cv2.namedWindow('scanned image',cv2.WINDOW_NORMAL)
        cv2.imshow('scanned image', screen)
        cv2.resizeWindow('scanned image', obj.x_cord, obj.y_cord)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            flag = 1
