#rectified linear activation
#it is simple and thus easy to compute
#it is the most popular activation
#watch this for more information on activation formulas:
#https://www.youtube.com/watch?v=gmjzbpSVY1A&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3&index=5

#study on the function of neural networks
#https://cs231n.github.io/neural-networks-case-study/

import numpy as np
import nnfs
from nnfs.datasets import spiral_data

nnfs.init()

X, y = spiral_data(100, 3)

inputs = [0, 2, -1, 3.3, -2.7, 1.1, 2.2, -100]
output = []

#EXAMPLES OF ACTIVATION FUNCTIONS
#___________________________________________________
# for i in inputs:
#     if i > 0:
#         output.append(i)
#     elif i <= 0:
#         output.append(0)

#same result further compressed
# for i in inputs:
#     output.append(max(0, i))

# print(output)
#_____________________________________________________

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases


class Activation_ReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)

layer1 = Layer_Dense(2, 5)
activation1 = Activation_ReLU()

layer1.forward(X)
#print(layer1.output)
activation1.forward(layer1.output)
print(activation1.output)
