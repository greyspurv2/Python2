import random
import numpy
import scipy



def __init__(self, inputnodes, hiddennodes, outputnodes,
learningrate):
        # set number of nodes in each input, hidden, output layer
    self.innodes = inputnodes
    self.hnodes = hiddennodes
    self.onnodes = outputnodes


#link weight matrices, wih and who
# weights inside the array are w_i_j, where link is from node i to node j in the next layer
    self.wih = numpy.random.normal(0.0, pow (self.innodes, -0.5),
    self.hnodes, self.innodes)
    self.who = numpy.random.normal(0.0, pow (self.hnodes, -0.5),
(self.onodes, self.hnodes))
     self.who = numpy.random.normal(0.0, pow(self.hnodes, -0.5),
(self.onodes, self.hnodes))

#learning rate
self.lr = learningrate

#activation function used here is the sigmoid function, and can be expressed as such with scipy (also convetionally possible to express as --> def sigmoid(x):return 1 / (1 + np.exp(-x))
self.activation_function = lambda X: scipy.special.expit(x)

pass

#traning the NN
def train(self, inputs_lists, targets_list):
    # conver inputs list to 2nd array
inputs = numpy.array(inputs_list, ndmin=2) .T
targets = numpy.array(targets_list, ndmin =2) .T

# calculate signals into hidden layer
hidden_inputs = numpy.dot(self.wih, inputs)
# calculate the signals emerging from hidden layer
hidden_outputs = self.activation_function(hidden_inputs)

#calculate signals into final output layer
final_inputs = numpy.dot(self.who, hidden_outputs)
#calculate the signals emerging from final output layer
final_outputs = self.activation_function(final_inputs)


# output layer error is the (target - actual)
output_errors = targets - final_outputs
# hidden layer error is the output_errors, split by weights,
recombined at hidden nodes
    hidden_errors = numpy.dot(self.who.T, output_errors)

# update the weights for the links between the hidden and output layers
    self.who += self.lr * numpy.dot ((output_errors *
    fina_outputs * (1.0 - final_outputs)),
numpy.transpose(hidden_outputs)

    #update the weights for the links between the input and hidden layers
    self.wih += self.lr * numpy.dot(hidden_errors *
hidden_outputs * (1.0 - hidden_outputs)), numpy.transpose(inputs))

    pass

#query the NN
def query(self, inputs_list):
    #convert inputs list to 2d array
inputs = numpy.array(inputs_list, ndmin=2).T

# calculate the signals into hidden layer
hidden_inputs = numpy.dot(self.wih, inputs)
#calculate the signals emerging from hidden layer
hidden_outputs = self.activation_function(hidden_inputs)

#calculate signals into final output layer
finals_inputs = numpy.dot(self.who, hidden_outputs)
#calculate the signals emerging from final output layer
final_outputs = self.activation_function_function(final_inputs)

return final_outputs
