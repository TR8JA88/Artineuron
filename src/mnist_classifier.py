import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

# 1. Load data
train_data = datasets.MNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor()
)

test_data = datasets.MNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor()
)

# 2. Prepare batches
train_loader = DataLoader(
    train_data,
    batch_size=64,
    shuffle=True
)

test_loader = DataLoader(
    test_data,
    batch_size=64,
    shuffle=False
)

# 3. Define the neural network
class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()

        self.flatten = nn.Flatten()

        self.layers = nn.Sequential(
            nn.Linear(28 * 28, 128),
            nn.ReLU(),
            nn.Linear(128, 10)
        )

    def forward(self, x):
        x = self.flatten(x)
        return self.layers(x)


# 4. Create the model
model = NeuralNetwork()
loss_function = nn.CrossEntropyLoss()

optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.1
)

epochs = 5

for epoch in range(epochs):

    for images, labels in train_loader:

        # Forward pass
        predictions = model(images)

        # Calculate loss
        loss = loss_function(predictions, labels)

        # Calculate gradients
        optimizer.zero_grad()
        loss.backward()

        # Update weights
        optimizer.step()

    print(f"Epoch {epoch + 1}: loss = {loss.item():.4f}")

print(model)