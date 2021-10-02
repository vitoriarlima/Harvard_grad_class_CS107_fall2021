#!/usr/bin/python3

### Exercise 2 Part A

import numpy as np
import matplotlib.pyplot as plt

class Regression():

    def __init__(self):
        self.params = {'coefficients': [], 'intercept':0}

    def get_params(self):
        return self.params

    def set_params(self, **kwargs):
        #raise NotImplementedError
        pass
    
    def fit(self, X, y):
        beta = np.linalg.pinv(X.T@X)@(X.T@y)
        self.params['coefficients']= beta
        
    def predict(self, X):
        y_pred = X@self.params['coefficients'] + self.params['intercept']
        return y_pred

    def score(self, X, y):
        #R_2= 1 - sse/sst
        #self.predict(self,X) == y_pred
        #self.predict(X)
        sst = np.sum((y-y.mean())**2)
        sse = np.sum ((y - self.predict(X))**2)
        R_2= 1 - sse/sst
        return R_2



##### PART C

class LinearRegression(Regression):
    
    def __init__(self):
        #Super(Regression, self).__init__()
        super().__init__()
    
    
    def fit(self, X, y):
        rows = X.shape[0]
        new_col = np.ones((rows, 1))
        #hstack, vstack, concatenate, np.c_
        X = np.hstack((new_col, X))
        
        beta = np.linalg.pinv(X.T@X)@(X.T@y)
        
        self.params['intercept']= beta[0]
        self.params['coefficients']= beta[1:]


######## PART D

class RidgeRegression(LinearRegression):
     
    def __init__(self):
        super().__init__()
        
    def set_params(self, **kwargs): #keyword arguments #created new variables that can be used anywhere in ridge regression
        
        for k, v in kwargs.items():
            setattr(self, k, v)
        
        
    def fit(self, X, y):
        rows = X.shape[0]
        new_col = np.ones((rows, 1))
        #hstack, vstack, concatenate, np.c_
        X = np.hstack((new_col, X))
    
        for v in vars(self).keys():
            if v !='params':
                alpha = vars(self)[v]
                
        
        #alpha = self.set_params()
        G = alpha * np.identity(X.shape[1])
        
        beta = np.linalg.pinv(X.T@X + G.T@G)@(X.T@y)
        
        self.params['intercept']= beta[0]
        self.params['coefficients']= beta[1:]
