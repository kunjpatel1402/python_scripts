from PIL import ImageEnhance
from PIL import Image
import numpy
#converts image into ascii characters
im1 = Image.open(r"path")
enhancer = ImageEnhance.Color(im1)
#im1 = enhancer.enhance(0)
im1 = im1.resize((750,750))
#im1 = im1.rotate(90)
im1.show()

chars = ["@","#","S","&","?","*","+",";",":",",","."]
a = numpy.asarray(im1)
count = 0

with open(r".\image.txt", "w") as file:
    for i in a:
        for j in i:
            sym = (chars[int(( j[0] + j[1] + j[2] ) / 76.5 )])
            print(sym," ",count)
            count += 1
            file.write(sym)
        file.write("\n")
    file.close()    
        
