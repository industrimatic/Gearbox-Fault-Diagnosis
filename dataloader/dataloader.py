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


class SEUCWTDataset(Dataset):
    def __init__(self, file_path: str, label: int, start_time, end_time, fs: int = 5120,
                 window_size: int = 256, stride: int = 128, channels: list = None):
        self.label = label
        self.window_size = window_size
        self.stride = stride
        self.fs = fs
        self.scales = np.geomspace(2, 256, num=256)
        self.wavename = 'cmor1.5-1.0'  # 常用复莫莱小波
        self.channels = channels if channels is not None else list(range(8))

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


def get_seu_dataloaders(data_dir: str,
                        batch_size: int = 16,
                        num_workers: int = 0,
                        train_start_time: int = 0,
                        train_end_time: int = 10,
                        test_start_time: int = 10,
                        test_end_time: int = 15,
                        train_stride: int = 128,
                        test_stride: int = 256,
                        need_val_dataset: bool = False,
                        val_start_time: int = 15,
                        val_end_time: int = 20,
                        val_stride: int = 256
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
            val_data = SEUCWTDataset(file_path, label, start_time=val_start_time, end_time=val_end_time, stride=val_stride)
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


def plot_demo_sample(full_dataset, sample_idx=0):
    data_tensor, label = full_dataset[sample_idx]

    # 获取对应的 Dataset 实例以读取参数
    if hasattr(full_dataset, 'datasets'):
        dataset_idx = 0
        for i, size in enumerate(full_dataset.cumulative_sizes):
            if sample_idx < size:
                dataset_idx = i
                break
        subset = full_dataset.datasets[dataset_idx]
        inner_idx = sample_idx if dataset_idx == 0 else sample_idx - \
            full_dataset.cumulative_sizes[dataset_idx - 1]
    else:
        subset = full_dataset
        inner_idx = sample_idx

    fs = subset.fs
    window_size = subset.window_size
    fc = 1.0  # cmor1.5-1.0 的中心频率是 1.0

    t_max = window_size / fs
    # 计算频率刻度：f = (fc * fs) / s
    # 注意：subset.scales[0] 是最小尺度(2)，对应最高频；scales[-1] 是最大尺度(256)，对应最低频
    freqs = (fc * fs) / subset.scales
    num_scales = len(subset.scales)  # 获取真实的 Y 轴分辨率，这里为 256

    start = inner_idx * subset.stride
    end = start + subset.window_size
    raw_sig_segment = subset.raw_data[start:end, :]

    fig, axes = plt.subplots(8, 2, figsize=(14, 20), constrained_layout=True)
    fault_map = {0: "Health", 1: "Chipped", 2: "Miss", 3: "Root", 4: "Surface"}
    state_name = fault_map.get(label.item(), "Unknown")

    fig.suptitle(f'Sample ID: {sample_idx} | State: {state_name}\n(CWT)', fontsize=18)

    for i in range(8):
        # --- 左侧：时域图 ---
        # 使用真实时间 t 绘图
        t_vector = np.linspace(0, t_max, window_size)
        axes[i, 0].plot(t_vector, raw_sig_segment[:, i],
                        color='#1f77b4', linewidth=0.8)
        axes[i, 0].set_ylabel(f'CH {i+1}\nAmp', fontsize=10, fontweight='bold')
        if i == 0:
            axes[i, 0].set_title("Time-Domain Signal (Raw)", fontsize=14)
        if i == 7:
            axes[i, 0].set_xlabel("Time (s)", fontsize=10, fontweight='bold')
        else:
            axes[i, 0].set_xticks([])

        # --- 右侧：时频图 ---
        cwt_img = data_tensor[i].numpy()

        # origin='upper'图像顶端为 y=0（对应最高频），底端为 y=num_scales-1（对应最低频）
        im = axes[i, 1].imshow(cwt_img, aspect='auto', cmap='magma', origin='upper',
                               extent=[0, t_max, num_scales - 1, 0])

        # 刻度索引也必须基于 num_scales-1 计算，保证不会超出 freqs 数组范围
        tick_indices = np.linspace(0, num_scales - 1, 6, dtype=int)
        axes[i, 1].set_yticks(tick_indices)

        # 因为顶端是 0，底端是 223，直接使用 idx 提取频率即可，不需要再倒序相减
        axes[i, 1].set_yticklabels([f"{int(freqs[idx])}" for idx in tick_indices])

        axes[i, 1].set_ylabel("Freq (Hz)", fontsize=10, fontweight='bold')
        if i == 0:
            axes[i, 1].set_title("CWT Spectrogram", fontsize=14)
        if i == 7:
            axes[i, 1].set_xlabel("Time (s)", fontsize=10, fontweight='bold')
        else:
            axes[i, 1].set_xticks([])

    cbar = fig.colorbar(im, ax=axes[:, 1], pad=0.08, fraction=0.03)
    cbar.set_label('Normalized Amplitude', fontweight='bold')
    cbar.ax.yaxis.set_label_position('left')

    save_name = f'debug_sample_{sample_idx}_label_{label.item()}.png'
    plt.savefig(save_name, dpi=300, bbox_inches='tight')
    plt.close(fig)  # 增加 close 防止批量画图时内存泄漏


if __name__ == "__main__":

    DATA_PATH = './dataset/gearset/'

    train_loader, test_loader = get_seu_dataloaders(DATA_PATH, batch_size=16)

    plot_demo_sample(train_loader.dataset, sample_idx=0)
    plot_demo_sample(train_loader.dataset, sample_idx=500)
    plot_demo_sample(train_loader.dataset, sample_idx=1000)
    plot_demo_sample(train_loader.dataset, sample_idx=1500)
    plot_demo_sample(train_loader.dataset, sample_idx=1800)
