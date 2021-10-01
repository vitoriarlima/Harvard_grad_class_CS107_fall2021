# Coder: Maxime Laasri
# Sharer: Kamran Ahmed
# Listener: Vitoria Lima

# Exercice 1
# ==========

import numpy as np

# Defining our class
class Layer:
    
    def __init__(self, shape, activation_function):
        self.shape = shape
        self.activation_function = activation_function
        self._weights = np.random.uniform(-1.0, 1.0, size = shape)
        self._bias = np.random.uniform(-1.0, 1.0, size = shape[1])
    
    def forward(self, inputs):
        return self.activation_function(np.dot(inputs, self._weights) + self._bias)

# Testing our class
layer1 = Layer((100, 30), np.tanh)
layer2 = Layer((30, 1), np.tanh)

t = np.random.uniform(0.0, 1.0, 100).reshape(1, -1)
h1 = layer1.forward(t)
print("Output of first layer:", h1)

h2 = layer2.forward(h1)
print("Output of second layer:", h2)

# Exercice 2
# ==========

# Redefining our class to enrich it
class Layer:
    
    def __init__(self, shape, activation_function):
        self.shape = shape
        self.activation_function = activation_function
        self._weights = np.random.uniform(-1.0, 1.0, size = shape)
        self._bias = np.random.uniform(-1.0, 1.0, size = shape[1])
    
    def forward(self, inputs):
        return self.activation_function(np.dot(inputs, self._weights) + self._bias)
    
    def __str__(self):
        text = "Layer:\n"
        text += "-- %s inputs -> %s outputs\n" % (self.shape[0], self.shape[1])
        text += "-- Activation function: " + self.activation_function.__name__
        return text
    
    def __repr__(self):
        text = "Layer:\n"
        text += "-- %s inputs -> %s outputs\n" % (self.shape[0], self.shape[1])
        text += "-- Shape of the weights: " + str(self._weights.shape) + "\n"
        text += "-- Shape of the bias: " + str(self._bias.shape) + "\n"
        text += "-- Activation function: " + self.activation_function.__name__
        return text
    
    def __call__(self, inputs):
        return self.forward(inputs)

# Testing our new class
layer = Layer((100, 30), np.tanh)
layer # calls __repr__
print(layer) # calls __str__
layer(t) # calls __call__ (note that 't' is already defined)