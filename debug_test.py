import pandas as pd
import numpy as np
import pywt
import torch
import matplotlib.pyplot as plt
from time import time
from model.model import ResNet
from model.other_model import get_googlenet, get_alexnet, get_resnet, get_vgg
from model.without_resconnect import ResNetWithoutConnection

WIGHT_PATH = r'weight\2026_4_23\epoch20_9_ac100.pth'

if __name__ == '__main__':

    model = ResNet()
    model.eval()
    model.load_state_dict(torch.load(WIGHT_PATH))
    wavename = 'cmor1.5-1.0'
    scales = np.geomspace(2, 256, num=256)

    label_list = ['Health', 'Chipped', 'Miss', 'Root', 'Surface']

    df = pd.read_csv(r'dataset\gearset\Health_30_2.csv', sep='\t', skiprows=16, header=None)
    serial_datas = df.dropna(axis=1, how='all').values[0:256, :]

    time_list = []

    for i in range(100):
        start_time = time()

        img_list = []
        for i in range(8):

            coeffs, _ = pywt.cwt(serial_datas[:, i], scales, wavename)
            amp = np.abs(coeffs)

            ch_min, ch_max = amp.min(), amp.max()
            if ch_max > ch_min:
                img = (amp - ch_min) / (ch_max - ch_min)
            else:
                img = np.zeros_like(amp)

            img_list.append(img)

        data_tensor = torch.tensor(np.stack(img_list, axis=0), dtype=torch.float32)
        data_tensor = data_tensor.reshape(1, 8, 256, 256)

        with torch.no_grad():
            predicted_label = model(data_tensor)
            _, result = torch.max(predicted_label, axis=1)

        cost_time = time() - start_time
        time_list.append(cost_time)

    mean_time = np.mean(time_list)
    median_time = np.median(time_list)

    # 创建画布，包含左右两个子图
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # --- 图 1：耗时折线图 ---
    iterations = np.arange(1, 101)
    ax1.plot(iterations, time_list, marker='o', linestyle='-', color='#1f77b4', markersize=4, alpha=0.8)
    ax1.axhline(mean_time, color='r', linestyle='--', label=f'Mean: {mean_time:.4f}s')
    ax1.set_title('Inference Time per Iteration', fontsize=14)
    ax1.set_xlabel('Iteration', fontsize=12)
    ax1.set_ylabel('Time (seconds)', fontsize=12)
    ax1.grid(True, linestyle='--', alpha=0.6)
    ax1.legend()

    # --- 图 2：耗时分布直方图 ---
    ax2.hist(time_list, bins=15, color='#2ca02c', edgecolor='black', alpha=0.7)
    ax2.axvline(mean_time, color='r', linestyle='--', label=f'Mean: {mean_time:.4f}s')
    ax2.axvline(median_time, color='b', linestyle='-.', label=f'Median: {median_time:.4f}s')
    ax2.set_title('Distribution of Inference Times', fontsize=14)
    ax2.set_xlabel('Time (seconds)', fontsize=12)
    ax2.set_ylabel('Frequency', fontsize=12)
    ax2.grid(axis='y', linestyle='--', alpha=0.6)
    ax2.legend()

    # 调整整体布局
    plt.suptitle('Model Inference Performance Analysis (100 Iterations)', fontsize=16, y=1.05)
    plt.tight_layout()
    plt.show()
