import cv2
import urllib.request as urllib
import numpy as np

from urllib.request import Request, urlopen


class ImageLoader():
    def __init__(self, id : str):
        """
        id should be in ' ' not in " " 
        """
        self.link = f"https://www.missionjuno.swri.edu/Vault/VaultOutput?VaultID={id}"

    def load(self):
        req = Request(
        url= self.link, 
        headers={'User-Agent': 'Mozilla/5.0'}
        )
        webpage = urlopen(req).read()


        arr = np.asarray(bytearray(webpage), dtype=np.uint8)
        img = cv2.imdecode(arr, -1) # 'Load it as it is'
        return img
