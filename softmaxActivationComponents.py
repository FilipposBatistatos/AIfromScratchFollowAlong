#creating the concepts that will allow us to create the softmax activation


import math
import numpy as np

layer_output = [4.8, 1.21, 2.385]

E = math.e

#using the exponent formular will remove all the negative values
#in a reversable manner
# for output in layer_output:
#     exp_values.append(E**output)

#replaces the code above
exp_values = np.exp(layer_output)

# norm_base = sum(exp_values)
# norm_values = []

# for value in exp_values:
#     norm_values.append(value / norm_base)

#replaces above code
norm_values = exp_values / np.sum(exp_values)

print(norm_values)
print(sum(norm_values))
