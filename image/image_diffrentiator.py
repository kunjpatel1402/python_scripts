from PIL import Image
import numpy

im = Image.open(r"C:\Users\Kunj R. Patel\Desktop\python\extra\me1.jpg")
im1 = im.resize((750,750))
arr1 = numpy.asarray(im1)

im = Image.open(r"C:\Users\Kunj R. Patel\Desktop\python\extra\me2.jpg")
im1 = im.resize((750,750))
arr2 = numpy.asarray(im1)
count = 0
for i in range(100) :
    for j in range(100):
        if (arr1[i][j][0] == arr2[i][j][0]) and (arr1[i][j][1] == arr2[i][j][1]) and (arr1[i][j][2] == arr2[i][j][2]):
            count += 1
        print ((i*100)+j)

print (count/10000)
