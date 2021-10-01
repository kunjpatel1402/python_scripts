import numpy as np

class CoordinateStack:
    def __init__(self,size):
        self.stack = np.empty((2,size),dtype=np.int32)
        self.stack_top=0
        self.size=size
    def push(self,x,y):
        if (self.stack_top < self.size):
            self.stack[0,self.stack_top] = x
            self.stack[1,self.stack_top] = y
            self.stack_top+=1
            return True
        else:
            return False
    def pop(self):
        if (self.stack_top==0):
            return None, None
        else:
            x, y = self.stack[0,self.stack_top], self.stack[1,self.stack_top]
            self.stack_top-=1
            return x, y 
    def __cost(self,a,b):
        return abs(self.stack[0,a]-self.stack[0,b]) + abs(self.stack[1,a]-self.stack[1,b])
    def __minKey(self,key,included):
        min = 1000000
        for v in range(self.stack_top):
            if (included[v]==False) and self.__cost(key,v) < min:
                min = self.__cost(key,v)
                min_index = v
                if min==1:return min_index
        return min_index
    def func(self):
        print("making func")
        included = np.zeros(self.size,dtype=bool)
        final_func = CoordinateStack(self.stack_top)
        current_pos = 0
        final_func.push(self.stack[0,current_pos],self.stack[1,current_pos])
        included[current_pos]=True
        count=1
        while (count < self.stack_top):
            print(count,"/",self.stack_top,end="\r")
            current_pos = self.__minKey(current_pos,included)
            final_func.push(self.stack[0,current_pos],self.stack[1,current_pos])
            included[current_pos]=True
            count+=1
        print("")
        return final_func
