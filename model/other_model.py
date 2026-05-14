import torch
import torch.nn as nn
import torchvision.models as models
from torchsummary import summary


# VGG-16
def get_vgg():

    vgg16 = models.vgg16_bn(pretrained=False)
    vgg16.features[0] = nn.Conv2d(in_channels=8, out_channels=64, kernel_size=3, stride=1, padding=1)
    vgg16.classifier[6] = nn.Linear(in_features=4096, out_features=5)
    return vgg16


# ResNet-18
def get_resnet():

    resnet18 = models.resnet18(pretrained=False)
    resnet18.conv1 = nn.Conv2d(in_channels=8, out_channels=64, kernel_size=7, stride=2, padding=3, bias=False)
    in_features = resnet18.fc.in_features
    resnet18.fc = nn.Linear(in_features, 5)
    return resnet18


# AlexNet
def get_alexnet():
    alexnet = models.alexnet(pretrained=False)
    alexnet.features[0] = nn.Conv2d(in_channels=8, out_channels=64, kernel_size=11, stride=4, padding=2)
    alexnet.classifier[6] = nn.Linear(in_features=4096, out_features=5)
    return alexnet


# GoogleNet
def get_googlenet():

    googlenet = models.googlenet(pretrained=False, aux_logits=False, init_weights=True)
    googlenet.conv1.conv = nn.Conv2d(in_channels=8, out_channels=64, kernel_size=7, stride=2, padding=3, bias=False)
    googlenet.fc = nn.Linear(in_features=1024, out_features=5)
    return googlenet


class ResidualBlock(torch.nn.Module):
    def __init__(self, channels: int):
        super().__init__()
        self.channels = channels
        self.conv1 = torch.nn.Conv2d(channels, channels, kernel_size=3, padding=1, bias=False)
        self.bn1 = torch.nn.BatchNorm2d(channels)
        self.conv2 = torch.nn.Conv2d(channels, channels, kernel_size=3, padding=1, bias=False)
        self.bn2 = torch.nn.BatchNorm2d(channels)
        self.relu = torch.nn.ReLU()

    def forward(self, x):
        y = self.relu(self.bn1(self.conv1(x)))
        y = self.bn2(self.conv2(y))

        return self.relu(x + y)


# 对该网络进行消融实验

class BaseModel(torch.nn.Module):

    def __init__(self):
        super().__init__()  # input = 8x256x256

        self.extractor1 = torch.nn.Sequential(
            torch.nn.Conv2d(8, 16, kernel_size=3, padding=1, bias=False),
            torch.nn.BatchNorm2d(16),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(kernel_size=2),
            ResidualBlock(channels=16)  # output = 16x128x128
        )

        self.extractor2 = torch.nn.Sequential(
            torch.nn.Conv2d(16, 32, kernel_size=3, padding=1, bias=False),
            torch.nn.BatchNorm2d(32),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(kernel_size=2),
            ResidualBlock(channels=32)  # output = 32x64x64
        )

        self.extractor3 = torch.nn.Sequential(
            torch.nn.Conv2d(32, 48, kernel_size=3, padding=1, bias=False),
            torch.nn.BatchNorm2d(48),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(kernel_size=2),
            ResidualBlock(channels=48),  # output = 48x32x32
        )

        self.extractor4 = torch.nn.Sequential(
            torch.nn.Conv2d(48, 64, kernel_size=3, padding=1, bias=False),
            torch.nn.BatchNorm2d(64),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(kernel_size=2),
            ResidualBlock(channels=64)  # output = 64x16x16
        )

        # gap = Global Avg Pooling
        self.gap = torch.nn.AdaptiveAvgPool2d((1, 1))  # 64x1x1
        self.linear = torch.nn.Linear(in_features=64, out_features=5)

    def forward(self, x: torch.Tensor):
        in_size = x.shape[0]

        x = self.extractor1(x)
        x = self.extractor2(x)
        x = self.extractor3(x)
        x = self.extractor4(x)

        x = self.gap(x)
        x = x.reshape(in_size, -1)
        x = self.linear(x)

        return x


if __name__ == "__main__":

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    test_model = BaseModel()
    test_model.to(device=device)
    summary(test_model, input_size=(8, 256, 256))
