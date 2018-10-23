from PIL import Image
from PIL.ImageQt import ImageQt
import os
from logging import debug as log 

class ImageHandler:
    def __init__(self,fnames):
        self.MAX_LOAD = 10
        self.current = 0
        self.last_load = 0
        self.fnames = fnames
        self.images = list()

        self.load_images()
    
    def load_img(self,imgfname):
        if os.path.exists(imgfname):
            return ImageQt(Image.open(imgfname))
    
    def load_images(self):
        end = min(self.last_load+self.MAX_LOAD,len(self.fnames))
        for i in range(self.last_load,end):      
            self.images.append(self.load_img(self.fnames[i]))
        
        self.last_load = end-1
        log('last batch load upto '+str(self.last_load))
        
    
    def next_img(self):
        if self.current < self.last_load:
            self.current += 1
            log('Current: '+str(self.current))
            return self.images[self.current]
        else:
            raise NotImplementedError()
    
    def getCurrent(self):
        return self.images[self.current]