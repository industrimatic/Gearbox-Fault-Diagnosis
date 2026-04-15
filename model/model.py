import torch
from torchsummary import summary

"""
STATUS      LABEL
Health      0
Chipped     1
Miss        2
Root        3
Surface     4
"""


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


class ResNet(torch.nn.Module):

    def __init__(self):
        super().__init__()  # input = 8x256x256

        self.channel_mixer = torch.nn.Conv2d(8, 8, kernel_size=1, bias=False)  # 8x256x256
        self.mixer_bn = torch.nn.BatchNorm2d(8)
        self.mixer_relu = torch.nn.ReLU()

        self.conv1 = torch.nn.Conv2d(8, 16, kernel_size=3, padding=1, bias=False)  # 16x256x256
        self.bn1 = torch.nn.BatchNorm2d(16)
        self.relu1 = torch.nn.ReLU()
        self.pool1 = torch.nn.MaxPool2d(kernel_size=2)  # 16x128x128
        self.res1 = ResidualBlock(channels=16)

        self.conv2 = torch.nn.Conv2d(16, 32, kernel_size=3, padding=1, bias=False)  # 32x128x128
        self.bn2 = torch.nn.BatchNorm2d(32)
        self.relu2 = torch.nn.ReLU()
        self.pool2 = torch.nn.MaxPool2d(kernel_size=2)  # 32x64x64
        self.res2 = ResidualBlock(channels=32)

        self.conv3 = torch.nn.Conv2d(32, 48, kernel_size=3, padding=1, bias=False)  # 48x64x64
        self.bn3 = torch.nn.BatchNorm2d(48)
        self.relu3 = torch.nn.ReLU()
        self.pool3 = torch.nn.MaxPool2d(kernel_size=2)  # 48x32x32
        self.res3 = ResidualBlock(channels=48)

        self.conv4 = torch.nn.Conv2d(48, 64, kernel_size=3, padding=1, bias=False)  # 64x32x32
        self.bn4 = torch.nn.BatchNorm2d(64)
        self.relu4 = torch.nn.ReLU()
        self.pool4 = torch.nn.MaxPool2d(kernel_size=2)  # 64x16x16
        self.res4 = ResidualBlock(channels=64)

        # gap = Global Avg Pooling
        self.gap = torch.nn.AdaptiveAvgPool2d((1, 1))  # 64x1x1
        self.linear = torch.nn.Linear(in_features=64, out_features=5)

    def forward(self, x: torch.Tensor):
        in_size = x.shape[0]

        x = self.channel_mixer(x)
        x = self.mixer_bn(x)
        x = self.mixer_relu(x)

        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu1(x)
        x = self.pool1(x)
        x = self.res1(x)

        x = self.conv2(x)
        x = self.bn2(x)
        x = self.relu2(x)
        x = self.pool2(x)
        x = self.res2(x)

        x = self.conv3(x)
        x = self.bn3(x)
        x = self.relu3(x)
        x = self.pool3(x)
        x = self.res3(x)

        x = self.conv4(x)
        x = self.bn4(x)
        x = self.relu4(x)
        x = self.pool4(x)
        x = self.res4(x)

        x = self.gap(x)
        x = x.reshape(in_size, -1)
        x = self.linear(x)

        return x


if __name__ == "__main__":

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    test_model = ResNet()
    test_model.to(device=device)

    summary(test_model, input_size=(8, 256, 256))
