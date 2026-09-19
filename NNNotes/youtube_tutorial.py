from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import time

start = time.perf_counter()

"""
Data Setup
"""
# Two features aka two axes on our graph
# Two centers aka two custers
# We create 1000 data points
X, y = make_blobs(n_samples=1000, n_features=2, centers=2, random_state=1234)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
# plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train)
# plt.xlabel("x1")
# plt.ylabel("x2")
# plt.show()

"""
DataSets and loading data
"""
import torch
from torch.utils.data import TensorDataset, DataLoader
# Taking the data we just created and put it into these tensor objects
X_tensor_train = torch.tensor(X_train, dtype=torch.float32)
y_tensor_train = torch.tensor(y_train, dtype=torch.long)

X_tensor_test = torch.tensor(X_train, dtype=torch.float32)
y_tensor_test = torch.tensor(y_train, dtype=torch.long)

# Take the tensor objects and insert them into a tensor dataset. Will represent our data
dataset_train = TensorDataset(X_tensor_train, y_tensor_train)

# Take the dataset and put it inIs there any built in functions to get the execution time in python?to our DataLoader. Will help feed batches of data to our neural network while we're training it
# While training, the dataloader is going to feed 32 datapoints to our neural network at a time in each batch
dataloader_train = DataLoader(dataset_train, batch_size=32, shuffle=True)

# Do the same with our testing data
dataset_test = TensorDataset(X_tensor_test, y_tensor_test)
dataloader_test = DataLoader(dataset_test, batch_size=32, shuffle=True)

"""
Create our first Neural Network from Scratch
"""
import torch.nn as nn
import torch.optim as optim

# Discern if the device is running on CUDA
device = 'cuda' if torch.cuda.is_available() else 'cpu'

# Create the neural network
# When creating a neural network from scratch, you need to inherit from the neural network module
class MyFirstNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        # Inherits from the neural network modules init function
        super(MyFirstNN, self).__init__()
        # Typically in your constructor, you are going to Define all of the layers and activation functions that you're going to use
        self.layer_1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU() # Our activation function
        self.layer_2 = nn.Linear(hidden_size, output_size) # We pass it thru another layer to get the outputs
    
    # The forward function is where you're actually going to use those layers
    def forward(self, x):
        out = self.layer_1(x) # Passes the data into layer 1
        out = self.relu(out) # Passes the result thru our relu
        out = self.layer_2(out) # Passes the data to get the outputs
        return out # Returns our outputs

# Take the model we created and move it to the device
# In PyTorch, if you want to do operations on the GPU, you have to move the model and the data onto the GPU
model = MyFirstNN(input_size=2, hidden_size=3, output_size=2)
model.to(device)

# criterion A.k.a loss function
criterion = nn.CrossEntropyLoss() # A really common loss function when dealing with classification problems
optimizer = optim.Adam(model.parameters(), lr=0.001) # Adam is just an adaptation of gradient descent. lr == learning rate

# Print out the model to see what it looks like
# print(model)
# for param in model.parameters():
#     print(param) # requires_grad=True in the output means that autograd is enabled on the models parameters

"""
Training and Evaluation Loop
"""
num_epochs = 15 # Which means we're going to pass through all of our data 15 times
for epoch in range(num_epochs):
    # We first go through our training loop, this will go through all of our training data and update our models parameters
    ## Sometimes, when you create a model, you have certain things that you want to do during training, and not to do during testing
    model.train() ## This tells PyTorch that we're about to do training
    # We're pulling data freom our dataloader_train object
    for inputs, labels in dataloader_train:
        # Move the data to our device, moves the data to where our model already is
        inputs, labels = inputs.to(device), labels.to(device)

        # Forward pass
        class_predictions = model(inputs) # Makes predictions
        loss_train = criterion(class_predictions, labels) # Compares predictions to labels
        
        # Backward pass AND optimization
        optimizer.zero_grad() # Clears out the gradient values from the previous "step" (remember, same terminology as Machine Learning)
        loss_train.backward() # Computes gradients using the loss function
        optimizer.step() # Updates model's parameters using the gradients, Adam (aka gradient descent)

    """
    Testing Loop - Evaluate data it hasn't seen before
    """
    model.eval() # We call this to make sure it doesn't do anything we've defined in our neural network that we don't want it to
    with torch.no_grad(): # We need to tell it not to calculate gradients, its just testing data. We don't want to update the models parameters during these steps
        for inputs, labels in dataloader_test:
            # Move our batches of test data to the device
            inputs, labels = inputs.to(device), labels.to(device)

            # Calculate the predictions on the test data
            class_predictions = model(inputs)
            # Calculate the loss
            loss_test = criterion(class_predictions, labels)
    print(f'epoch [{epoch+1/num_epochs}] - loss_train: {loss_train.item():.4f} - loss_test: {loss_test.item():.4f}')

end = time.perf_counter()

"""
Visualizing how our model did
"""
# Turn off gradient tracking
with torch.no_grad():
    # We pass in the test features to get some predictions
    class_predictions = model(X_tensor_test.to(device))

    # Returns the index on each row that has the highest probability
    _, predicted = torch.max(class_predictions, 1)

    # Move the predictions back to the CPU, so we can print them out and visualize them
    predicted = predicted.to("cpu")

# Visualize the trained data
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, marker='x')
plt.xlabel("x1")
plt.xlabel("x2")
plt.show()

# Visualize the trained data AND the test data too
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, marker='.')
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, marker='x')
plt.xlabel("x1")
plt.xlabel("x2")
plt.show()
# You will see two clusters in this output. One in purple, one in yellow
# Every single "x" in one cluster is purple, and every single "x" in the other cluster is yellow
# What you dont see is a mix of colors in each cluster. If that were to happen, that means our algorithm didn't do so well
# Lower the "num_epochs" and you will see that the clusters become more mixed up, thanks to not reaching convergence or letting our loss run down


print(f'Time taken: {end - start:.4f} seconds')