import numpy
from stack import CoordinateStack
from complex import Complex
import math


func = numpy.empty((2,500))
func[0,0:250]=1
func[0,250:500]=0
func[1,:]=0
def get_coeff(func,size,number_of_coeff):
    del_t = 1/(size)
    n = number_of_coeff
    Cn = numpy.empty((2,n))
    for i in range(n):
        coeff = Complex(0,0)
        t = del_t
        print(i,"/",n,end="\r")
        for j in range(size):
            coeff += ((Complex(func[0,j],func[1,j]))*(Complex(math.cos((i-n/2)*2*math.pi*t),-math.sin((i-n/2)*2*math.pi*t))))*Complex(del_t,0)
            t += del_t
        Cn[0,i]=coeff.x
        Cn[1,i]=coeff.y
    return Cn

def plot(del_t,Cn,n):
    t=del_t
    number_of_points = int(1/del_t)
    set_points = numpy.empty((2,number_of_points))
    for j in range(number_of_points):
        coeff = Complex(0,0)
        print(t,"/",1,end="\r",flush=True)
        for i in range(n):
            coeff += ((Complex(Cn[0,i],Cn[1,i]))*(Complex(math.cos((i-n/2)*2*math.pi*t),+math.sin((i-n/2)*2*math.pi*t))))
        set_points[0,j] = coeff.x
        set_points[1,j] = coeff.y
        #print(coeff.x,coeff.y)
        t += del_t
    return set_points

#set_points = plot(1/500,500,get_coeff(func,500),100)

#numpy.savetxt("func.txt",set_points,delimiter=',')