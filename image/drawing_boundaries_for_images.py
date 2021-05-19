from PIL import Image
import numpy

im1 = Image.open(r"C:\Users\Kunj R. Patel\Desktop\codes\python\image related\mario.jpg")
height = 500
width = 500
im1 = im1.resize((height,width))
im1.show()

a = numpy.asarray(im1)
row = 0
im2 = Image.new(im1.mode,(height,width))
new_pixels = im2.load()

for i in range(len(a)):
    col = 0
    for j in range(len(a[i,:])):
        print(i*width + j,"/",height*width)
        #new_pixels[col,row] = (a[i,j,0],a[i,j,1],a[i,j,2])
        new_pixels[col,row] = (256,256,256)
        if j < (len(a[i,:])-1):
            x = (int(a[i,j,0])+int(a[i,j,1])+int(a[i,j,2]))
            y = (int(a[i,j+1,0])+int(a[i,j+1,1])+int(a[i,j+1,2]))
            #print(x,y,end="    ")
            if abs(x-y) >= 25:
                new_pixels[col,row] = (0,0,0)
                #print("boundary")
        col += 1
    row += 1
im2.show()