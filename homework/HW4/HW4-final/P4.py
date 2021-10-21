#!/usr/bin/python3


### EXERCISE 4

class AutoDiffToy():
    
    def __init__(self,val, der = 1):
        self.val = val
        self.der = der
        
    def __mul__(self, other):
        try:
            der = self.der * other.val + self.val *other.der #CHAIN RULE
            val = self.val * other.val
        #return AutoDiffToy(der, val)
        except AttributeError:
            val = other * self.val
            der = self.der * other
        return AutoDiffToy(val, der)
    
    def __rmul__(self, other):
        return self.__mul__(other)
        
    def __add__(self, other):
        try:
            total_val= self.val + other.val
            total_der = self.der + other.der
        #return AutoDiffToy(total_val, total_der)
        except AttributeError:
            total_val = self.val + other
            total_der = self.der + 0
        return AutoDiffToy(total_val, total_der)
    
    def __radd__(self,other):
        return self.__add__(other)
        
    def __str__(self): ### THIS OVERWRITES YOUR PRINT ()
        temp = f"Value = {self.val}"
        if hasattr(self, "der"):
            temp+= f" Derivative: {self.der}"
        return temp
    
    
    
if __name__ == "__main__":
    a = 2.0
    x = AutoDiffToy(a)
    
    alpha = 3.0
    beta = 5.0
    
    f1 = alpha * x + beta
    f2 = x * alpha + beta
    f3 = beta + alpha * x
    f4 = beta + x * alpha

    f_list = [f1, f2, f3, f4]
    for i in f_list:
        print(i)
        
          