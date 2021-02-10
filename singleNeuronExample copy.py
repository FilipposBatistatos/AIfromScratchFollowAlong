#this is the code from !one! neuron in a hidden layer of the network

#outputs from the neurons in the previous layer or data from input layer
inputs = [1, 2, 3, 2.5] 
weights = [0.2, 0.8, -0.5, 1.0] #weights are associated to a unique input 
bias = 2 #each neuron has one unique bias

output = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + inputs[3]*weights[3] + bias
print(output)


