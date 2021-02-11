#working in batches
#we work with batches to ensure optimal learning 
#by providing new information in a batch, 
#the neuron is able to create a good model.

#providing a batch size that is too large will
#cause your neuron to over fit and be less good at 
#generalising. It will do really well within the sample
#but badly when new data is presented 

import numpy as np

inputs = [[1, 2, 3, 2.5],
          [2.0, 5.0, -1.0, 2.0],
          [-1.5, 2.7, 3.3, -0.8]]

weights = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]

#be careful with the order of these are the dimensions of the final result is important
output = np.dot(inputs, np.array(weights).T) + biases
print(output)

