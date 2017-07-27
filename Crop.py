from PIL import Image
import os
import cv2
import glob

#I will comment these out.
#directory = os.path.abspath('/home/moocows/PycharmProjects/Aim/data/')
#file_paths = os.listdir(directory)
images = glob.glob("*.jpg")

for image in images:
    img = cv2.imread(image,1)
    path = '/home/moocows/PycharmProjects/Aim/croppeddata/'
    crop_img = img[(540-200):(540+200), (960-200):(960+200)]

    cv2.imwrite(str(path) + image, crop_img)

    


