from PIL import ImageEnhance
from PIL import Image
import numpy

im1 = Image.open(r"path")

im1 = im1.resize((500,500))
im1.show()

a = numpy.asarray(im1)
row = 0
im2 = Image.new(im1.mode,(500,500))
new_pixels = im2.load()

for i in a:
    col = 0
    for j in i:
        print (j," ", row*500 + col)
        new_pixels[col,row] = (0,j[1],0)
        print (new_pixels[row,col])
        #print (pixels[row-1,col-1])
        #print (row,col)
        col += 1
    row += 1

im2.show()
