#a loss function should be able to provide a value to indicate how 
#false the predictions is 
#hence, the more correct it is the smaller the value

import math

softmax_output = [0.7, 0.1, 0.2]
target_output = [1, 0, 0]

loss = -(math.log(softmax_output[0])*target_output[0] +
         math.log(softmax_output[1])*target_output[1] +
         math.log(softmax_output[2])*target_output[2])

print(loss)

loss = -math.log(softmax_output[0])*target_output[0]
print(loss)