# File: exercise_1.py
# Coder: Erin Tomlinson
# Sharer: Kamran Ahmed
# Listener: Angel Hsu, Vitoria Lima

import numpy as np

def layer(shape, actv):
    def activation(inputs, weights, bias):
        assert shape == [inputs.shape[1], weights.shape[1]], "Mismatch of dimensions."
        return actv(np.dot(inputs, weights) + bias)
    return activation

t = np.random.uniform(0.0, 1.0, 100).reshape(1,-1)

# Initialize weights and biases
w1 = np.random.random((100, 30))
w2 = np.random.random((30, 5))
b1 = np.random.random((1, 30))
b2 = np.random.random((1, 5))

layer1 = layer(list(w1.shape), lambda x: np.maximum(x, 0)) # Define layer 1
layer2 = layer(list(w2.shape), lambda x: np.maximum(x, 0)) # Define layer 2

# Run through the network
h1 = layer1(t, w1, b1) # First layer
h2 = layer2(h1, w2, b2) # Last layer

print(h2)