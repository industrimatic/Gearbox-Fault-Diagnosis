import os
import pandas as pd
import numpy as np
import pywt

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem
from PySide6.QtCore import QThread, Signal
from main_window_ui import Ui_MainWindow
from datetime import datetime
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

# use $pyside6-uic '.\GUI\main_window.ui' -o '.\GUI\main_window_ui.py' to compile .ui file


def current_time():
    # use f-sting and [{current_time()}] to format console output
    return datetime.now().strftime("%H:%M:%S")


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.form = Ui_MainWindow()
        self.form.setupUi(self)

        self.bind()
        self.init_parameters()
        self.form.plainTextEdit.appendPlainText(f'[{current_time()}]欢迎使用智能齿轮箱故障诊断系统！')

    def bind(self):

        # 清空控制台
        self.form.pushButton_7.clicked.connect(self.clear_console)

        # 切换页面按钮绑定
        self.form.pushButton.clicked.connect(lambda: self.switch_widget(0))
        self.form.pushButton_2.clicked.connect(lambda: self.switch_widget(1))
        self.form.pushButton_3.clicked.connect(lambda: self.switch_widget(2))
        self.form.pushButton_4.clicked.connect(lambda: self.switch_widget(3))
        self.form.pushButton_6.clicked.connect(lambda: self.switch_widget(4))

        # 选择数据集
        self.form.pushButton_5.clicked.connect(self.choose_dataset_file)
        self.form.comboBox.currentTextChanged.connect(self.show_raw_data)

        # 更改参数
        self.form.spinBox.valueChanged.connect(self.update_parameters_batchsize)
        self.form.spinBox_2.valueChanged.connect(self.update_parameters_epoch)
        self.form.spinBox_3.valueChanged.connect(self.update_parameters_TrST)
        self.form.spinBox_4.valueChanged.connect(self.update_parameters_TrET)
        self.form.spinBox_5.valueChanged.connect(self.update_parameters_TrS)
        self.form.spinBox_6.valueChanged.connect(self.update_parameters_TeST)
        self.form.spinBox_7.valueChanged.connect(self.update_parameters_TeET)
        self.form.spinBox_8.valueChanged.connect(self.update_parameters_VST)
        self.form.spinBox_9.valueChanged.connect(self.update_parameters_VET)

        # 更新数据集样本数
        self.form.comboBox_2.currentTextChanged.connect(self.update_sample_num)

        # 展示变换后图像
        self.form.pushButton_8.clicked.connect(self.walvelet_transform)

    def init_parameters(self):

        self.train_start_time = self.form.spinBox_3.value()
        self.train_end_time = self.form.spinBox_4.value()
        self.train_stride = self.form.spinBox_5.value()
        self.test_start_time = self.form.spinBox_6.value()
        self.test_end_time = self.form.spinBox_7.value()
        self.val_start_time = self.form.spinBox_8.value()
        self.val_end_time = self.form.spinBox_9.value()

        self.batch_size = self.form.spinBox.value()
        self.epoch = self.form.spinBox_2.value()

        self.form.lineEdit.setText(str(self.train_stride))

    def clear_console(self):
        self.form.plainTextEdit.clear()
        self.form.plainTextEdit.appendPlainText(f'[{current_time()}]清空控制台')

    def switch_widget(self, page_index: int):

        if page_index == 0:
            self.form.stackedWidget.setCurrentIndex(0)
            self.form.plainTextEdit.appendPlainText(f'[{current_time()}]切换页面至“原始数据”')
            self.form.label_2.setText('功能区：原始数据')
        elif page_index == 1:
            self.form.stackedWidget.setCurrentIndex(1)
            self.form.plainTextEdit.appendPlainText(f'[{current_time()}]切换页面至“查看数据集”')
            self.form.label_2.setText('功能区：信号处理')
        elif page_index == 2:
            self.form.stackedWidget.setCurrentIndex(2)
            self.form.plainTextEdit.appendPlainText(f'[{current_time()}]切换页面至“模型训练”')
            self.form.label_2.setText('功能区：模型训练')
        elif page_index == 3:
            self.form.stackedWidget.setCurrentIndex(3)
            self.form.plainTextEdit.appendPlainText(f'[{current_time()}]切换页面至“模型工作”')
            self.form.label_2.setText('功能区：模型工作')
        elif page_index == 4:
            self.form.stackedWidget.setCurrentIndex(4)
            self.form.plainTextEdit.appendPlainText(f'[{current_time()}]切换页面至“参数设置”')
            self.form.label_2.setText('功能区：参数设置')

    def choose_dataset_file(self):  # 选择数据集

        self.dataset_path = QFileDialog.getExistingDirectory(self, "选择东齿轮箱数据集所在文件夹")
        self.form.label_3.setText(f'已选中数据集地址：{self.dataset_path}')
        self.form.plainTextEdit.appendPlainText(f'[{current_time()}]已选择数据集地址')
        self.data_chosen_dic = {
            'Health': False,
            'Chipped': False,
            'Miss': False,
            'Root': False,
            'Surface': False
        }
        # 先判断有无
        if os.path.exists(f'{self.dataset_path}/Health_30_2.csv'):
            self.data_chosen_dic['Health'] = True
        else:
            self.data_chosen_dic['Health'] = False

        if os.path.exists(f'{self.dataset_path}/Chipped_30_2.csv'):
            self.data_chosen_dic['Chipped'] = True
        else:
            self.data_chosen_dic['Chipped'] = False

        if os.path.exists(f'{self.dataset_path}/Miss_30_2.csv'):
            self.data_chosen_dic['Miss'] = True
        else:
            self.data_chosen_dic['Miss'] = False

        if os.path.exists(f'{self.dataset_path}/Root_30_2.csv'):
            self.data_chosen_dic['Root'] = True
        else:
            self.data_chosen_dic['Root'] = False

        if os.path.exists(f'{self.dataset_path}/Surface_30_2.csv'):
            self.data_chosen_dic['Surface'] = True
        else:
            self.data_chosen_dic['Surface'] = False

        # 再根据有无进行操作
        if self.data_chosen_dic['Health'] == True:
            self.form.checkBox.setChecked(True)
            self.form.comboBox.addItem('Health')
        else:
            self.form.plainTextEdit.appendPlainText(f'[{current_time()}]警告：未找到Health数据集')
            self.form.checkBox.setChecked(False)
            if self.form.comboBox.findText('Health') != -1:
                self.form.comboBox.removeItem(self.form.comboBox.findText('Health'))

        if self.data_chosen_dic['Chipped'] == True:
            self.form.checkBox_2.setChecked(True)
            self.form.comboBox.addItem('Chipped')
        else:
            self.form.plainTextEdit.appendPlainText(f'[{current_time()}]警告：未找到Chipped数据集')
            self.form.checkBox_2.setChecked(False)
            if self.form.comboBox.findText('Chipped') != -1:
                self.form.comboBox.removeItem(self.form.comboBox.findText('Chipped'))

        if self.data_chosen_dic['Miss'] == True:
            self.form.checkBox_3.setChecked(True)
            self.form.comboBox.addItem('Miss')
        else:
            self.form.plainTextEdit.appendPlainText(f'[{current_time()}]警告：未找到Miss数据集')
            self.form.checkBox_3.setChecked(False)
            if self.form.comboBox.findText('Miss') != -1:
                self.form.comboBox.removeItem(self.form.comboBox.findText('Miss'))

        if self.data_chosen_dic['Root'] == True:
            self.form.checkBox_4.setChecked(True)
            self.form.comboBox.addItem('Root')
        else:
            self.form.plainTextEdit.appendPlainText(f'[{current_time()}]警告：未找到Root数据集')
            self.form.checkBox_4.setChecked(False)
            if self.form.comboBox.findText('Root') != -1:
                self.form.comboBox.removeItem(self.form.comboBox.findText('Root'))

        if self.data_chosen_dic['Surface'] == True:
            self.form.checkBox_5.setChecked(True)
            self.form.comboBox.addItem('Surface')
        else:
            self.form.plainTextEdit.appendPlainText(f'[{current_time()}]警告：未找到Surface数据集')
            self.form.checkBox_5.setChecked(False)
            if self.form.comboBox.findText('Surface') != -1:
                self.form.comboBox.removeItem(self.form.comboBox.findText('Surface'))

        # 最后顺带刷新一下信号处理界面的combobox
        self.choose_trans_dataset()

    def show_raw_data(self, label: str):  # 展示原始数据
        if True not in self.data_chosen_dic.values():
            self.form.tableWidget.clear()
        else:
            file_path = f'{self.dataset_path}/{label}_30_2.csv'
            df = pd.read_csv(file_path, sep='\t', skiprows=16, header=None, nrows=128)
            df = df.dropna(axis=1, how='all')
            self.form.tableWidget.setRowCount(df.shape[0])
            self.form.tableWidget.setColumnCount(df.shape[1])

            for row in range(df.shape[0]):
                for col in range(df.shape[1]):
                    value = df.iat[row, col]
                    item = QTableWidgetItem(str(value))
                    self.form.tableWidget.setItem(row, col, item)

            self.form.plainTextEdit.appendPlainText(f'[{current_time()}]预览{label}数据集')

    def choose_trans_dataset(self):  # 选择信号处理数据集

        # 注意该方法在self.choose_dataset_file被调用，而不是用signal-slot调用
        for key in self.data_chosen_dic.keys():
            if self.data_chosen_dic[key] == True:
                self.form.comboBox_2.addItem(key)
            else:
                if self.form.comboBox_2.findText(key) == -1:
                    pass
                else:
                    self.form.comboBox_2.removeItem(self.form.comboBox_2.findText(key))

        if True not in self.data_chosen_dic.values():
            pass
        else:
            label = self.form.comboBox_2.currentText()
            file_path = f'{self.dataset_path}/{label}_30_2.csv'
            df = pd.read_csv(file_path, sep='\t', skiprows=16, header=None, usecols=[0])

            data_num = df.shape[0]
            sample_num = (data_num - 256) // self.train_stride + 1
            self.form.lineEdit_2.setText(str(data_num))
            self.form.lineEdit_3.setText(str(sample_num))

            self.form.spinBox_10.setMaximum(sample_num - 1)

    def update_sample_num(self, label: str):

        file_path = f'{self.dataset_path}/{label}_30_2.csv'
        df = pd.read_csv(file_path, sep='\t', skiprows=16, header=None, usecols=[0])

        data_num = df.shape[0]
        sample_num = (data_num - 256) // self.train_stride + 1
        self.form.lineEdit_2.setText(str(data_num))
        self.form.lineEdit_3.setText(str(sample_num))

        self.form.spinBox_10.setMaximum(sample_num - 1)

    def walvelet_transform(self):

        while self.form.verticalLayout_16.count():
            item = self.form.verticalLayout_16.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        channel = self.form.spinBox_11.value()
        start_data_num = 256 * self.form.spinBox_10.value()
        label = self.form.comboBox_2.currentText()
        file_path = f'{self.dataset_path}/{label}_30_2.csv'
        df = pd.read_csv(file_path, sep='\t', skiprows=16 + start_data_num, nrows=256)
        df = df.dropna(axis=1, how='all')

        datas = df.values
        datas = datas[:, channel]

        fs = 5120
        window_size = 256
        scales = np.geomspace(2, 256, num=256)
        wavename = 'cmor1.5-1.0'
        t_max = window_size / fs
        t_vector = np.linspace(0, t_max, window_size)

        self.fig = Figure(figsize=(12, 4), tight_layout=True)
        self.canvas = FigureCanvas(self.fig)
        self.form.verticalLayout_16.addWidget(self.canvas)

        ax1 = self.fig.add_subplot(121)
        ax2 = self.fig.add_subplot(122)

        ax1.plot(t_vector, datas, color='#1f77b4', linewidth=1.2)
        ax1.set_title("Time-Domain Signal")
        ax1.set_xlabel("Time (s)")
        ax1.set_ylabel("Amplitude")

        coeffs, _ = pywt.cwt(datas, scales, wavename)
        amp = np.abs(coeffs)

        ch_min, ch_max = amp.min(), amp.max()
        if ch_max > ch_min:
            img = (amp - ch_min) / (ch_max - ch_min)
        else:
            img = np.zeros_like(amp)

        fc = 1.0
        freqs = (fc * fs) / scales
        num_scales = len(scales)

        im = ax2.imshow(img, aspect='auto', cmap='magma', origin='upper',
                        extent=[0, t_max, num_scales - 1, 0])

        tick_indices = np.linspace(0, num_scales - 1, 6, dtype=int)
        ax2.set_yticks(tick_indices)
        ax2.set_yticklabels([f"{int(freqs[idx])}" for idx in tick_indices])

        ax2.set_title("CWT Spectrogram")
        ax2.set_xlabel("Time (s)")
        ax2.set_ylabel("Freq (Hz)")

        self.fig.colorbar(im, ax=ax2, pad=0.05, fraction=0.05)
        self.fig.suptitle(f'Label:{label},Sample:{self.form.spinBox_10.value()},Channel:{channel}')
        self.form.plainTextEdit.appendPlainText(f'[{current_time()}]生成图像：Label:{label},Sample:{self.form.spinBox_10.value()},Channel:{channel}')

    def update_parameters_batchsize(self, value: int):
        self.batch_size = value
        self.form.plainTextEdit.appendPlainText(f'[{current_time()}]已更新BATCH_SIZE={value}')

    def update_parameters_epoch(self, value: int):
        self.epoch = value
        self.form.plainTextEdit.appendPlainText(f'[{current_time()}]已更新EPOCH={value}')

    def update_parameters_TrST(self, value: int):
        self.train_start_time = value
        self.form.plainTextEdit.appendPlainText(f'[{current_time()}]已更新训练集开始时间={value}s')
        self.form.spinBox_3.setMaximum(self.form.spinBox_4.value() - 1)
        self.form.spinBox_4.setMinimum(self.form.spinBox_3.value() + 1)

    def update_parameters_TrET(self, value: int):
        self.train_end_time = value
        self.form.plainTextEdit.appendPlainText(f'[{current_time()}]已更新训练集结束时间={value}s')
        self.form.spinBox_3.setMaximum(self.form.spinBox_4.value() - 1)
        self.form.spinBox_4.setMinimum(self.form.spinBox_3.value() + 1)

    def update_parameters_TrS(self, value: int):
        self.train_stride = value
        self.form.plainTextEdit.appendPlainText(f'[{current_time()}]已更新训练集滑窗长度={value}')
        self.form.lineEdit.setText(str(self.train_stride))

    def update_parameters_TeST(self, value: int):
        self.test_start_time = value
        self.form.plainTextEdit.appendPlainText(f'[{current_time()}]已更新测试集开始时间={value}s')
        self.form.spinBox_6.setMaximum(self.form.spinBox_7.value() - 1)
        self.form.spinBox_7.setMinimum(self.form.spinBox_6.value() + 1)

    def update_parameters_TeET(self, value: int):
        self.test_end_time = value
        self.form.plainTextEdit.appendPlainText(f'[{current_time()}]已更新测试集结束时间={value}s')
        self.form.spinBox_6.setMaximum(self.form.spinBox_7.value() - 1)
        self.form.spinBox_7.setMinimum(self.form.spinBox_6.value() + 1)

    def update_parameters_VST(self, value: int):
        self.val_start_time = value
        self.form.plainTextEdit.appendPlainText(f'[{current_time()}]已更新验证集开始时间={value}s')
        self.form.spinBox_8.setMaximum(self.form.spinBox_9.value() - 1)
        self.form.spinBox_9.setMinimum(self.form.spinBox_8.value() + 1)

    def update_parameters_VET(self, value: int):
        self.val_end_time = value
        self.form.plainTextEdit.appendPlainText(f'[{current_time()}]已更新验证集结束时间={value}s')
        self.form.spinBox_8.setMaximum(self.form.spinBox_9.value() - 1)
        self.form.spinBox_9.setMinimum(self.form.spinBox_8.value() + 1)


if __name__ == '__main__':
    app = QApplication()

    # with open("GUI/style.css", "r", encoding="utf-8") as f:
    #     qss_style = f.read()
    #     app.setStyleSheet(qss_style)  # 全局应用样式

    window = MyWindow()
    window.show()
    app.exec()
