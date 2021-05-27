#view the pixel intensity of the image while display

import os
import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

prediction_images_nd_mask = "/segmentation_results/"

list_img_msk = os.listdir(prediction_images_nd_mask)

for j in list_img_msk:
	if j.endswith("_image.png"):
		image_path = prediction_images_nd_mask + j
		mask_path = prediction_images_nd_mask + j.split("_")[0]+"_prediction.png"
		img = cv2.imread(image_path)
		plt.figure(1)
		plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
		plt.show()
