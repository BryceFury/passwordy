# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/AppleUser/Downloads/PyMove/Python/passwordytemp/mainwindowops.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 61)
        MainWindow.setStyleSheet("#options_frame {\n"
"background: #232532;\n"
"border: None;\n"
"}\n"
"\n"
"#checks_frame {\n"
"border: None;\n"
"}\n"
"\n"
"#checks_frame QCheckBox {\n"
"color: #FFFFFF;\n"
"font: 10px;\n"
"border: None;\n"
"}\n"
"\n"
"#case_frame {\n"
"border: None;\n"
"}\n"
"\n"
"#characters_frame {\n"
"border: None;\n"
"}\n"
"\n"
"#spins_frame  {\n"
"border: None;\n"
"}\n"
"\n"
"#spins_frame  QLabel {\n"
"font: 10px;\n"
"qproperty-alignment: AlignCenter;\n"
"}\n"
"\n"
"#spins_frame  QSpinBox {\n"
"font: 10px;\n"
"qproperty-alignment: AlignCenter;\n"
"color: #232532;\n"
"}\n"
"\n"
"#spins_frame {\n"
"border: None;\n"
"max-width:250px;\n"
"max-height:50px;\n"
"min-width:225px;\n"
"min-height:50px;\n"
"}\n"
"\n"
"#labels_frame  {\n"
"border: None;\n"
"}\n"
"\n"
"#characters_label_frame  {\n"
"border: None;\n"
"}\n"
"\n"
"#passwords_label_frame  {\n"
"border: None;\n"
"}\n"
"\n"
"#spin_boxes_frame {\n"
"border: None;\n"
"}\n"
"\n"
"\n"
"#close_button_frame {\n"
"border: None;\n"
"}\n"
"\n"
"#close_options_button {\n"
"text-align:center;\n"
"font: 18px;\n"
"color: #FFFFFF;\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 25px;\n"
"max-width:50px;\n"
"max-height:50px;\n"
"min-width:50px;\n"
"min-height:50px;\n"
"}\n"
"\n"
"#close_options_button:hover {\n"
"color: #59F3D7;\n"
"}\n"
"\n"
"QLabel {\n"
"color: #FFFFFF;\n"
"font: 18px;\n"
"}\n"
"\n"
"\n"
"")
        self.options_frame = QtWidgets.QWidget(MainWindow)
        self.options_frame.setObjectName("options_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.options_frame)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checks_frame = QtWidgets.QFrame(self.options_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checks_frame.sizePolicy().hasHeightForWidth())
        self.checks_frame.setSizePolicy(sizePolicy)
        self.checks_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.checks_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.checks_frame.setObjectName("checks_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.checks_frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.characters_frame = QtWidgets.QFrame(self.checks_frame)
        self.characters_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.characters_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.characters_frame.setObjectName("characters_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.characters_frame)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBox_3 = QtWidgets.QCheckBox(self.characters_frame)
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_4.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.characters_frame)
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_4.addWidget(self.checkBox_4)
        self.horizontalLayout.addWidget(self.characters_frame)
        self.case_frame = QtWidgets.QFrame(self.checks_frame)
        self.case_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.case_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.case_frame.setObjectName("case_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.case_frame)
        self.verticalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.checkBox = QtWidgets.QCheckBox(self.case_frame)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_5.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.case_frame)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_5.addWidget(self.checkBox_2)
        self.horizontalLayout.addWidget(self.case_frame)
        self.horizontalLayout_2.addWidget(self.checks_frame)
        self.spins_frame = QtWidgets.QFrame(self.options_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spins_frame.sizePolicy().hasHeightForWidth())
        self.spins_frame.setSizePolicy(sizePolicy)
        self.spins_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.spins_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.spins_frame.setObjectName("spins_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.spins_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labels_frame = QtWidgets.QFrame(self.spins_frame)
        self.labels_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labels_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.labels_frame.setObjectName("labels_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.labels_frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.characters_label_frame = QtWidgets.QFrame(self.labels_frame)
        self.characters_label_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.characters_label_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.characters_label_frame.setObjectName("characters_label_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.characters_label_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.characters_label = QtWidgets.QLabel(self.characters_label_frame)
        self.characters_label.setObjectName("characters_label")
        self.verticalLayout_3.addWidget(self.characters_label)
        self.horizontalLayout_4.addWidget(self.characters_label_frame)
        self.passwords_label_frame = QtWidgets.QFrame(self.labels_frame)
        self.passwords_label_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.passwords_label_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.passwords_label_frame.setObjectName("passwords_label_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.passwords_label_frame)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.passwords_label = QtWidgets.QLabel(self.passwords_label_frame)
        self.passwords_label.setObjectName("passwords_label")
        self.horizontalLayout_5.addWidget(self.passwords_label)
        self.horizontalLayout_4.addWidget(self.passwords_label_frame)
        self.verticalLayout.addWidget(self.labels_frame)
        self.spin_boxes_frame = QtWidgets.QFrame(self.spins_frame)
        self.spin_boxes_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.spin_boxes_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.spin_boxes_frame.setObjectName("spin_boxes_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.spin_boxes_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.spinBox = QtWidgets.QSpinBox(self.spin_boxes_frame)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(64)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_3.addWidget(self.spinBox)
        self.spinBox_2 = QtWidgets.QSpinBox(self.spin_boxes_frame)
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_3.addWidget(self.spinBox_2)
        self.verticalLayout.addWidget(self.spin_boxes_frame)
        self.horizontalLayout_2.addWidget(self.spins_frame)
        self.close_button_frame = QtWidgets.QFrame(self.options_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close_button_frame.sizePolicy().hasHeightForWidth())
        self.close_button_frame.setSizePolicy(sizePolicy)
        self.close_button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.close_button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.close_button_frame.setObjectName("close_button_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.close_button_frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.close_options_button = QtWidgets.QPushButton(self.close_button_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close_options_button.sizePolicy().hasHeightForWidth())
        self.close_options_button.setSizePolicy(sizePolicy)
        self.close_options_button.setObjectName("close_options_button")
        self.verticalLayout_2.addWidget(self.close_options_button)
        self.horizontalLayout_2.addWidget(self.close_button_frame)
        MainWindow.setCentralWidget(self.options_frame)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox_3.setText(_translate("MainWindow", "Numbers"))
        self.checkBox_4.setText(_translate("MainWindow", "Specials"))
        self.checkBox.setText(_translate("MainWindow", "Lowercase"))
        self.checkBox_2.setText(_translate("MainWindow", "Uppercase"))
        self.characters_label.setText(_translate("MainWindow", "Number of Characters"))
        self.passwords_label.setText(_translate("MainWindow", "Number of Passwords"))
        self.close_options_button.setText(_translate("MainWindow", "X"))

