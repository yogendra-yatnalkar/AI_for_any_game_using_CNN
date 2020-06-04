import os
import cv2
import time

class SaveFile:

    def __init__(self, path = None):
        self.path = path # directory path where the image needs to be saved

    def get_image_name(self):
        files_list = os.listdir(self.path)
        dir_len = len(files_list)
        files_list = []
        img_name = str(dir_len + 1) + '.png'
        return img_name
    
    def save_image(self, image_np_array): # numpy array of the image to be saved
        image_name = self.get_image_name()
        cv2.imwrite(os.path.join(self.path, image_name), image_np_array)
        return image_name

    def display_image(self,image_name, image_np_array):
        cv2.namedWindow(image_name,cv2.WINDOW_NORMAL)
        cv2.imshow(image_name, img)
        # cv2.resizeWindow(image_name, 400, 400)
        if cv2.waitKey(0) & 0xFF == ord('q'):
            cv2.destroyAllWindows()

    def save_df(self, pd_df): # pd_df --> pandas dataframe
        save_df_path = os.path.dirname(self.path) 
        # storing to the parent folder of images
        pd_df.to_csv(os.path.join(save_df_path, 'dataset.csv'), index = False)
            # save the in-memory df to csv

if __name__ == "__main__": # for testing this file
    start_time = time.time()
    obj = SaveFile('../game_dataset/')
    img = cv2.imread('test/test_image.jpg')
    img_name = obj.get_image_name()
    print(img_name)
    obj.save_image(img)
    end_time = time.time()
    print("Time Required : ", end_time - start_time)
    obj.display_image('test_img',img)
