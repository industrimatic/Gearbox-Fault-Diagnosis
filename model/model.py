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

        self.channel_mixer = torch.nn.Sequential(
            torch.nn.Conv2d(8, 8, kernel_size=1, bias=False),
            torch.nn.BatchNorm2d(8),
            torch.nn.ReLU())

        self.extractor1 = torch.nn.Sequential(
            torch.nn.Conv2d(8, 16, kernel_size=3, padding=1, bias=False),
            torch.nn.BatchNorm2d(16),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(kernel_size=2),
            ResidualBlock(channels=16)
        )

        self.extractor2 = torch.nn.Sequential(
            torch.nn.Conv2d(16, 32, kernel_size=3, padding=1, bias=False),
            torch.nn.BatchNorm2d(32),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(kernel_size=2),
            ResidualBlock(channels=32)
        )

        self.extractor3 = torch.nn.Sequential(
            torch.nn.Conv2d(32, 48, kernel_size=3, padding=1, bias=False),
            torch.nn.BatchNorm2d(48),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(kernel_size=2),
            ResidualBlock(channels=48),
        )

        self.extractor4 = torch.nn.Sequential(
            torch.nn.Conv2d(48, 64, kernel_size=3, padding=1, bias=False),
            torch.nn.BatchNorm2d(64),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(kernel_size=2),
            ResidualBlock(channels=64)
        )

        # gap = Global Avg Pooling
        self.gap = torch.nn.AdaptiveAvgPool2d((1, 1))  # 64x1x1
        self.linear = torch.nn.Linear(in_features=64, out_features=5)

    def forward(self, x: torch.Tensor):
        in_size = x.shape[0]

        x = self.channel_mixer(x)

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
    test_model = ResNet()
    test_model.to(device=device)

    summary(test_model, input_size=(8, 256, 256))
