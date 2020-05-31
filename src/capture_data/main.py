from pynput import keyboard
import time
import pandas as pd

class KeyboardMonitor:

    def on_press(self,key):
        print("Key Pressed : ",key)
    
    def on_release(self,key):
        print("Released Key : ",key)
        print(keyboard.KeyCode)
        if(key == keyboard.Key.esc):
            # Stop listener
            return False

def main():
    obj = KeyboardMonitor()

    listener = keyboard.Listener(
    on_press=obj.on_press,
    on_release=obj.on_release)

    listener.run()

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print("Time required for execution : ", end_time - start_time)