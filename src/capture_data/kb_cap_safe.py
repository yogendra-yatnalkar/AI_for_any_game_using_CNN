''' Note: ScreenCapture and SaveImage class will be integrated in this file. '''

from pynput import keyboard
import time
import pandas as pd
from save_file import SaveFile
from screen_capture import ScreenCapture
from utility import Utility

class KeyboardCapture:

    def __init__(self, x_ul, y_ul, x_br, y_br, save_path):
        # x_ul, y_ul --> x,y coordinates of upper left corner
        # x_br, y_br --> x,y coordinates of bottom right corner
        self.key_pressed = set()
        # action_df --> DataFrame where image and the action will be saved. Conver later to .csv
        self.action_df = pd.DataFrame(columns=['image_name','action'])
        self.sc_cap_obj = ScreenCapture(x_ul, y_ul, x_br, y_br)
        # sc_cap_obj --> screen capture object
        self.sv_file_obj = SaveFile(save_path) 
        self.save_path = save_path
        # sv_file_obj --> save file object

    def on_press(self, key):
        # if(key != keyboard.Key.esc):
        self.key_pressed.add(key)
        sc_grab = self.sc_cap_obj.image_grab() # screen grab
        img_name = self.sv_file_obj.save_image(sc_grab)  # save the screen to disk
        last_row = len(self.action_df)
        print(last_row)
        self.action_df.loc[last_row] = [img_name,self.key_pressed]
        print(img_name,self.key_pressed)
        print('\n',self.action_df)

    def on_release(self,key):
        if(key == keyboard.Key.esc):
            # Stop listener
            self.sv_file_obj.save_df(self.action_df)
            return False
        if(key in self.key_pressed):
            self.key_pressed.remove(key)

if __name__ == "__main__":
    start_time = time.time()
    util = Utility()
    x0,y0,x1,y1 = util.get_coordinates() #returns 4 coordinates
    # The module will start after a defined dalay
    delay_time = 3
    util.generate_delay(delay_time)
    save_img_path = 'D:/Yogendra D/AI_for_any_game_using_CNN/src/game_dataset'
    obj = KeyboardCapture(x0,y0,x1,y1,save_img_path)

    try:
        listener = keyboard.Listener(
        on_press=obj.on_press,
        on_release=obj.on_release)
        listener.run()
    except BaseException as error:
        print("Unexpected error : ",error)
        print("The current created dataset will be cleared")
    
    end_time = time.time()
    print("Time required for execution : ", end_time - start_time)