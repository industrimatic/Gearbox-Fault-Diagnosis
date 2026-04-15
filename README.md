# 齿轮箱故障诊断

This README is written by Qinghan You from USTB 2026 and used for recording purpose

## 数据集
[GitHub公开故障诊断数据集](https://github.com/hustcxl/Rotating-machine-fault-data-set)
[东南大学齿轮箱故障数据集](https://github.com/hustcxl/Rotating-machine-fault-data-set)

东南大学齿轮箱故障数据集由东南大学严如强教授团队提供，本数据集模拟了两种工况下的5种轴承运行状态和5种齿轮运行状态。两种工况分别为转速20Hz (1200rpm) -无负载0V (0Nm)与转速 30Hz (1800rpm) -有负载 2V (7.32Nm)

**参考文献**
- [1]邵思羽.基于深度学习的旋转机械故障诊断方法研究[D].东南大学,2019.DOI:10.27014/d.cnki.gdnau.2019.000303.
- [2]Shao S, McAleer S, Yan R, et al. Highly accurate machine fault diagnosis using deep transfer learning[J]. IEEE transactions on industrial informatics, 2018, 15(4): 2446-2455.
- [3]陈超.基于迁移学习的旋转机械故障诊断方法研究[D].东南大学,2020.DOI:10.27014/d.cnki.gdnau.2020.003075.
- [东南大学齿轮箱数据集SUFD技术文档](https://wenku.baidu.com/view/4ead94f8730bf78a6529647d27284b73f24236dc.html?_wkts_=1774356261785&bdQuery=%E4%B8%9C%E5%8D%97%E5%A4%A7%E5%AD%A6%E9%BD%BF%E8%BD%AE%E7%AE%B1%E6%95%B0%E6%8D%AE%E9%9B%86)
- [基于小波时频图和2D-CNN的齿轮箱故障检测](https://blog.csdn.net/m0_67853969/article/details/131205641)

邵思羽的网络基于VGG16，使用了迁移学习方法和GAN方法

东南大学GearSet dataset: 采样频率是5120Hz。第1列电机振动信号；第2、3、4列分别对应行星齿轮x，y和z三个方向的振动信号；第5列对应着电机扭矩；第6、7、8列分别对应着减速器x，y和z三个方向的振动信号

