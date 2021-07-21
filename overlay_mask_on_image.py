#overlay mask on the rgb image after inference 
import cv2
import numpy as np


inference_folder = "/code/road_centerline/data/inference_results_10_90/exp/train_on_train_set/vis/segmentation_results/"
overlaped_inference_mask =  "/code/road_centerline/data/inference_results_10_90/exp/train_on_train_set/vis/overlaped/"

if not os.path.exists(overlaped_inference_mask):
    os.makedirs(overlaped_inference_mask)
    
listimage = os.listdir(inference_folder)

list_inference_image = []
for km in listimage:
    if km.endswith(".png"):
        if km.endswith("_image.png"):
            imgpath = inference_folder+ km
            list_inference_image.append(km.split("_")[0]+".png")
            maskpath = inference_folder + km.split("_")[0]+"_prediction.png"
            print(km,km.split("_")[0]+"_prediction.png")
            rgbimg = cv2.imread(imgpath)
            mask = cv2.imread(maskpath)
            new_mask = np.zeros((2048, 2048, 3), dtype=np.uint8)
            for j in range(0,2048):
                for k in range(0,2048):
                    if mask[j,k][2] == 128:
                        new_mask[j,k,:]=[0,0,255]
                    else:
                        new_mask[j,k,:]=rgbimg[j,k,:]
            savepath =  overlaped_inference_mask + km.split("_")[0]+"_overlap.png"   
            cv2.imwrite(savepath,new_mask)
