#resize mask and rgb image together
import os, sys
from PIL import Image
import multiprocessing

size = 1024, 1024

path_JPEG_images = "/code/deeplab_aws/models/research/deeplab/datasets/VOCdevkit/VOC2012/JPEGImages/"
path_mask_centerline = "/code/deeplab_aws/models/research/deeplab/datasets/VOCdevkit/VOC2012/SegmentationClass/"

path_2048_images = "/code/deeplab_aws/models/research/deeplab/datasets/VOCdevkit/VOC2012/1024_JPEGImages/"
path_2048_mask = "/code/deeplab_aws/models/research/deeplab/datasets/VOCdevkit/VOC2012/1024_SegmentationClass/"


list_images = os.listdir(path_JPEG_images)   
if not os.path.exists(path_2048_images):
    os.makedirs(path_2048_images)
       
if not os.path.exists(path_2048_mask):
    os.makedirs(path_2048_mask)

    
def resize_image_mask(image_full_path,mask_full_path,outfile_image,outfile_mask):
    #---------------image resize -----------------------
    im = Image.open(image_full_path)
    im.thumbnail(size, Image.ANTIALIAS)
    #---------------mask resize -----------------------
    mk = Image.open(mask_full_path)
    mk.thumbnail(size, Image.ANTIALIAS)
    print(outfile_image)
    im.save(outfile_image, "png")
    mk.save(outfile_mask, "png")
    
starmap_list = []

for i in list_images:
    image_full_path = path_JPEG_images + i
    mask_full_path = path_mask_centerline + i
    outfile_image = path_2048_images + i
    outfile_mask = path_2048_mask + i
    starmap_list.append([image_full_path,mask_full_path,outfile_image,outfile_mask])
    
print(len(starmap_list))   

with multiprocessing.Pool(processes=11) as pool:
    pool.starmap(resize_image_mask,starmap_list)    
    
