# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1033, 730)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_15 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout.addWidget(self.pushButton_6)


        self.horizontalLayout_15.addLayout(self.verticalLayout)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_15.addWidget(self.line_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox = QGroupBox(self.page)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_5 = QPushButton(self.groupBox)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_2.addWidget(self.pushButton_5)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 4)

        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_4.addWidget(self.label_8)

        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setEnabled(False)
        self.checkBox.setCheckable(True)
        self.checkBox.setChecked(False)

        self.horizontalLayout_4.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setEnabled(False)
        self.checkBox_2.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setEnabled(False)
        self.checkBox_3.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(self.groupBox)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setEnabled(False)
        self.checkBox_4.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.checkBox_4)

        self.checkBox_5 = QCheckBox(self.groupBox)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setEnabled(False)
        self.checkBox_5.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.checkBox_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.page)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.comboBox = QComboBox(self.groupBox_2)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_3.addWidget(self.comboBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.tableWidget = QTableWidget(self.groupBox_2)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_5.addWidget(self.tableWidget)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 5)
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_14 = QVBoxLayout(self.page_3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.groupBox_9 = QGroupBox(self.page_3)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.verticalLayout_17 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_5 = QLabel(self.groupBox_9)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_18.addWidget(self.label_5)

        self.comboBox_2 = QComboBox(self.groupBox_9)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_18.addWidget(self.comboBox_2)

        self.horizontalLayout_18.setStretch(0, 1)
        self.horizontalLayout_18.setStretch(1, 1)

        self.horizontalLayout_22.addLayout(self.horizontalLayout_18)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_20 = QLabel(self.groupBox_9)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_19.addWidget(self.label_20)

        self.lineEdit_2 = QLineEdit(self.groupBox_9)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setReadOnly(True)

        self.horizontalLayout_19.addWidget(self.lineEdit_2)

        self.horizontalLayout_19.setStretch(0, 1)
        self.horizontalLayout_19.setStretch(1, 1)

        self.horizontalLayout_22.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_22.setStretch(0, 1)
        self.horizontalLayout_22.setStretch(2, 1)

        self.verticalLayout_17.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_21 = QLabel(self.groupBox_9)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_16.addWidget(self.label_21)

        self.lineEdit = QLineEdit(self.groupBox_9)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)
        self.lineEdit.setReadOnly(True)

        self.horizontalLayout_16.addWidget(self.lineEdit)

        self.horizontalLayout_16.setStretch(0, 1)
        self.horizontalLayout_16.setStretch(1, 1)

        self.horizontalLayout_21.addLayout(self.horizontalLayout_16)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_22 = QLabel(self.groupBox_9)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_17.addWidget(self.label_22)

        self.lineEdit_3 = QLineEdit(self.groupBox_9)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_3.setReadOnly(True)

        self.horizontalLayout_17.addWidget(self.lineEdit_3)

        self.horizontalLayout_17.setStretch(0, 1)
        self.horizontalLayout_17.setStretch(1, 1)

        self.horizontalLayout_21.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_21.setStretch(0, 1)
        self.horizontalLayout_21.setStretch(2, 1)

        self.verticalLayout_17.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_23 = QLabel(self.groupBox_9)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_20.addWidget(self.label_23)

        self.spinBox_10 = QSpinBox(self.groupBox_9)
        self.spinBox_10.setObjectName(u"spinBox_10")

        self.horizontalLayout_20.addWidget(self.spinBox_10)


        self.verticalLayout_15.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_24 = QLabel(self.groupBox_9)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_24.addWidget(self.label_24)

        self.spinBox_11 = QSpinBox(self.groupBox_9)
        self.spinBox_11.setObjectName(u"spinBox_11")
        self.spinBox_11.setMaximum(7)

        self.horizontalLayout_24.addWidget(self.spinBox_11)


        self.verticalLayout_15.addLayout(self.horizontalLayout_24)


        self.horizontalLayout_25.addLayout(self.verticalLayout_15)

        self.pushButton_8 = QPushButton(self.groupBox_9)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_25.addWidget(self.pushButton_8)

        self.horizontalLayout_25.setStretch(0, 4)
        self.horizontalLayout_25.setStretch(1, 1)

        self.verticalLayout_17.addLayout(self.horizontalLayout_25)


        self.verticalLayout_14.addWidget(self.groupBox_9)

        self.groupBox_8 = QGroupBox(self.page_3)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.horizontalLayout_23 = QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")

        self.horizontalLayout_23.addLayout(self.verticalLayout_16)


        self.verticalLayout_14.addWidget(self.groupBox_8)

        self.verticalLayout_14.setStretch(0, 1)
        self.verticalLayout_14.setStretch(1, 3)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_18 = QVBoxLayout(self.page_4)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.groupBox_10 = QGroupBox(self.page_4)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.verticalLayout_20 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_6 = QLabel(self.groupBox_10)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_30.addWidget(self.label_6)

        self.lineEdit_4 = QLineEdit(self.groupBox_10)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setReadOnly(True)

        self.horizontalLayout_30.addWidget(self.lineEdit_4)

        self.horizontalLayout_30.setStretch(0, 1)
        self.horizontalLayout_30.setStretch(1, 2)

        self.verticalLayout_20.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_25 = QLabel(self.groupBox_10)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_29.addWidget(self.label_25)

        self.lineEdit_5 = QLineEdit(self.groupBox_10)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setReadOnly(True)

        self.horizontalLayout_29.addWidget(self.lineEdit_5)

        self.horizontalLayout_29.setStretch(0, 1)
        self.horizontalLayout_29.setStretch(1, 2)

        self.verticalLayout_20.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_27 = QLabel(self.groupBox_10)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_28.addWidget(self.label_27)

        self.lineEdit_6 = QLineEdit(self.groupBox_10)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.horizontalLayout_28.addWidget(self.lineEdit_6)

        self.horizontalLayout_28.setStretch(0, 1)
        self.horizontalLayout_28.setStretch(1, 2)

        self.verticalLayout_20.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.pushButton_9 = QPushButton(self.groupBox_10)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.horizontalLayout_27.addWidget(self.pushButton_9)

        self.label_26 = QLabel(self.groupBox_10)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_27.addWidget(self.label_26)

        self.horizontalLayout_27.setStretch(0, 1)
        self.horizontalLayout_27.setStretch(1, 2)

        self.verticalLayout_20.addLayout(self.horizontalLayout_27)


        self.verticalLayout_18.addWidget(self.groupBox_10)

        self.groupBox_11 = QGroupBox(self.page_4)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.verticalLayout_19 = QVBoxLayout(self.groupBox_11)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.pushButton_10 = QPushButton(self.groupBox_11)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.horizontalLayout_26.addWidget(self.pushButton_10)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_3)

        self.pushButton_11 = QPushButton(self.groupBox_11)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.horizontalLayout_26.addWidget(self.pushButton_11)

        self.horizontalLayout_26.setStretch(0, 2)
        self.horizontalLayout_26.setStretch(1, 1)
        self.horizontalLayout_26.setStretch(2, 2)

        self.verticalLayout_19.addLayout(self.horizontalLayout_26)

        self.plainTextEdit_2 = QPlainTextEdit(self.groupBox_11)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setReadOnly(True)

        self.verticalLayout_19.addWidget(self.plainTextEdit_2)


        self.verticalLayout_18.addWidget(self.groupBox_11)

        self.verticalLayout_18.setStretch(0, 1)
        self.verticalLayout_18.setStretch(1, 3)
        self.stackedWidget.addWidget(self.page_4)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_21 = QVBoxLayout(self.page_2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.groupBox_12 = QGroupBox(self.page_2)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.verticalLayout_25 = QVBoxLayout(self.groupBox_12)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.pushButton_12 = QPushButton(self.groupBox_12)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.horizontalLayout_34.addWidget(self.pushButton_12)

        self.label_4 = QLabel(self.groupBox_12)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_34.addWidget(self.label_4)

        self.horizontalLayout_34.setStretch(0, 1)
        self.horizontalLayout_34.setStretch(1, 3)

        self.verticalLayout_25.addLayout(self.horizontalLayout_34)

        self.line_3 = QFrame(self.groupBox_12)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_25.addWidget(self.line_3)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.groupBox_14 = QGroupBox(self.groupBox_12)
        self.groupBox_14.setObjectName(u"groupBox_14")
        font = QFont()
        font.setKerning(True)
        self.groupBox_14.setFont(font)
        self.groupBox_14.setFlat(False)
        self.groupBox_14.setCheckable(False)
        self.verticalLayout_24 = QVBoxLayout(self.groupBox_14)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")

        self.verticalLayout_24.addLayout(self.verticalLayout_23)


        self.horizontalLayout_33.addWidget(self.groupBox_14)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.pushButton_13 = QPushButton(self.groupBox_12)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.horizontalLayout_32.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.groupBox_12)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.horizontalLayout_32.addWidget(self.pushButton_14)

        self.horizontalLayout_32.setStretch(0, 1)
        self.horizontalLayout_32.setStretch(1, 1)

        self.verticalLayout_22.addLayout(self.horizontalLayout_32)

        self.plainTextEdit_3 = QPlainTextEdit(self.groupBox_12)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setReadOnly(True)

        self.verticalLayout_22.addWidget(self.plainTextEdit_3)


        self.horizontalLayout_33.addLayout(self.verticalLayout_22)

        self.horizontalLayout_33.setStretch(0, 1)
        self.horizontalLayout_33.setStretch(1, 1)

        self.verticalLayout_25.addLayout(self.horizontalLayout_33)


        self.verticalLayout_21.addWidget(self.groupBox_12)

        self.groupBox_13 = QGroupBox(self.page_2)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.verticalLayout_27 = QVBoxLayout(self.groupBox_13)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.pushButton_15 = QPushButton(self.groupBox_13)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.horizontalLayout_35.addWidget(self.pushButton_15)

        self.pushButton_16 = QPushButton(self.groupBox_13)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.horizontalLayout_35.addWidget(self.pushButton_16)


        self.verticalLayout_27.addLayout(self.horizontalLayout_35)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")

        self.verticalLayout_27.addLayout(self.verticalLayout_26)

        self.verticalLayout_27.setStretch(0, 1)
        self.verticalLayout_27.setStretch(1, 9)

        self.verticalLayout_21.addWidget(self.groupBox_13)

        self.verticalLayout_21.setStretch(0, 3)
        self.verticalLayout_21.setStretch(1, 2)
        self.stackedWidget.addWidget(self.page_2)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_10 = QVBoxLayout(self.page_5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.groupBox_3 = QGroupBox(self.page_5)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_11 = QLabel(self.groupBox_3)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_8.addWidget(self.label_11)

        self.spinBox_3 = QSpinBox(self.groupBox_3)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setMaximum(200)

        self.horizontalLayout_8.addWidget(self.spinBox_3)


        self.verticalLayout_11.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_9.addWidget(self.label_12)

        self.spinBox_4 = QSpinBox(self.groupBox_3)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setMaximum(200)
        self.spinBox_4.setValue(10)

        self.horizontalLayout_9.addWidget(self.spinBox_4)


        self.verticalLayout_11.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_10.addWidget(self.label_15)

        self.spinBox_5 = QSpinBox(self.groupBox_3)
        self.spinBox_5.setObjectName(u"spinBox_5")
        self.spinBox_5.setMaximum(256)
        self.spinBox_5.setValue(128)

        self.horizontalLayout_10.addWidget(self.spinBox_5)


        self.verticalLayout_11.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_7.addWidget(self.groupBox_3)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox_6 = QGroupBox(self.page_5)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_16 = QLabel(self.groupBox_6)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_11.addWidget(self.label_16)

        self.spinBox_6 = QSpinBox(self.groupBox_6)
        self.spinBox_6.setObjectName(u"spinBox_6")
        self.spinBox_6.setMaximum(200)
        self.spinBox_6.setValue(10)

        self.horizontalLayout_11.addWidget(self.spinBox_6)


        self.verticalLayout_12.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_17 = QLabel(self.groupBox_6)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_12.addWidget(self.label_17)

        self.spinBox_7 = QSpinBox(self.groupBox_6)
        self.spinBox_7.setObjectName(u"spinBox_7")
        self.spinBox_7.setMaximum(200)
        self.spinBox_7.setValue(15)

        self.horizontalLayout_12.addWidget(self.spinBox_7)


        self.verticalLayout_12.addLayout(self.horizontalLayout_12)


        self.verticalLayout_7.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(self.page_5)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_18 = QLabel(self.groupBox_7)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_13.addWidget(self.label_18)

        self.spinBox_8 = QSpinBox(self.groupBox_7)
        self.spinBox_8.setObjectName(u"spinBox_8")
        self.spinBox_8.setMaximum(200)
        self.spinBox_8.setValue(20)

        self.horizontalLayout_13.addWidget(self.spinBox_8)


        self.verticalLayout_13.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_19 = QLabel(self.groupBox_7)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_14.addWidget(self.label_19)

        self.spinBox_9 = QSpinBox(self.groupBox_7)
        self.spinBox_9.setObjectName(u"spinBox_9")
        self.spinBox_9.setMaximum(200)
        self.spinBox_9.setValue(100)

        self.horizontalLayout_14.addWidget(self.spinBox_9)


        self.verticalLayout_13.addLayout(self.horizontalLayout_14)


        self.verticalLayout_7.addWidget(self.groupBox_7)


        self.horizontalLayout_7.addLayout(self.verticalLayout_7)


        self.verticalLayout_10.addLayout(self.horizontalLayout_7)

        self.groupBox_4 = QGroupBox(self.page_5)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_13 = QLabel(self.groupBox_4)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_5.addWidget(self.label_13)

        self.spinBox = QSpinBox(self.groupBox_4)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(32)
        self.spinBox.setValue(16)

        self.horizontalLayout_5.addWidget(self.spinBox)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_14 = QLabel(self.groupBox_4)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_6.addWidget(self.label_14)

        self.spinBox_2 = QSpinBox(self.groupBox_4)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setValue(20)

        self.horizontalLayout_6.addWidget(self.spinBox_2)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_28 = QLabel(self.groupBox_4)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_31.addWidget(self.label_28)

        self.spinBox_12 = QSpinBox(self.groupBox_4)
        self.spinBox_12.setObjectName(u"spinBox_12")
        self.spinBox_12.setMaximum(4)
        self.spinBox_12.setValue(4)

        self.horizontalLayout_31.addWidget(self.spinBox_12)


        self.verticalLayout_9.addLayout(self.horizontalLayout_31)


        self.verticalLayout_10.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.page_5)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_9 = QLabel(self.groupBox_5)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_8.addWidget(self.label_9)

        self.label_10 = QLabel(self.groupBox_5)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_8.addWidget(self.label_10)


        self.verticalLayout_10.addWidget(self.groupBox_5)

        self.verticalLayout_10.setStretch(0, 5)
        self.verticalLayout_10.setStretch(1, 2)
        self.verticalLayout_10.setStretch(2, 1)
        self.stackedWidget.addWidget(self.page_5)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout_15.addLayout(self.verticalLayout_3)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_15.addWidget(self.line)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout.addWidget(self.pushButton_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.plainTextEdit)


        self.horizontalLayout_15.addLayout(self.verticalLayout_2)

        self.horizontalLayout_15.setStretch(0, 2)
        self.horizontalLayout_15.setStretch(1, 1)
        self.horizontalLayout_15.setStretch(2, 10)
        self.horizontalLayout_15.setStretch(3, 1)
        self.horizontalLayout_15.setStretch(4, 4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u667a\u80fd\u9f7f\u8f6e\u7bb1\u6545\u969c\u8bca\u65ad\u7cfb\u7edf", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u539f\u59cb\u6570\u636e", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u4fe1\u53f7\u5904\u7406", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u8bad\u7ec3", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u8fd0\u884c", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u53c2\u6570\u8bbe\u7f6e", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u529f\u80fd\u533a\uff1a\u539f\u59cb\u6570\u636e", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d\u6570\u636e\u96c6", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d\u6570\u636e\u96c6", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u672a\u52a0\u8f7d\u6570\u636e\u96c6", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u88ab\u9009\u4e2d\u7684\u6570\u636e\u96c6\uff1a", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Health", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Chipped", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Miss", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Root", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"Surface", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u9884\u89c8\u539f\u59cb\u6570\u636e", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u9700\u8981\u9884\u89c8\u7684\u6570\u636e\u96c6\uff08\u53ea\u5c55\u793a\u524d128\u884c\u6570\u636e\uff09\uff1a", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u7535\u673a\u632f\u52a8", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u884c\u661f\u8f6ex", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u884c\u661f\u8f6ey", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u884c\u661f\u8f6ez", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u7535\u673a\u626d\u77e9", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u51cf\u901f\u5668x", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u51cf\u901f\u5668y", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u51cf\u901f\u5668z", None));
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u96c6\u8be6\u7ec6", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u9700\u8981\u67e5\u770b\u7684\u6570\u636e\u96c6\uff1a", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u8be5\u6570\u636e\u96c6\u5171\u6709\u6570\u636e\uff1a", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u7684\u6ed1\u7a97\u957f\u5ea6\u4e3a\uff1a", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u53ef\u83b7\u5f97\u6709\u6548\u6837\u672c\u6570\uff1a", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u9700\u8981\u67e5\u770b\u7684\u6837\u672c\u7f16\u53f7\uff08\u4ece0\u5f00\u59cb\uff09\uff1a", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u9700\u8981\u67e5\u770b\u7684\u901a\u9053\u7f16\u53f7\uff08\u4ece0\u5f00\u59cb\uff09\uff1a", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u8fdb\u884c\u5c0f\u6ce2\u53d8\u6362", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"\u5de6\uff1a\u539f\u59cb\u4fe1\u53f7\uff0c\u53f3\uff1a\u5c0f\u6ce2\u53d8\u6362\u540e\u4fe1\u53f7", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"\u6743\u91cd\u4fdd\u5b58\u8bbe\u7f6e", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u7684EPOCH\u4e3a:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u7684BATCH_SIZE\u4e3a\uff1a", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u4fdd\u5b58\u7684\u6743\u91cd\u540d\u79f0\uff1a", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u4fdd\u5b58\u8def\u5f84", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u672a\u8bbe\u7f6e\u6743\u91cd\u4fdd\u5b58\u8def\u5f84", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"\u8bad\u7ec3\u72b6\u51b5", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u8bad\u7ec3", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"\u7ec8\u6b62\u8bad\u7ec3", None))
        self.plainTextEdit_2.setPlainText("")
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u8bc4\u4f30", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d\u6743\u91cd", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u672a\u9009\u62e9\u6743\u91cd\u6587\u4ef6", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"\u6df7\u6dc6\u77e9\u9635", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u8bc4\u4f30", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"\u7ec8\u6b62\u8bc4\u4f30", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u5de5\u4f5c", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u5de5\u4f5c", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"\u7ec8\u6b62\u5de5\u4f5c", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u8bad\u7ec3\u96c6", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u91c7\u6837\u5f00\u59cb\u65f6\u95f4(s)", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u91c7\u6837\u7ed3\u675f\u65f6\u95f4(s)", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u6ed1\u7a97\u957f\u5ea6", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u96c6", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u91c7\u6837\u5f00\u59cb\u65f6\u95f4(s)", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u91c7\u6837\u5f00\u59cb\u65f6\u95f4(s)", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"\u9a8c\u8bc1\u96c6", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u91c7\u6837\u5f00\u59cb\u65f6\u95f4(s)", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u91c7\u6837\u5f00\u59cb\u65f6\u95f4(s)", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u795e\u7ecf\u7f51\u7edc", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"BATCH_SIZE", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"EPOCH", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"NUM_WORKERS", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u9f7f\u8f6e\u7bb1\u6545\u969c\u8bca\u65ad\u7cfb\u7edf 2026\u5317\u4eac\u79d1\u6280\u5927\u5b66\u6bd5\u4e1a\u8bbe\u8ba1", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"MIT License Copyright (c) 2026 Reef", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u63a7\u5236\u53f0", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u63a7\u5236\u53f0", None))
    # retranslateUi

