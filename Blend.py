from PIL import Image

#Toy example of the idea thus far.
data = [1,2,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print("this is the data ")
print(data)

# Takes existing list and segments into batches.
def chunker(data,size):
    for i in range(0, len(data), size):
        yield data[i:i + size]

# trying to show wtf is going on here
print('what does it look like')

#4 means the batch size which is 4 numbers within each batch.  this piece of code will show me what "data" looks like after transformation.
for j in chunker(data, 4):
    print(j)
  
#this will give a pretty good output with 
#[1,2,3,4]
#[5,6,7,8]
#[9,10,11,12]
#[13,14,15,16]
#[17,18,19,20]
# Now the next step is to be able to operate on only the numbers within each batch and do something like a simple summation
#eg: [1+2+3+4]. Then do the same for the rest of the batces [5+6+7+8] etc. Then we name them accordingly.

a= "frame144.jpg"
b="frame145.jpg"
c="frame146.jpg"
d="frame147.jpg"
e="frame148.jpg"
f="frame149.jpg"
g="frame150.jpg"
h="frame151.jpg"
i="frame152.jpg"
j="frame153.jpg"
k="frame154.jpg"

img1 = Image.open(a)
img2 = Image.open(b)
img3 = Image.open(c)
img4 = Image.open(d)
img5 = Image.open(e)
img6 = Image.open(f)
img7 = Image.open(g)
img8 = Image.open(h)
img9 = Image.open(i)
img10 = Image.open(j)
img11 = Image.open(k)

imgbld1 = Image.blend(img1, img2, 0.3)
imgbld2 = Image.blend(imgbld1, img3, 0.3)
imgbld3 = Image.blend(imgbld2, img4, 0.3)
imgbld4 = Image.blend(imgbld3, img5, 0.3)
imgbld5 = Image.blend(imgbld4, img6, 0.3)
imgbld6 = Image.blend(imgbld5, img7, 0.3)
imgbld7 = Image.blend(imgbld6, img8, 0.3)
imgbld8 = Image.blend(imgbld7, img9, 0.3)
imgbld9 = Image.blend(imgbld8, img10, 0.3)
imgbld10 = Image.blend(imgbld9, img11, 0.3)

imgbld10.show()
#this will show me the final results that I want.







