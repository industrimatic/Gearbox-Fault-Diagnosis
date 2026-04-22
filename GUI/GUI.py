import sys
import time
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QHBoxLayout, QPushButton, QLabel, QProgressBar,
                               QFileDialog, QTextEdit, QGroupBox, QFrame)
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QFont, QIcon


class TrainingThread(QThread):
    progress_update = Signal(int)
    log_update = Signal(str)
    finished_signal = Signal()

    def run(self):
        self.log_update.emit("初始化模型参数...")
        time.sleep(1)  # 模拟加载时间

        epochs = 100
        for i in range(1, epochs + 1):

            time.sleep(0.05)  # 模拟每个 epoch 的训练耗时

            # 更新进度条
            self.progress_update.emit(i)

            # 模拟输出训练日志 (每 10 个 epoch 打印一次 loss)
            if i % 10 == 0:
                fake_loss = 1.0 / i
                self.log_update.emit(f"Epoch [{i}/{epochs}] - Loss: {fake_loss:.4f} - Accuracy: {0.5 + i*0.004:.2f}")

        self.log_update.emit("训练完成！模型已保存。")
        self.finished_signal.emit()


class FaultDiagnosisUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("智能故障诊断系统 - 毕业设计")
        self.resize(800, 600)
        self.dataset_path = ""
        self.init_ui()
        self.apply_stylesheet()

    def init_ui(self):

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        title_label = QLabel("基于深度学习的设备故障诊断系统")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setObjectName("titleLabel")  # 用于 QSS 样式绑定
        main_layout.addWidget(title_label)

        data_group = QGroupBox("1. 数据准备")
        data_layout = QHBoxLayout(data_group)

        self.btn_import = QPushButton("导入数据集")
        self.btn_import.clicked.connect(self.import_dataset)
        self.lbl_path = QLabel("尚未选择任何数据集...")
        self.lbl_path.setStyleSheet("color: #666666; font-style: italic;")

        data_layout.addWidget(self.btn_import)
        data_layout.addWidget(self.lbl_path, stretch=1)
        main_layout.addWidget(data_group)

        train_group = QGroupBox("2. 模型训练")
        train_layout = QVBoxLayout(train_group)

        control_layout = QHBoxLayout()
        self.btn_train = QPushButton("开始训练")
        self.btn_train.clicked.connect(self.start_training)

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(True)

        control_layout.addWidget(self.btn_train)
        control_layout.addWidget(self.progress_bar, stretch=1)
        train_layout.addLayout(control_layout)

        self.log_box = QTextEdit()
        self.log_box.setReadOnly(True)
        self.log_box.setPlaceholderText("训练日志将在此处显示...")
        train_layout.addWidget(self.log_box)

        main_layout.addWidget(train_group)

        work_group = QGroupBox("3. 故障诊断推理")
        work_layout = QHBoxLayout(work_group)

        self.btn_diagnose = QPushButton("加载测试数据并诊断")
        self.btn_diagnose.clicked.connect(self.run_diagnosis)

        self.lbl_result = QLabel("诊断结果：等待执行...")
        self.lbl_result.setObjectName("resultLabel")
        self.lbl_result.setAlignment(Qt.AlignmentFlag.AlignCenter)

        work_layout.addWidget(self.btn_diagnose)
        work_layout.addWidget(self.lbl_result, stretch=1)

        main_layout.addWidget(work_group)

    def apply_stylesheet(self):
        """应用现代扁平化 QSS 样式"""
        style = """
            QMainWindow {
                background-color: #F5F7FA;
            }
            QGroupBox {
                font-size: 15px;
                font-weight: bold;
                border: 1px solid #DCDFE6;
                border-radius: 8px;
                margin-top: 1.5ex;
                background-color: white;
                padding: 15px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top left;
                left: 15px;
                color: #2C3E50;
            }
            QPushButton {
                background-color: #409EFF;
                color: white;
                border-radius: 5px;
                padding: 8px 16px;
                font-weight: bold;
                border: none;
            }
            QPushButton:hover {
                background-color: #66B1FF;
            }
            QPushButton:disabled {
                background-color: #A0CFFF;
                color: #FFFFFF;
            }
            QProgressBar {
                border: 1px solid #E4E7ED;
                border-radius: 5px;
                text-align: center;
                background-color: #EBEEF5;
                color: #303133;
                font-weight: bold;
            }
            QProgressBar::chunk {
                background-color: #67C23A;
                border-radius: 4px;
            }
            QTextEdit {
                border: 1px solid #DCDFE6;
                border-radius: 5px;
                background-color: #F8F9FA;
                color: #606266;
                font-family: Consolas, monospace;
            }
            #titleLabel {
                font-size: 24px;
                font-weight: bold;
                color: #303133;
                margin-bottom: 10px;
            }
            #resultLabel {
                font-size: 16px;
                color: #E6A23C;
                font-weight: bold;
                background-color: #FDF6EC;
                border: 1px solid #FAECD8;
                border-radius: 5px;
                padding: 5px;
            }
        """
        self.setStyleSheet(style)

    def import_dataset(self):
        """导入数据集功能"""

        directory = QFileDialog.getExistingDirectory(self, "选择数据集文件夹", "")
        if directory:
            self.dataset_path = directory
            self.lbl_path.setText(f"已选择: {self.dataset_path}")
            self.log_box.append(f"> 成功导入数据集，路径: {directory}")

    def start_training(self):
        """开始训练功能"""
        if not self.dataset_path:
            self.log_box.append("> 警告：请先导入数据集！")
            return

        self.btn_train.setEnabled(False)
        self.btn_train.setText("训练中...")
        self.progress_bar.setValue(0)
        self.log_box.clear()

        self.thread = TrainingThread()
        self.thread.progress_update.connect(self.update_progress)
        self.thread.log_update.connect(self.update_log)
        self.thread.finished_signal.connect(self.training_finished)
        self.thread.start()

    def update_progress(self, val):
        self.progress_bar.setValue(val)

    def update_log(self, text):
        self.log_box.append(text)

        scrollbar = self.log_box.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

    def training_finished(self):
        self.btn_train.setEnabled(True)
        self.btn_train.setText("重新训练")

    def run_diagnosis(self):
        """模型诊断推理功能"""
        if self.progress_bar.value() != 100:
            self.log_box.append("> 提示：建议先完成模型训练再进行诊断。")

        self.lbl_result.setStyleSheet("color: #409EFF; background-color: #ECF5FF; border-color: #D9ECFF;")
        self.lbl_result.setText("正在分析振动信号...")
        QApplication.processEvents()  # 强制刷新界面一下

        time.sleep(1)  # 模拟推理时间

        diagnosis_status = "【内圈故障】 置信度: 98.5%"
        self.lbl_result.setStyleSheet("color: #F56C6C; background-color: #FEF0F0; border-color: #FDE2E2;")
        self.lbl_result.setText(f"诊断结果：{diagnosis_status}")
        self.log_box.append(f"> 执行诊断，发现异常：{diagnosis_status}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    font = QFont("Microsoft YaHei", 10)
    app.setFont(font)

    window = FaultDiagnosisUI()
    window.show()
    sys.exit(app.exec())
