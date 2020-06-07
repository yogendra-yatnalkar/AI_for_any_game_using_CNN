from PIL import Image
import imagehash

class RmDuplicate:
    
    def __init__(self,path):
        self.path = path
        self.hash_db = set()

    def remove_img(self):
        img_db = os.listdir(self.path)
        for img_name in image_db:
            img = Image.open('')
            hash = imagehash.averag_hash(img)
            if(hash in self.hash_db):
                os.remove('')
            else:
                hash_db.add(hash)
            img = None