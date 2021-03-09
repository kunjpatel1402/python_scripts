from PIL import ImageEnhance
from PIL import Image
import numpy

im1 = Image.open(r"path")

enhancer = ImageEnhance.Color(im1)
#im1 = enhancer.enhance(0)
im1 = im1.resize((500,500))
#im1 = im1.rotate(90)
im1.show()

a = numpy.asarray(im1)
row = 0
pixels = numpy.ones((500,500,3))

for i in a:
    col = 0
    for j in i:
        print (j," ", row*500 + col)
        pixels[row,col,0] = 255 - j[0]
        pixels[row,col,1] = 255 - j[1]
        pixels[row,col,2] = 255 - j[2]
        #print (pixels[row-1,col-1])
        #print (row,col)
        col += 1
    row += 1

im2 = Image.new(im1.mode,(500,500))
new_pixels = im2.load()
for i in range(im2.height):
    for j in range(im2.width):
        new_pixels[i,j] = (int(pixels[i,j,0]),int(pixels[i,j,1]),int(pixels[i,j,2]))
        print (new_pixels[i,j])
        #print ((i*500) + j)
im2.show()
