import os
import numpy as np
import cv2
from pyautogui import screenshot
import time

class Utility:

    def generate_delay(self, delay_time):
        for i in range(delay_time,0,-1):
            print("Program will start in : ",i)
            time.sleep(1)

    def get_coordinates(self):
        screen = np.array(screenshot())
        screen = cv2.cvtColor(screen,cv2.COLOR_RGB2BGR)
        # roi = cv2.selectROI(screen)
        x0, y0, w, h = cv2.selectROI(screen) 
        #returns the top-left corner coordinates and the width and height of the roi
        cv2.destroyAllWindows()
        x1 = x0 + w
        y1 = y0 + h
        return (x0,y0,x1,y1)

    def delete_images(self, path):
        pass
