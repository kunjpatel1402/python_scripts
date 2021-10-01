
class Complex:
    def __init__(self,a,b):
        self.x=a
        self.y=b
    def __mul__(self, other):
        a = ((self.x)*(other.x)) - ((self.y)*(other.y))
        b = ((self.x)*(other.y)) + ((self.y)*(other.x))
        return Complex(a,b)
    def __add__(self,other):
        sum = Complex(self.x+other.x,self.y+other.y)
        return sum