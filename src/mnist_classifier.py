from torchvision import datasets
from torchvision.transforms import ToTensor

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

print("Training images:", len(train_data))
print("Test images:", len(test_data))

image, label = train_data[0]

print("Image shape:", image.shape)
print("Label:", label)