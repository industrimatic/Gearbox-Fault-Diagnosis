import torch
import numpy as np
import matplotlib.pyplot as plt
import os
from time import time
from dataloader.dataloader import get_seu_dataloaders
from model.model import ResNet

DATA_PATH = './dataset/gearset/'
BATCH_SIZE = 16
NUM_WORKERS = 4
EPOCH = 10
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = ResNet()
model.to(device=DEVICE)

criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

"""
！！！训练前务必修改模型保存的权重名称！！！
！！！否则之前训练好的老文件会被覆盖！！！
"""


def train(epoch, train_loader):
    model.train()
    batch_num = len(train_loader)
    running_loss = 0.0

    for batch_index, (x_data, y_data) in enumerate(train_loader):
        x_data, y_data = x_data.to(DEVICE), y_data.to(DEVICE)
        # forward
        y_pred = model(x_data)
        loss = criterion(y_pred, y_data)
        # backward
        optimizer.zero_grad()
        loss.backward()
        # update
        optimizer.step()

        running_loss += loss.item()
        if batch_index % 20 == 19:
            print(f'|epoch:{epoch+1}|All Iteration:{batch_num} Now:{batch_index+1}|loss:{running_loss/20}')
            running_loss = 0.0


def test(test_loader):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for (x_data, y_data) in test_loader:
            x_data, y_data = x_data.to(DEVICE), y_data.to(DEVICE)
            y_pred = model(x_data)
            _, predicted = torch.max(y_pred.data, dim=1)
            total += y_data.shape[0]
            correct += (predicted == y_data).sum().item()

    print(f'accuracy:{100*correct/total:.3f}%')
    return 100 * correct / total


def plot_accuracy_figure(show_accu: list):

    x = np.arange(0, len(show_accu), 1)

    plt.plot(x, show_accu)
    plt.title("Accuracy Figure")
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy Rate (%)")
    plt.tight_layout()

    base_name = 'AccuracyFigure'
    ext = '.png'
    filename = f"{base_name}{ext}"

    counter = 1
    while os.path.exists(filename):
        filename = f"{base_name}_{counter}{ext}"
        counter += 1

    plt.savefig(filename, bbox_inches='tight')
    print(f"图表已成功保存为: {filename}")

    plt.show()


if __name__ == "__main__":

    start_time = time()

    train_loader, test_loader = get_seu_dataloaders(DATA_PATH, BATCH_SIZE, NUM_WORKERS)
    print(f"数据加载完成，总 Batch 数：{len(train_loader)}")

    show_accu = []

    for epoch in range(EPOCH):
        train(epoch, train_loader)
        show_accu.append(test(test_loader))
        print(f'Epoch:{epoch+1} 完毕|已耗时:{(time()-start_time):.2f}s')
        if show_accu[-1] == max(show_accu):
            torch.save(model.state_dict(), f'./weight/model1_epoch{EPOCH}.pth')
            print("已保存更好的模型")
        else:
            print("该epoch并非最佳模型")

    print(f'最好模型准确率为： {max(show_accu):.3f}')

    plot_accuracy_figure(show_accu=show_accu)
