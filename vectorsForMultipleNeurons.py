#turning things into vectors and matrices
import numpy as np

inputs = [1, 2, 3, 2.5] 
weights = [[0.2, 0.8, -0.5, 1.0], 
           [0.5, -0.91, 0.26, -0.5], 
           [-0.26, -0.27, 0.17, 0.87]] 
biases = [2, 3, 0.5] 

#the order is important when using multiple neurons
#in thi case weights is a matrix so it has to be first
output = np.dot(weights, inputs) + biases

#np.dot(weight, input) = np.dot(weights[0], input), np.dot(weights[1], inputs), ...

print(output)













# layer_outputs = []
# #zip documentation https://www.w3schools.com/python/ref_func_zip.asp
# for neuron_weights, neuron_bias in zip(weights, biases):
#     neuron_output = 0
#     for n_input, weight in zip(inputs, neuron_weights):
#         neuron_output += n_input * weight
#     neuron_output += neuron_bias
#     layer_outputs.append(neuron_output)

# print(layer_outputs)

