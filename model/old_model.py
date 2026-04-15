import torch


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


class ResNet(torch.nn.Module):
    def __init__(self):
        super().__init__()  # input = 8x224x224
        self.conv1 = torch.nn.Conv2d(8, 16, kernel_size=5)  # 16x224x224
        self.relu1 = torch.nn.ReLU()
        self.pool1 = torch.nn.MaxPool2d(kernel_size=2)  # 16x112x112
        self.res1 = ResidualBlock(channels=16)  # 16x112x112

        self.conv2 = torch.nn.Conv2d(16, 32, kernel_size=5)  # 32x108x108
        self.relu2 = torch.nn.ReLU()  # 32x108x108
        self.pool2 = torch.nn.MaxPool2d(kernel_size=2)  # 32x54x54
        self.res2 = ResidualBlock(channels=32)  # 32x54x54

        self.conv3 = torch.nn.Conv2d(32, 48, kernel_size=5)  # 48x50x50
        self.relu3 = torch.nn.ReLU()  # 48x50x50
        self.pool3 = torch.nn.MaxPool2d(kernel_size=2)  # 48x25x25
        self.res3 = ResidualBlock(channels=48)  # 48x25x25

        self.conv4 = torch.nn.Conv2d(48, 64, kernel_size=5)  # 64x21x21
        self.relu4 = torch.nn.ReLU()  # 64x21x21
        self.pool4 = torch.nn.MaxPool2d(kernel_size=3)  # 64x7x7
        self.res4 = ResidualBlock(channels=64)  # 64x7x7

        # gap = Global Avg Pooling
        self.gap = torch.nn.AdaptiveAvgPool2d((1, 1))  # 64x1x1
        self.linear = torch.nn.Linear(in_features=64, out_features=5)

    def forward(self, x: torch.Tensor):
        in_size = x.shape[0]

        x = self.conv1(x)
        x = self.relu1(x)
        x = self.pool1(x)
        x = self.res1(x)

        x = self.conv2(x)
        x = self.relu2(x)
        x = self.pool2(x)
        x = self.res2(x)

        x = self.conv3(x)
        x = self.relu3(x)
        x = self.pool3(x)
        x = self.res3(x)

        x = self.conv4(x)
        x = self.relu4(x)
        x = self.pool4(x)
        x = self.res4(x)

        x = self.gap(x)
        x = x.reshape(in_size, -1)
        x = self.linear(x)

        return x
