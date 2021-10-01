from PIL import Image
import numpy
from stack import CoordinateStack
from temp import get_coeff, plot
 
im1 = Image.open(r"note.jpeg")
height = 500
width = 500
im1 = im1.resize((height,width))
im1.show()

a = numpy.asarray(im1)
row = 0
im2 = Image.new(im1.mode,(height,width))
new_pixels = im2.load()
points = CoordinateStack(500*500)
print("size of image:", len(a),"*", len(a[0,:]))
for i in range(len(a)):
    col = 0
    state=0
    for j in range(len(a[i,:])):
        print(i,",",j,end='\r')
        new_pixels[col,row] = (255,255,255)
        if j < (len(a[i,:])-1):
            x = (int(a[i,j,0])+int(a[i,j,1])+int(a[i,j,2]))
            y = (int(a[i,j+1,0])+int(a[i,j+1,1])+int(a[i,j+1,2]))
            if (abs(x-y)) >= 150:
                new_pixels[col,row] = (0,0,0)
                points.push(-row,col)
        col += 1
    row += 1
print("")
row=0
col=0
for j in range(500):
    row=0
    state = 0
    for i in range(500):
        print(i,",",j,end='\r')
        if i < (499):
            x = (int(a[i,j,0])+int(a[i,j,1])+int(a[i,j,2]))
            y = (int(a[i+1,j,0])+int(a[i+1,j,1])+int(a[i+1,j,2]))
            if (abs(x-y)) >= 150:
                if new_pixels[col,row] == (255,255,255):
                    new_pixels[col,row] = (0,0,0)
                    points.push(-row,col)
        row+=1
    col+=1
print("")
im2.show()
set_points = points.func()
n=5000
fig = plot(1/set_points.stack_top,get_coeff(set_points.stack,set_points.stack_top,n),n)
numpy.savetxt("func.txt",fig,delimiter=',')