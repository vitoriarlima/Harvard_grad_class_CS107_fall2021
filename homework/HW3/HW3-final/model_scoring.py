#!/usr/bin/python3

import Regression as reg

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
#import regression classes

#dataset = datasets.load_diabetes()
dataset = datasets.fetch_california_housing()
X_train, X_test, y_train, y_test = train_test_split(dataset['data'], 
                                                    dataset['target'], 
                                                    test_size=0.2, 
                                                    random_state=42)

alpha = 0.5
model1 = reg.LinearRegression()
model2 = reg.RidgeRegression()

model1.set_params(alpha = 0.1)
model2.set_params(alpha = 0.1)


models = [model1, model2]

r_2_list= list()

for model in models:
    model.fit(X_train, y_train);
    r_2 = model.score(X_test, y_test)
    r_2_list.append(r_2)

print(r_2_list)

y_pred_train = model.predict(X_train)
y_pred_train


max_value = max(r_2_list)
index = r_2_list.index(max_value)

best_model = models[index]

print(best_model.get_params())