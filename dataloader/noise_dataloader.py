import os
import pandas as pd
import numpy as np
import pywt
import torch
import matplotlib.pyplot as plt
from torch.utils.data import Dataset, DataLoader, ConcatDataset

"""
The dataset has samples of about 200 seconds 

STATUS      LABEL
Health      0
Chipped     1
Miss        2
Root        3
Surface     4
"""


def add_noise(signal, snr_db):

    if snr_db is None:
        return signal

    signal_power = np.mean(signal ** 2)
    noise_power = signal_power / (10 ** (snr_db / 10))
    noise = np.random.normal(0, np.sqrt(noise_power), size=signal.shape)
    noisy_signal = signal + noise

    return noisy_signal


class SEUCWTDataset(Dataset):
    def __init__(self, file_path: str, label: int, start_time, end_time, fs: int = 5120,
                 window_size: int = 256, stride: int = 128, channels: list = None, snr: float = None):
        self.label = label
        self.window_size = window_size
        self.stride = stride
        self.fs = fs
        self.scales = np.geomspace(2, 256, num=256)
        self.wavename = 'cmor1.5-1.0'  # 常用复莫莱小波
        self.channels = channels if channels is not None else list(range(8))
        self.snr = snr

        # 读取数据：SEU数据集使用 '\t' 分隔，前16行为表头
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"文件未找到: {file_path}")

        df = pd.read_csv(file_path, sep='\t', skiprows=16, header=None)

        start_idx = int(start_time * fs)
        end_idx = int(end_time * fs)
        # 获取指定通道的数据
        self.raw_data = df.iloc[start_idx:end_idx, self.channels].values
        # 计算总样本数
        self.num_samples = (len(self.raw_data) - window_size) // stride + 1

    def __len__(self):
        return self.num_samples

    def __getitem__(self, idx):
        start = idx * self.stride
        end = start + self.window_size
        sig_segment = self.raw_data[start:end, :]  # shape: (224, num_channels)
        sig_segment = add_noise(sig_segment, self.snr)

        multi_channel_img = []
        for i in range(sig_segment.shape[1]):
            coeffs, _ = pywt.cwt(sig_segment[:, i], self.scales, self.wavename)
            amp = np.abs(coeffs)

            ch_min, ch_max = amp.min(), amp.max()
            if ch_max > ch_min:
                img = (amp - ch_min) / (ch_max - ch_min)
            else:
                img = np.zeros_like(amp)

            multi_channel_img.append(img)

        # 堆叠通道并转换为 Tensor (C, H, W)
        data_tensor = torch.tensor(np.stack(multi_channel_img, axis=0), dtype=torch.float32)
        label_tensor = torch.tensor(self.label, dtype=torch.long)

        return data_tensor, label_tensor


def get_noisy_seu_dataloaders(
        data_dir: str, batch_size: int = 16, num_workers: int = 0,
        train_start_time: int = 0, train_end_time: int = 10, test_start_time: int = 10,
        test_end_time: int = 15, train_stride: int = 128, test_stride: int = 256,
        need_val_dataset: bool = False, val_start_time: int = 15, val_end_time: int = 20,
        val_stride: int = 256, snr: float = None
):
    file_info = [
        ('Health_30_2.csv', 0),
        ('Chipped_30_2.csv', 1),
        ('Miss_30_2.csv', 2),
        ('Root_30_2.csv', 3),
        ('Surface_30_2.csv', 4)
    ]

    train_subsets = []
    test_subsets = []

    if need_val_dataset == True:
        val_subsets = []

    for file_name, label in file_info:
        file_path = os.path.join(data_dir, file_name)
        if not os.path.exists(file_path):
            print(f"警告: 找不到文件 {file_path}，已跳过")
            continue

        print(f"正在加载数据: {file_name} (标签: {label})")

        # 训练集: 前10秒, 步长较小增加样本
        train_data = SEUCWTDataset(file_path, label, start_time=train_start_time, end_time=train_end_time, stride=train_stride)
        train_subsets.append(train_data)

        # 测试集: 10-15秒, 步进等于窗口大小避免重叠
        test_data = SEUCWTDataset(file_path, label, start_time=test_start_time, end_time=test_end_time, stride=test_stride)
        test_subsets.append(test_data)

        if need_val_dataset == True:
            val_data = SEUCWTDataset(file_path, label, start_time=val_start_time, end_time=val_end_time, stride=val_stride, snr=snr)
            val_subsets.append(val_data)

    full_train_ds = ConcatDataset(train_subsets)
    full_test_ds = ConcatDataset(test_subsets)

    if need_val_dataset == True:
        full_val_ds = ConcatDataset(val_subsets)

    if need_val_dataset == False:
        train_loader = DataLoader(full_train_ds, batch_size=batch_size, shuffle=True, num_workers=num_workers)
        test_loader = DataLoader(full_test_ds, batch_size=batch_size, shuffle=False, num_workers=num_workers)

        return train_loader, test_loader
    else:
        train_loader = DataLoader(full_train_ds, batch_size=batch_size, shuffle=True, num_workers=num_workers)
        test_loader = DataLoader(full_test_ds, batch_size=batch_size, shuffle=False, num_workers=num_workers)
        val_loader = DataLoader(full_val_ds, batch_size=batch_size, shuffle=True, num_workers=num_workers)

        return train_loader, test_loader, val_loader


if __name__ == "__main__":

    DATA_PATH = './dataset/gearset/'
