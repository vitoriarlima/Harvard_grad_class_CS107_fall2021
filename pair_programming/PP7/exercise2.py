# AC 207 pair programming

# Partners: Angel, Chelsea, Vitoria

import numpy as np

def func(x,r):
    return(x**r, r*x**(r-1))

if __name == "__main__":
    print("Passing in x-3, x=4")
    print(func(3,4))
