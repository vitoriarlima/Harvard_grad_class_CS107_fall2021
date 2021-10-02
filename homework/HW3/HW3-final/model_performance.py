#!/usr/bin/python3

import Regression as reg

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split

dataset = datasets.fetch_california_housing()
X_train, X_test, y_train, y_test = train_test_split(dataset['data'], 
                                                    dataset['target'], 
                                                    test_size=0.2, 
                                                    random_state=42)

a_list = [0.001, 0.01, 0.1, 1, 10]
a_list = np.linspace(0.001, 10, 1000)

model1 = reg.LinearRegression()
model2 = reg.RidgeRegression()



r_2_list_model1= list()
r_2_list_model2= list()


for a in a_list:
    model1.set_params(alpha = a)
    model2.set_params(alpha = a)
    
    model1.fit(X_train, y_train);
    model2.fit(X_train, y_train);

    r_2_1 = model1.score(X_test, y_test)
    r_2_list_model1.append(r_2_1)
    
    
    r_2_2 = model2.score(X_test, y_test)
    r_2_list_model2.append(r_2_2)

#print(r_2_list_model1)
#print(r_2_list_model2)
plt.figure(figsize=(8,8))
plt.plot(a_list, r_2_list_model1, label = 'Linear regression model')
plt.plot(a_list, r_2_list_model2, label = 'Ridge regression model')
plt.xlabel("Alpha values")
plt.ylabel("R squared")
plt.title("Plot of the performance of linear vs ridge regressions")
plt.legend()
plt.draw()
plt.savefig("P2F.png", dpi=300, bbox_inches='tight')

plt.show()

