# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serial_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_serial_ui(object):
    def setupUi(self, serial_ui):
        serial_ui.setObjectName("serial_ui")
        serial_ui.resize(1031, 606)
        self.gridLayout = QtWidgets.QGridLayout(serial_ui)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(serial_ui)
        self.widget.setStyleSheet("background-color: rgb(51, 51, 51);")
        self.widget.setObjectName("widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.comExpandtabWidget = QtWidgets.QTabWidget(self.widget)
        self.comExpandtabWidget.setStyleSheet("background-color: rgb(51, 51, 51);")
        self.comExpandtabWidget.setObjectName("comExpandtabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.comExpandtabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.comExpandtabWidget.addTab(self.tab_4, "")
        self.gridLayout_4.addWidget(self.comExpandtabWidget, 0, 1, 1, 1)
        self.ComRecvtextBrowser = QtWidgets.QTextBrowser(self.widget)
        self.ComRecvtextBrowser.setStyleSheet("background-color: rgb(35, 35, 35);\n"
"color: rgb(255, 255, 0);")
        self.ComRecvtextBrowser.setObjectName("ComRecvtextBrowser")
        self.gridLayout_4.addWidget(self.ComRecvtextBrowser, 0, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 250))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setLineWidth(5)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 35))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comClearButton = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comClearButton.sizePolicy().hasHeightForWidth())
        self.comClearButton.setSizePolicy(sizePolicy)
        self.comClearButton.setStyleSheet("font: 9pt ;\n"
"color: rgb(255, 204, 0);\n"
"background-color: rgb(34, 34, 34);\n"
"padding: 8;")
        self.comClearButton.setFlat(False)
        self.comClearButton.setObjectName("comClearButton")
        self.horizontalLayout_2.addWidget(self.comClearButton)
        self.comRecvHexcheckBox = QtWidgets.QCheckBox(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comRecvHexcheckBox.sizePolicy().hasHeightForWidth())
        self.comRecvHexcheckBox.setSizePolicy(sizePolicy)
        self.comRecvHexcheckBox.setStyleSheet("color: rgb(255, 204, 0);")
        self.comRecvHexcheckBox.setTristate(False)
        self.comRecvHexcheckBox.setObjectName("comRecvHexcheckBox")
        self.horizontalLayout_2.addWidget(self.comRecvHexcheckBox)
        self.comRecvTimecheckBox = QtWidgets.QCheckBox(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comRecvTimecheckBox.sizePolicy().hasHeightForWidth())
        self.comRecvTimecheckBox.setSizePolicy(sizePolicy)
        self.comRecvTimecheckBox.setStyleSheet("color: rgb(255, 204, 0);")
        self.comRecvTimecheckBox.setTristate(False)
        self.comRecvTimecheckBox.setObjectName("comRecvTimecheckBox")
        self.horizontalLayout_2.addWidget(self.comRecvTimecheckBox)
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setStyleSheet("color: rgb(255, 204, 0);")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.comRecvTimeoutEdit = QtWidgets.QLineEdit(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comRecvTimeoutEdit.sizePolicy().hasHeightForWidth())
        self.comRecvTimeoutEdit.setSizePolicy(sizePolicy)
        self.comRecvTimeoutEdit.setMaximumSize(QtCore.QSize(40, 16777215))
        self.comRecvTimeoutEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comRecvTimeoutEdit.setObjectName("comRecvTimeoutEdit")
        self.horizontalLayout_2.addWidget(self.comRecvTimeoutEdit)
        self.label_8 = QtWidgets.QLabel(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setStyleSheet("color: rgb(255, 204, 0);")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.comRecvSavecheckBox = QtWidgets.QCheckBox(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comRecvSavecheckBox.sizePolicy().hasHeightForWidth())
        self.comRecvSavecheckBox.setSizePolicy(sizePolicy)
        self.comRecvSavecheckBox.setStyleSheet("color: rgb(255, 204, 0);")
        self.comRecvSavecheckBox.setTristate(False)
        self.comRecvSavecheckBox.setObjectName("comRecvSavecheckBox")
        self.horizontalLayout_2.addWidget(self.comRecvSavecheckBox)
        self.comRecvSavepushButton = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comRecvSavepushButton.sizePolicy().hasHeightForWidth())
        self.comRecvSavepushButton.setSizePolicy(sizePolicy)
        self.comRecvSavepushButton.setStyleSheet("font: 9pt ;\n"
"color: rgb(255, 204, 0);\n"
"background-color: rgb(34, 34, 34);\n"
"padding: 8;")
        self.comRecvSavepushButton.setObjectName("comRecvSavepushButton")
        self.horizontalLayout_2.addWidget(self.comRecvSavepushButton)
        self.comHidepushButton = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comHidepushButton.sizePolicy().hasHeightForWidth())
        self.comHidepushButton.setSizePolicy(sizePolicy)
        self.comHidepushButton.setStyleSheet("font: 9pt ;\n"
"color: rgb(255, 204, 0);\n"
"background-color: rgb(34, 34, 34);\n"
"padding: 8;")
        self.comHidepushButton.setFlat(False)
        self.comHidepushButton.setObjectName("comHidepushButton")
        self.horizontalLayout_2.addWidget(self.comHidepushButton)
        self.comExpandpushButton = QtWidgets.QPushButton(self.frame_5)
        self.comExpandpushButton.setStyleSheet("font: 9pt ;\n"
"color: rgb(255, 204, 0);\n"
"background-color: rgb(34, 34, 34);\n"
"padding: 8;")
        self.comExpandpushButton.setFlat(False)
        self.comExpandpushButton.setObjectName("comExpandpushButton")
        self.horizontalLayout_2.addWidget(self.comExpandpushButton)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_6 = QtWidgets.QFrame(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QtCore.QSize(350, 0))
        self.frame_6.setStyleSheet("background-color: rgb(51, 51, 51);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.comIDcomboBox = QtWidgets.QComboBox(self.frame_6)
        self.comIDcomboBox.setGeometry(QtCore.QRect(50, 10, 141, 31))
        self.comIDcomboBox.setStyleSheet("font: 10pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comIDcomboBox.setObjectName("comIDcomboBox")
        self.label = QtWidgets.QLabel(self.frame_6)
        self.label.setGeometry(QtCore.QRect(10, 16, 41, 16))
        self.label.setStyleSheet("font: 10pt \"宋体\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_6)
        self.label_2.setGeometry(QtCore.QRect(210, 16, 41, 16))
        self.label_2.setStyleSheet("font: 10pt \"宋体\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.comBaudcomboBox = QtWidgets.QComboBox(self.frame_6)
        self.comBaudcomboBox.setGeometry(QtCore.QRect(250, 10, 81, 31))
        self.comBaudcomboBox.setStyleSheet("font: 10pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comBaudcomboBox.setObjectName("comBaudcomboBox")
        self.comBaudcomboBox.addItem("")
        self.comBaudcomboBox.addItem("")
        self.comBaudcomboBox.addItem("")
        self.comBaudcomboBox.addItem("")
        self.comBaudcomboBox.addItem("")
        self.comBaudcomboBox.addItem("")
        self.comBaudcomboBox.addItem("")
        self.comBaudcomboBox.addItem("")
        self.comBaudcomboBox.addItem("")
        self.comBaudcomboBox.addItem("")
        self.comBaudcomboBox.addItem("")
        self.comBaudcomboBox.addItem("")
        self.comBaudcomboBox.addItem("")
        self.comBaudcomboBox.addItem("")
        self.comBaudcomboBox.addItem("")
        self.comBaudcomboBox.addItem("")
        self.comBaudcomboBox.addItem("")
        self.comBaudcomboBox.addItem("")
        self.comBaudcomboBox.addItem("")
        self.comBaudcomboBox.addItem("")
        self.comBaudcomboBox.addItem("")
        self.comOpenpushButton = QtWidgets.QPushButton(self.frame_6)
        self.comOpenpushButton.setGeometry(QtCore.QRect(160, 70, 161, 41))
        self.comOpenpushButton.setStyleSheet("font: 11pt \"宋体\";\n"
"color: rgb(255, 255, 255);")
        self.comOpenpushButton.setObjectName("comOpenpushButton")
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 41, 16))
        self.label_3.setStyleSheet("font: 10pt \"宋体\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 41, 16))
        self.label_4.setStyleSheet("font: 10pt \"宋体\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_6)
        self.label_5.setGeometry(QtCore.QRect(10, 130, 41, 16))
        self.label_5.setStyleSheet("font: 10pt \"宋体\";\n"
"color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_6)
        self.label_6.setGeometry(QtCore.QRect(10, 160, 41, 16))
        self.label_6.setStyleSheet("font: 10pt \"宋体\";\n"
"color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.comBitlencomboBox = QtWidgets.QComboBox(self.frame_6)
        self.comBitlencomboBox.setGeometry(QtCore.QRect(60, 70, 61, 21))
        self.comBitlencomboBox.setStyleSheet("font: 10pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comBitlencomboBox.setObjectName("comBitlencomboBox")
        self.comBitlencomboBox.addItem("")
        self.comBitlencomboBox.addItem("")
        self.comBitlencomboBox.addItem("")
        self.comBitlencomboBox.addItem("")
        self.comStoplencomboBox = QtWidgets.QComboBox(self.frame_6)
        self.comStoplencomboBox.setGeometry(QtCore.QRect(60, 100, 61, 21))
        self.comStoplencomboBox.setStyleSheet("font: 10pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comStoplencomboBox.setObjectName("comStoplencomboBox")
        self.comStoplencomboBox.addItem("")
        self.comStoplencomboBox.addItem("")
        self.comStoplencomboBox.addItem("")
        self.comCheckcomboBox = QtWidgets.QComboBox(self.frame_6)
        self.comCheckcomboBox.setGeometry(QtCore.QRect(60, 130, 61, 21))
        self.comCheckcomboBox.setStyleSheet("font: 10pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comCheckcomboBox.setObjectName("comCheckcomboBox")
        self.comCheckcomboBox.addItem("")
        self.comCheckcomboBox.addItem("")
        self.comCheckcomboBox.addItem("")
        self.comCheckcomboBox.addItem("")
        self.comCheckcomboBox.addItem("")
        self.comFlowCtlcomboBox = QtWidgets.QComboBox(self.frame_6)
        self.comFlowCtlcomboBox.setGeometry(QtCore.QRect(60, 160, 61, 21))
        self.comFlowCtlcomboBox.setStyleSheet("font: 10pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comFlowCtlcomboBox.setObjectName("comFlowCtlcomboBox")
        self.comFlowCtlcomboBox.addItem("")
        self.comFlowCtlcomboBox.addItem("")
        self.comFlowCtlcomboBox.addItem("")
        self.comSendpushButton = QtWidgets.QPushButton(self.frame_6)
        self.comSendpushButton.setGeometry(QtCore.QRect(160, 140, 161, 41))
        self.comSendpushButton.setStyleSheet("font: 11pt \"宋体\";\n"
"color: rgb(255, 255, 255);")
        self.comSendpushButton.setObjectName("comSendpushButton")
        self.horizontalLayout.addWidget(self.frame_6)
        self.frame_8 = QtWidgets.QFrame(self.frame_7)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_9 = QtWidgets.QFrame(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setMinimumSize(QtCore.QSize(0, 70))
        self.frame_9.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_9.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.comSendHexcheckBox = QtWidgets.QCheckBox(self.frame_9)
        self.comSendHexcheckBox.setGeometry(QtCore.QRect(10, 46, 67, 18))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comSendHexcheckBox.sizePolicy().hasHeightForWidth())
        self.comSendHexcheckBox.setSizePolicy(sizePolicy)
        self.comSendHexcheckBox.setStyleSheet("color: rgb(255, 204, 0);")
        self.comSendHexcheckBox.setTristate(False)
        self.comSendHexcheckBox.setObjectName("comSendHexcheckBox")
        self.comFiletextBrowser = QtWidgets.QTextBrowser(self.frame_9)
        self.comFiletextBrowser.setGeometry(QtCore.QRect(80, 10, 191, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comFiletextBrowser.sizePolicy().hasHeightForWidth())
        self.comFiletextBrowser.setSizePolicy(sizePolicy)
        self.comFiletextBrowser.setMaximumSize(QtCore.QSize(300, 30))
        self.comFiletextBrowser.setStyleSheet("font: 10pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comFiletextBrowser.setObjectName("comFiletextBrowser")
        self.comOpenFilepushButton = QtWidgets.QPushButton(self.frame_9)
        self.comOpenFilepushButton.setGeometry(QtCore.QRect(10, 10, 66, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comOpenFilepushButton.sizePolicy().hasHeightForWidth())
        self.comOpenFilepushButton.setSizePolicy(sizePolicy)
        self.comOpenFilepushButton.setStyleSheet("font: 9pt ;\n"
"color: rgb(255, 204, 0);\n"
"background-color: rgb(34, 34, 34);\n"
"padding: 8;")
        self.comOpenFilepushButton.setFlat(False)
        self.comOpenFilepushButton.setObjectName("comOpenFilepushButton")
        self.comSendFilepushButton = QtWidgets.QPushButton(self.frame_9)
        self.comSendFilepushButton.setGeometry(QtCore.QRect(280, 10, 66, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comSendFilepushButton.sizePolicy().hasHeightForWidth())
        self.comSendFilepushButton.setSizePolicy(sizePolicy)
        self.comSendFilepushButton.setStyleSheet("font: 9pt ;\n"
"color: rgb(255, 204, 0);\n"
"background-color: rgb(34, 34, 34);\n"
"padding: 8;")
        self.comSendFilepushButton.setFlat(False)
        self.comSendFilepushButton.setObjectName("comSendFilepushButton")
        self.comFileSendStoppushButton = QtWidgets.QPushButton(self.frame_9)
        self.comFileSendStoppushButton.setGeometry(QtCore.QRect(350, 10, 42, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comFileSendStoppushButton.sizePolicy().hasHeightForWidth())
        self.comFileSendStoppushButton.setSizePolicy(sizePolicy)
        self.comFileSendStoppushButton.setStyleSheet("font: 9pt ;\n"
"background-color: rgb(34, 34, 34);\n"
"padding: 8;\n"
"color: rgb(255, 87, 53);")
        self.comFileSendStoppushButton.setObjectName("comFileSendStoppushButton")
        self.comTimingSendcheckBox = QtWidgets.QCheckBox(self.frame_9)
        self.comTimingSendcheckBox.setGeometry(QtCore.QRect(90, 46, 67, 18))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comTimingSendcheckBox.sizePolicy().hasHeightForWidth())
        self.comTimingSendcheckBox.setSizePolicy(sizePolicy)
        self.comTimingSendcheckBox.setStyleSheet("color: rgb(255, 204, 0);")
        self.comTimingSendcheckBox.setTristate(False)
        self.comTimingSendcheckBox.setObjectName("comTimingSendcheckBox")
        self.comTimnglineEdit = QtWidgets.QLineEdit(self.frame_9)
        self.comTimnglineEdit.setGeometry(QtCore.QRect(170, 46, 41, 20))
        self.comTimnglineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comTimnglineEdit.setObjectName("comTimnglineEdit")
        self.label_9 = QtWidgets.QLabel(self.frame_9)
        self.label_9.setGeometry(QtCore.QRect(220, 44, 20, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setStyleSheet("color: rgb(255, 204, 0);")
        self.label_9.setObjectName("label_9")
        self.comSendEntercheckBox = QtWidgets.QCheckBox(self.frame_9)
        self.comSendEntercheckBox.setGeometry(QtCore.QRect(240, 47, 81, 18))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comSendEntercheckBox.sizePolicy().hasHeightForWidth())
        self.comSendEntercheckBox.setSizePolicy(sizePolicy)
        self.comSendEntercheckBox.setStyleSheet("color: rgb(255, 204, 0);")
        self.comSendEntercheckBox.setTristate(False)
        self.comSendEntercheckBox.setObjectName("comSendEntercheckBox")
        self.label_10 = QtWidgets.QLabel(self.frame_9)
        self.label_10.setGeometry(QtCore.QRect(340, 45, 20, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setStyleSheet("color: rgb(255, 204, 0);")
        self.label_10.setObjectName("label_10")
        self.comChecklineEdit = QtWidgets.QLineEdit(self.frame_9)
        self.comChecklineEdit.setGeometry(QtCore.QRect(356, 46, 31, 20))
        self.comChecklineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comChecklineEdit.setText("")
        self.comChecklineEdit.setObjectName("comChecklineEdit")
        self.label_11 = QtWidgets.QLabel(self.frame_9)
        self.label_11.setGeometry(QtCore.QRect(394, 50, 51, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setStyleSheet("color: rgb(255, 204, 0);")
        self.label_11.setObjectName("label_11")
        self.comCheckcomboBox_2 = QtWidgets.QComboBox(self.frame_9)
        self.comCheckcomboBox_2.setGeometry(QtCore.QRect(434, 45, 72, 20))
        self.comCheckcomboBox_2.setStyleSheet("font: 9pt ;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comCheckcomboBox_2.setObjectName("comCheckcomboBox_2")
        self.comCheckcomboBox_2.addItem("")
        self.label_12 = QtWidgets.QLabel(self.frame_9)
        self.label_12.setGeometry(QtCore.QRect(511, 50, 41, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setStyleSheet("color: rgb(255, 204, 0);")
        self.label_12.setObjectName("label_12")
        self.comCheckWaycomboBox = QtWidgets.QComboBox(self.frame_9)
        self.comCheckWaycomboBox.setGeometry(QtCore.QRect(552, 45, 71, 20))
        self.comCheckWaycomboBox.setStyleSheet("font: 9pt ;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comCheckWaycomboBox.setObjectName("comCheckWaycomboBox")
        self.comCheckWaycomboBox.addItem("")
        self.comCheckRestextBrowser = QtWidgets.QTextBrowser(self.frame_9)
        self.comCheckRestextBrowser.setGeometry(QtCore.QRect(630, 45, 71, 21))
        self.comCheckRestextBrowser.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.comCheckRestextBrowser.setObjectName("comCheckRestextBrowser")
        self.verticalLayout_3.addWidget(self.frame_9)
        self.ComSendtextEdit = QtWidgets.QTextEdit(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ComSendtextEdit.sizePolicy().hasHeightForWidth())
        self.ComSendtextEdit.setSizePolicy(sizePolicy)
        self.ComSendtextEdit.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.ComSendtextEdit.setFrameShape(QtWidgets.QFrame.Panel)
        self.ComSendtextEdit.setObjectName("ComSendtextEdit")
        self.verticalLayout_3.addWidget(self.ComSendtextEdit)
        self.horizontalLayout.addWidget(self.frame_8)
        self.verticalLayout_2.addWidget(self.frame_7)
        self.gridLayout_4.addWidget(self.frame_4, 1, 0, 1, 2)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(serial_ui)
        self.comExpandtabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(serial_ui)

    def retranslateUi(self, serial_ui):
        _translate = QtCore.QCoreApplication.translate
        serial_ui.setWindowTitle(_translate("serial_ui", "Form"))
        self.comExpandtabWidget.setTabText(self.comExpandtabWidget.indexOf(self.tab_3), _translate("serial_ui", "多条字符串发送"))
        self.comExpandtabWidget.setTabText(self.comExpandtabWidget.indexOf(self.tab_4), _translate("serial_ui", "Reserver"))
        self.comClearButton.setText(_translate("serial_ui", "清除窗口"))
        self.comRecvHexcheckBox.setText(_translate("serial_ui", "HEX显示"))
        self.comRecvTimecheckBox.setText(_translate("serial_ui", "加时间戳和分包显示"))
        self.label_7.setText(_translate("serial_ui", "<html><head/><body><p>超时时间</p></body></html>"))
        self.comRecvTimeoutEdit.setText(_translate("serial_ui", "20"))
        self.label_8.setText(_translate("serial_ui", "ms"))
        self.comRecvSavecheckBox.setText(_translate("serial_ui", "接收数据到文件"))
        self.comRecvSavepushButton.setText(_translate("serial_ui", "保存数据"))
        self.comHidepushButton.setText(_translate("serial_ui", "隐藏设置"))
        self.comExpandpushButton.setText(_translate("serial_ui", "扩展工具"))
        self.label.setText(_translate("serial_ui", "端口号"))
        self.label_2.setText(_translate("serial_ui", "波特率"))
        self.comBaudcomboBox.setItemText(0, _translate("serial_ui", "Custom"))
        self.comBaudcomboBox.setItemText(1, _translate("serial_ui", "110"))
        self.comBaudcomboBox.setItemText(2, _translate("serial_ui", "300"))
        self.comBaudcomboBox.setItemText(3, _translate("serial_ui", "600"))
        self.comBaudcomboBox.setItemText(4, _translate("serial_ui", "1200"))
        self.comBaudcomboBox.setItemText(5, _translate("serial_ui", "2400"))
        self.comBaudcomboBox.setItemText(6, _translate("serial_ui", "4800"))
        self.comBaudcomboBox.setItemText(7, _translate("serial_ui", "9600"))
        self.comBaudcomboBox.setItemText(8, _translate("serial_ui", "14400"))
        self.comBaudcomboBox.setItemText(9, _translate("serial_ui", "19200"))
        self.comBaudcomboBox.setItemText(10, _translate("serial_ui", "38400"))
        self.comBaudcomboBox.setItemText(11, _translate("serial_ui", "56000"))
        self.comBaudcomboBox.setItemText(12, _translate("serial_ui", "57600"))
        self.comBaudcomboBox.setItemText(13, _translate("serial_ui", "115200"))
        self.comBaudcomboBox.setItemText(14, _translate("serial_ui", "128000"))
        self.comBaudcomboBox.setItemText(15, _translate("serial_ui", "230400"))
        self.comBaudcomboBox.setItemText(16, _translate("serial_ui", "256000"))
        self.comBaudcomboBox.setItemText(17, _translate("serial_ui", "512000"))
        self.comBaudcomboBox.setItemText(18, _translate("serial_ui", "1000000"))
        self.comBaudcomboBox.setItemText(19, _translate("serial_ui", "2000000"))
        self.comBaudcomboBox.setItemText(20, _translate("serial_ui", "新建项目"))
        self.comOpenpushButton.setText(_translate("serial_ui", "打开串口"))
        self.label_3.setText(_translate("serial_ui", "数据位"))
        self.label_4.setText(_translate("serial_ui", "停止位"))
        self.label_5.setText(_translate("serial_ui", "校验位"))
        self.label_6.setText(_translate("serial_ui", "流控制"))
        self.comBitlencomboBox.setItemText(0, _translate("serial_ui", "8"))
        self.comBitlencomboBox.setItemText(1, _translate("serial_ui", "7"))
        self.comBitlencomboBox.setItemText(2, _translate("serial_ui", "6"))
        self.comBitlencomboBox.setItemText(3, _translate("serial_ui", "5"))
        self.comStoplencomboBox.setItemText(0, _translate("serial_ui", "1"))
        self.comStoplencomboBox.setItemText(1, _translate("serial_ui", "1.5"))
        self.comStoplencomboBox.setItemText(2, _translate("serial_ui", "2"))
        self.comCheckcomboBox.setItemText(0, _translate("serial_ui", "None"))
        self.comCheckcomboBox.setItemText(1, _translate("serial_ui", "Odd"))
        self.comCheckcomboBox.setItemText(2, _translate("serial_ui", "Even"))
        self.comCheckcomboBox.setItemText(3, _translate("serial_ui", "Mark"))
        self.comCheckcomboBox.setItemText(4, _translate("serial_ui", "Space"))
        self.comFlowCtlcomboBox.setItemText(0, _translate("serial_ui", "None"))
        self.comFlowCtlcomboBox.setItemText(1, _translate("serial_ui", "Software"))
        self.comFlowCtlcomboBox.setItemText(2, _translate("serial_ui", "Hardware"))
        self.comSendpushButton.setText(_translate("serial_ui", "发送"))
        self.comSendHexcheckBox.setText(_translate("serial_ui", "HEX发送"))
        self.comOpenFilepushButton.setText(_translate("serial_ui", "打开文件"))
        self.comSendFilepushButton.setText(_translate("serial_ui", "发送文件"))
        self.comFileSendStoppushButton.setText(_translate("serial_ui", "停止"))
        self.comTimingSendcheckBox.setText(_translate("serial_ui", "定时发送"))
        self.label_9.setText(_translate("serial_ui", "ms"))
        self.comSendEntercheckBox.setText(_translate("serial_ui", "加回车换行"))
        self.label_10.setText(_translate("serial_ui", "第"))
        self.label_11.setText(_translate("serial_ui", "<html><head/><body><p>字节至</p></body></html>"))
        self.comCheckcomboBox_2.setItemText(0, _translate("serial_ui", "末尾"))
        self.label_12.setText(_translate("serial_ui", "<html><head/><body><p>加校验</p></body></html>"))
        self.comCheckWaycomboBox.setItemText(0, _translate("serial_ui", "末尾"))
        self.comCheckRestextBrowser.setHtml(_translate("serial_ui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
