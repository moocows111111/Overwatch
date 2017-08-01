from PIL import Image
import os.path
import glob

#this test is for a series of 12 pictures. The goal is to divide the list into 3 parts. This should make about 4 bins for the images.
#Then the idea is to blend the images in each bin together to make a final composite.


#Lists Directory
Dir = os.listdir('/home/moocows/PycharmProjects/Aim/blendtest')
#Glob all jpgs
im = glob.glob( '/home/moocows/PycharmProjects/Aim/blendtest/*.jpg')

#sort jpg according to name = time as well
imsort = sorted(im)

#I want to define chunker because I'll be calling from it using j.

#The code below basically is saying that we'll take the entire list right now and we will parse all info into groups of 3
def chunker(imsort,size = 3):
    for i in range(0, len(imsort), size):
        yield imsort[i:i + size]


#With is I want to see what we have. So I make sure to print j.        
print('what does it look like?')
for j in chunker(imsort):
    print(j)

    # so from here I realized that when you call j[0] it'll call all position 1 values in each single bin. Since we are working
    #with 12 images we have 4 total bins, meaning we have 4 values of j[0]. This is a problem. BUT however this can be useful 
    #because it allows the computer to do everything at once instead of going through the list systematically
    
    #Lets open up the images using Image from PIL
    img1 = Image.open(j[0])
    img2 = Image.open(j[1])
    img3 = Image.open(j[2])

    #Then I blend the images using the blend function. 
    imgbld1 = Image.blend(img1, img2, 0.3)
    imgbld2 = Image.blend(imgbld1, img3, 0.3)
    imgbld2.show()
    #Now I show the final result.
   
    #we have success right now but however now I need to save the results. My idea is to save the results using the row number in
    #the matrix we have created earlier. This way I dont mix up anything keep my temporal data.
    


