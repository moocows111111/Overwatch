from PIL import Image
import os
directory = os.path.abspath('/home/moocows/PycharmProjects/Aim/data/')
file_paths = os.listdir(directory)

for _files in file_paths:
    img = Image.open(_files)
    halfWidth = img.size[0]/2
    halfHeight = img.size[1]/2
    croppedImage = img.crop(
        (
            halfWidth - 250,
            halfHeight - 250,
            halfWidth + 250,
            halfHeight + 250)
    )
    croppedImage.save('/home/moocows/PycharmProjects/Aim/croppeddata', 'JPEG')



