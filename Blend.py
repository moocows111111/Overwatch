from PIL import Image

n = 10

#this will give me the chunks I want but I dont know how to access it and operate on one chunk at a time. I might have to do def chunks instead.
#for i in range(0 , len(data), n)
  #chunks = data[i:i+n]
#Toy example of the idea thus far.
data = [1,2,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print("this is the data ")
print(data)


def chunker(data,size):
    for i in range(0, len(data), size):
        yield data[i:i + size]

# trying to show wtf is going on here
print('what does it look like')

for j in chunker(data, 4):
    print(j)
  

#Chunk the directory
#get chunks

#basic operation...




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







