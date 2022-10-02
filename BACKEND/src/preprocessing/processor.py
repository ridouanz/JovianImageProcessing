from ..dataloader import ImageLoader
import numpy as np 
import cv2 as cv
from scipy.ndimage import median_filter

class ImageProcessor(ImageLoader):
    def __init__(self, id: str):
        super().__init__(id)
        self.img = self.load()

    def enhance(self, clipLimit = 10.0, window = 50, denoising = True, sharpen=True):
        sharpen_kernel = np.array([[0, -1, 0],
                        [-1, 5, -1],
                        [0, -1, 0]])

        clahe = cv.createCLAHE(clipLimit = clipLimit, tileGridSize = (window, window))

        img_result = np.zeros(self.img.shape)
        img_result[:,:,0] = clahe.apply(self.img[:,:,0])
        img_result[:,:,1] = clahe.apply(self.img[:,:,1])
        img_result[:,:,2] = clahe.apply(self.img[:,:,2])

        img_result = median_filter(img_result.astype('uint8'), 3)

        if denoising :
            img_result = cv.fastNlMeansDenoisingColored(img_result, None, 3, 3)

        if sharpen :
            img_result = cv.filter2D(src=img_result, ddepth=-1, kernel=sharpen_kernel)

        return img_result