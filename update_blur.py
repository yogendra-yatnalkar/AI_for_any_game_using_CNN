import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui
import pydirectinput

def process_img(image):
    original_image = image
    # convert to gray
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # edge detection
    processed_img =  cv2.Canny(processed_img, threshold1 = 200, threshold2=300)
    return processed_img

def main():
    
    for i in list(range(6))[::-1]:
        print(i+1)
        time.sleep(1)

    last_time = time.time()
    print("We are going to press w now ")
    pydirectinput.keyDown('w')
    print("We pressed w just now")
    while True:
        #PressKey(W)
        pydirectinput.keyDown('w')
        screen =  np.array(ImageGrab.grab(bbox=(0,0,640,480)))
        # screen =  np.array(ImageGrab.grab(bbox=None))
        #print('Frame took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        new_screen = process_img(screen)
# ------------------------------------------------------------
        # cv2.namedWindow('san',cv2.WINDOW_NORMAL)
        # cv2.resizeWindow('san', 788,670)
        cv2.imshow('san', new_screen)
# --------------------------------------------------------------
        #cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
main()
