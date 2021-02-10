#turning things into vectors and matrices
import numpy as np

inputs = [1, 2, 3, 2.5] 
weights = [0.2, 0.8, -0.5, 1.0] 
bias = 2 

#the order is important when using layers
output = np.dot(weights, inputs) + bias
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

