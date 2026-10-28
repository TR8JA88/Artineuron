# The first Neural network hello world

A function that takes in 784 inputs and produces 10 outputs. 
This is called a fully connected neural network/a multilayer perceptron .

# linear layer 
We have z = Wx +b 
W is a matrix this provides us with a compact way of writing many equations together 
A§ linear layer is a mathematical operation that takes a collection of input numbers , multiplies them by learned weights, adds learned biases and produces a new collection of numbers.

What really are weights and biases given context ?

Weights are adjustable paramters that indicate how signfiicantly an element contributes towards the output. I imagine that at its core it the central tool the machine uses to improve back propgopogation I hypothesis is the process of teh machine reducing its error/ loss however its by adjusting teh weights and biases that
Checkpoint 6 
As  I also cover matrices in FM I am beginning to see matrices as tranfomrations, a type of function that takes in a particular sized matrix and outputs another.
# How does the newtwork learn 
Cross entropy loss is our method of measuring loss
# I assumed that if we wanted to measure the deviation from some value (the correct value) follwing statistical methods we mind find the squared difference
However that would work if our network was tryin to predict height but for our inital netwrok the purpose is to classify digits.
Cross entropy loss:  the model assigning a higher probability to the correct class.
L = -log(probability assigned to correct class)

The logarithm function fits this use case if the probabaility assigend to the correct class is 1 we compute -log(1)=0 . This is a very inetresting reflection as this is begginning to form a pattern the idea of evalauting a function based on a usecase we say this again with the softmax function we need a function that has paramters x = R and so can take in the whole number line but outputs values between 1 and -1 . f(x)= sin (x) or f(x)= cos(x) came to mind but it became clear our trig functions were not a good fit because they do not discriminate .

But importantly I think this may be an important principle in advanced modeling and mathematical applications were you are given a use case you wnat to predict and so you evalaute a function based on this usecase and the properties of that function.
First results training ; 

Epoch 1: loss = 0.2523
Epoch 2: loss = 0.1512
Epoch 3: loss = 0.1434
Epoch 4: loss = 0.0504
Epoch 5: loss = 0.0505

// An epoch represents 1 pass through the training data set.

# The learning process 
-
The network produces ten logits.

Cross-entropy uses those logits and the correct digit to calculate the loss.

The loss is a function of the network's weights and biases.

Calculus tells us how the loss changes as those parameters change.

Backpropagation calculates the gradients efficiently using the chain rule.

The optimiser uses those gradients to update the parameters.