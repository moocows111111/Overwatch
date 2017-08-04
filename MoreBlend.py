import glob
import re
from PIL import Image

#Using the default sorted(function) creates issues with numbers like 10, 20, 100, 200 so I needed something more robust 
#and has a naturally sorted method.
#The function below allows me to do that and have no issues with these numbers.
def natural_key(string_):
    return [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', string_)]
#glob all jpg in the directory
im = glob.glob( '*.jpg')

#ensures the directory is sorted numerically based on the file name. This is incredibly important to have.
ims = sorted(im, key=natural_key)

#directory I want to save in
outdir = '/home/moocows/PycharmProjects/Aim/Blended/'


# want to take my list and blend in groups of 10. so I segregated the list as such.
def chunker(ims,size = 10):
    for i in range(0, len(ims), size):
        yield ims[i:i + size]

#since everything is made into chunks I want to take each one and take a picture oine at a time and blend with PIL's Blend function
for j in chunker(ims):
    print(j) #this allows me to debug all the functions I've implemented above.

    img1 = Image.open(j[0])  #opens all the images in each chunk
    img2 = Image.open(j[1])
    img3 = Image.open(j[2])
    img4 = Image.open(j[3])
    img5 = Image.open(j[4])
    img6 = Image.open(j[5])
    img7 = Image.open(j[6])
    img8 = Image.open(j[7])
    img9 = Image.open(j[8])
    img10 = Image.open(j[9])

    imgbld1 = Image.blend(img1, img2, 0.3) #.blend() can only blend 2 images at a time
    imgbld2 = Image.blend(imgbld1, img3, 0.3) # so I feed the previous blended image into the next one.
    imgbld3 = Image.blend(imgbld2, img4, 0.3)
    imgbld4 = Image.blend(imgbld3, img5, 0.3)
    imgbld5 = Image.blend(imgbld4, img6, 0.3) #its important to note that the blending causes the previous images to be degraded
    imgbld6 = Image.blend(imgbld5, img7, 0.3) #even moreso than what the alpha depicts. This is because of the additive nature
    imgbld7 = Image.blend(imgbld6, img8, 0.3) #of my script. This is intended to give a fade effect on the background of the images
    imgbld8 = Image.blend(imgbld7, img9, 0.3) #to denote changes in time.
    imgbld9 = Image.blend(imgbld8, img10, 0.3) #10 images are blended together at this point

    imgbld9.save(outdir + str(j) + '.jpeg') #saves the images into a seperate directory.
