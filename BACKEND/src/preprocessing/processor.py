from ..dataloader import ImageLoader
import numpy as np 
import cv2 as cv
from scipy.ndimage import median_filter

class ImageProcessor(ImageLoader):
    def __init__(self, id: str = None, img : bytes = None):
        super().__init__(id, img)
        self.image = self.load()
    
    def enhance(self, clipLimit = 10.0, window = 50, sharpen=True):

        sharpen_kernel = np.array([[0, -1, 0],
                        [-1, 5, -1],
                        [0, -1, 0]])


        clahe = cv.createCLAHE(clipLimit = clipLimit, tileGridSize = (window, window))

        img_result = np.zeros(self.image.shape)

        img_result[:,:,0] = clahe.apply(self.image[:,:,0])
        img_result[:,:,1] = clahe.apply(self.image[:,:,1])
        img_result[:,:,2] = clahe.apply(self.image[:,:,2])


        #img_result = median_filter(img_result.astype('uint8'), 3)
        img_result = img_result.astype("uint8")
        img_result= cv.bilateralFilter(img_result, 3, 31, 31)
    
        if sharpen :
            img_result[:,:,2] = cv.filter2D(src=img_result[:,:,2], ddepth=-1, kernel=sharpen_kernel)
        return img_result

    def enhance_2(self, clipLimit = 10.0, window = 50, denoising = True, sharpen=True):
        sharpen_kernel = np.array([[0, -1, 0],
                        [-1, 5, -1],
                        [0, -1, 0]])

        clahe = cv.createCLAHE(clipLimit = clipLimit, tileGridSize = (window, window))

        img_result = np.zeros(self.image.shape)
        img_result[:,:,0] = clahe.apply(self.image[:,:,0])
        img_result[:,:,1] = clahe.apply(self.image[:,:,1])
        img_result[:,:,2] = clahe.apply(self.image[:,:,2])

        #img_result = median_filter(img_result.astype('uint8'), 3)
        img_result = img_result.astype("uint8")
        img_result = cv.bilateralFilter(img_result, 9, 41, 41)

        if denoising :
            img_result = cv.fastNlMeansDenoisingColored(img_result, None, 3, 3)

        if sharpen :
            img_result = cv.filter2D(src=img_result, ddepth=-1, kernel=sharpen_kernel)

        return img_result