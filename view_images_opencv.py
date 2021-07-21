import cv2 

image_1 = cv2.imread("/Users/prajendr/workhere/road_centerline/data/images_2048/20938-50656-17_2048.pngr")
image_2 = cv2.imread("/Users/prajendr/workhere/road_centerline/data/images_2048/20938-50656-17.png")

cv2.imshow("2048",image_1)
cv2.imshow("1024",image_2)
cv2.waitKey(0)
