#!/usr/bin/python3


## EXERCISE 1

import numpy as np
import matplotlib.pyplot as plt


def numerical_diff(f, h):
    def first_derivative(x):
        return (f(x+h) - f(x))/h   
    return first_derivative

def f(x):
    return np.log(x)

numerical_diff(f, 0.1)(0.5)

h =[1e-15, 1e-7, 1e-1] #h = [0.000000000000001, 0.0000001, 0.1]

x = np.array(np.linspace(0.2, 0.4, 1000))

graph_list = []
for i in h:
    #print(h)
    list_h_vals = []
    for j in x:
        point_derivative = numerical_diff(f, i)(j)
        list_h_vals.append(point_derivative)
        #print(point_derivative)
    graph_list.append(list_h_vals)
    
def real_first_derivative(x):
    return 1/x

real_deriv = []
for i in x:
    real_derivative = real_first_derivative(i)
    real_deriv.append(real_derivative)
    
graph_list = np.array(graph_list)

h1 = graph_list[0].reshape(-1,1) # h of 10 - 15
print(len(h1))
h2 = graph_list[1].reshape(-1,1) # h 10 -7
h3 = graph_list[2].reshape(-1,1) # h = 0.01



plt.figure(figsize = (20, 20))
#plt.plot(h, graph_list)
plt.plot(x, h1, '--', label = "derivative with h = 1*10^(-15)" ) 
plt.plot(x, h2, color = "yellow", label = "derivative with h = 1*10^(-7)")
plt.plot(x, h3, '--', color = "green" ,label = "derivative with h = 0.1")
plt.plot(x, real_deriv, '--', color = "pink", label = "real derivative, 1/x")
plt.title("Plot showing the derivate of 10 x points with different h steps and showing also the real derivative 1/x", size = 20)
plt.xlabel("x", size = 20)
plt.ylabel("f'(x)", size = 20)
plt.legend(fontsize = 20)
plt.savefig("P1_fig.png", dpi = 300, bbox_inches = 'tight')
plt.show()

print("Answer to Q-a:")
print("Which value of h most closely approximates the true derivative? What happens for values of h that are too small? What happens for values of h that are too large?")

print("To the values of h that are too small, the derivative with that stepsize \
h is going to be choppy and not smooth enough as the real derivative because of truncation error. Whereas for the h that are too big, \
we get a derivative that is smaller than the real one, i.e. the stepsize is too big and the derivative is \
an underestimation of the real derivative. \
I have found the stepsize of a*10^_-7 to be the value that most closely approximates the true derivative")

print("Answer to Q-b:")
print("Q-b: How does automatic differentiation address these problems?")

print("The way that AD addresses this is to make the calculations of the derivative more easy  \
i.e. broken down in more parts. What AD does is to use basic arithmetic operations (additiona, multiplication, division) \
on any function (like functions like log, sin and so on) in order to break any complex function into smaller less complex ones. \
What is hapening is that AD breaks down the big complex function into these primitive parts where the computation of\
the derivative is easier to compute. Then the derivative of the complex function will be the combination of\
all these smaller parts' derivatives.\
Particularly, AD uses the chain rule as principle to evaluate  derivatives. Consequently, AD\
can guarantee a very precise computation of derivatives.")

print("Additionally, given that it takes a lot of computing power to find the entire curve \
of derivatives for a function f(x) with a given stepsize h (where the smallest usually the \
better, i.e. even more computation power needed), we can still use the 'optimal' h but do the derivative \
only at the point we deem necessary. AD helps us save computing power to get only the point derivative that we need.")



