import cv2 as cv
import numpy as np
class mean_filter(object):
    def __init__(self, image, kernel_size):
        self.image = image
        self.kernel_size = kernel_size
        self.H = image.shape[0]
        self.W = image.shape[1]
        self.image_res = image.copy()
    def calculate_mean(self, img):
        mean = np.mean(img)
        return mean
    def preprocessing_image(self):

        for H in range(self.H):
            H_start = H
            H_end = H_start + self.kernel_size
            for W in range(self.W):
                W_start = W
                W_end = W_start + self.kernel_size

                tmp = self.image[H_start: H_end, W_start: W_end]
                if tmp.shape[0] == self.kernel_size and tmp.shape[1] == self.kernel_size:
                    self.image_res[H_start: H_end, W_start: W_end][int(self.kernel_size / 2)][
                        int(self.kernel_size / 2)] = self.calculate_mean(tmp)
                else:
                    break
        return self.image_res

image = cv.imread(r"D:\FAMILY\Su\z4334388270363_98ded100e255012940630469557fb908.jpg", 0)
image = cv.resize(image, (512, 512))

image_mean = mean_filter(image,7)
image_mean = image_mean.preprocessing_image()

cv.imshow("org", image)
cv.imshow("mean", image_mean)
cv.waitKey(0)