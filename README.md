# 齿轮箱故障诊断

<p align="center">
  <img alt="Stars" src="https://img.shields.io/github/stars/industrimatic/Gearbox-Fault-Diagnosis?style=for-the-badge">
  &nbsp;&nbsp;
  <img alt="Last commit" src="https://img.shields.io/github/last-commit/industrimatic/Gearbox-Fault-Diagnosis?style=for-the-badge">
  &nbsp;&nbsp;
    <img alt="License" src="https://img.shields.io/github/license/industrimatic/Gearbox-Fault-Diagnosis?style=for-the-badge">
  &nbsp;&nbsp;
</p>

本项目为一个齿轮箱故障诊断的项目

## 基本思想

- 使用东南大学齿轮箱公开数据集
- 使用小波变换对原始数据进行处理
- 使用一个受ResNet启发的网络
- 使用PySide6进行页面开发

## 东南大学齿轮箱数据集

- 采样频率是5120Hz
- 第1列电机振动信号
- 第2、3、4列分别对应行星齿轮x，y和z三个方向的振动信号
- 第5列对应着电机扭矩
- 第6、7、8列分别对应着减速器x，y和z三个方向的振动信号

### 齿轮箱数据集参考文献

- 邵思羽.基于深度学习的旋转机械故障诊断方法研究[D].东南大学,2019.DOI:10.27014/d.cnki.gdnau.2019.000303.
- Shao S, McAleer S, Yan R, et al. Highly accurate machine fault diagnosis using deep transfer learning[J]. IEEE transactions on industrial informatics, 2018, 15(4): 2446-2455.
- 陈超.基于迁移学习的旋转机械故障诊断方法研究[D].东南大学,2020.DOI:10.27014/d.cnki.gdnau.2020.003075.
- [东南大学齿轮箱数据集SUFD技术文档](https://wenku.baidu.com/view/4ead94f8730bf78a6529647d27284b73f24236dc.html?_wkts_=1774356261785&bdQuery=%E4%B8%9C%E5%8D%97%E5%A4%A7%E5%AD%A6%E9%BD%BF%E8%BD%AE%E7%AE%B1%E6%95%B0%E6%8D%AE%E9%9B%86)
- [基于小波时频图和2D-CNN的齿轮箱故障检测](https://blog.csdn.net/m0_67853969/article/details/131205641)
- [GitHub公开故障诊断数据集](https://github.com/hustcxl/Rotating-machine-fault-data-set)
- [东南大学齿轮箱故障数据集](https://github.com/hustcxl/Rotating-machine-fault-data-set)

## 使用本程序

### 创建虚拟环境

使用conda创建一个用于存放本项目的环境，本项目的python版本为3.8.20

```shell
conda create -n pytorch python==3.8.20
conda activate pytorch
```

### 使用conda安装的包

安装`pytorch`

```shell
# CUDA 10.2
conda install pytorch==1.10.1 torchvision==0.11.2 torchaudio==0.10.1 cudatoolkit=10.2 -c pytorch

# CUDA 11.3
conda install pytorch==1.10.1 torchvision==0.11.2 torchaudio==0.10.1 cudatoolkit=11.3 -c pytorch -c conda-forge

# CPU Only
conda install pytorch==1.10.1 torchvision==0.11.2 torchaudio==0.10.1 cpuonly -c pytorch
```

安装`matplotlib`

```shell
conda install matplotlib
```

安装`pandas`

```shell
conda install pandas
```

安装`seaborn`

```shell
conda install seaborn
```

### 使用pip安装的包

安装`pywt`

```shell
pip install PyWavelets
```

安装`sklearn`

```shell
pip install scikit-learn
```

安装`pyside6`

```shell
pip install pyside6
```

安装`torchsummary`

```shell
pip install torchsummary
```

### 打开主窗口

```shell
conda activate pytorch
python ./GUI/main_window.py
```
