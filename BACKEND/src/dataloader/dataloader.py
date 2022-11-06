from threading import local
import cv2
import urllib.request as urllib
import numpy as np
from ..utils import Utils
from urllib.request import Request, urlopen


class ImageLoader():
    def __init__(self, id : str = None, img: np.array = None):
        """
        This is the Image Loader class which loads the image from either the NASA website (from its ID) or from a local file (img). Hence, id and img should not be "not None" in the same time.

        Parameters
        ----------

        id (str) : choice 1 - the image ID found in NASA Juno website.
        img (np.array) : choice 2 - the image in np.array.

        id should be in ' ' not in " " 
        """
        self.id = id
        self.img = img
        
        if self.id is not None:
            self.url = f"https://www.missionjuno.swri.edu/Vault/VaultOutput?VaultID={id}"
        
    def load(self):
        
        '''
        This function returns a np.array img either using the image ID from the NASA Juno website or in default from the upload file. 
        '''
        if self.id is not None:
            req = Request(
            url= self.url, 
            headers={'User-Agent': 'Mozilla/5.0'}
            )
            webpage = urlopen(req).read()
            img = Utils().decode(img_coded=webpage)
            return img
        elif self.img is not None:
            return self.img
