import os
import cv2
import time

class SaveImage:

    path = None # directory path where the image needs to be saved

    def __init__(self, path):
        self.path = path

    def get_image_name(self):
        files_list = os.listdir(self.path)
        dir_len = len(files_list)
        files_list = []
        img_name = str(dir_len + 1) + '.png'
        return img_name
    
    def save_image(self, image_np_array): # numpy array of the image to be saved
        image_name = self.get_image_name()
        cv2.imwrite(os.path.join(self.path, image_name), image_np_array)

    def display_image(self, image_np_array):
        cv2.namedWindow('test image',cv2.WINDOW_NORMAL)
        cv2.imshow('test image', img)
        cv2.resizeWindow('test image', 400, 400)
        if cv2.waitKey(0) & 0xFF == ord('q'):
            cv2.destroyAllWindows()


if __name__ == "__main__": # for testing this file
    start_time = time.time()
    obj = SaveImage('../game_dataset/')
    img = cv2.imread('test/test_image.jpg')
    img_name = obj.get_image_name()
    print(img_name)
    obj.save_image(img)
    end_time = time.time()
    print("Time Required : ", end_time - start_time)
    obj.display_image(img)
