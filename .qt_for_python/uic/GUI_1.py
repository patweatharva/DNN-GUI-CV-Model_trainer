# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI_1.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(1169, 767)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)

        self.verticalLayout_3.addWidget(self.label_4)

        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.verticalLayout_3.addWidget(self.label_10)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.prediction = QTextBrowser(Form)
        self.prediction.setObjectName(u"prediction")

        self.verticalLayout_4.addWidget(self.prediction)

        self.confidence = QTextBrowser(Form)
        self.confidence.setObjectName(u"confidence")

        self.verticalLayout_4.addWidget(self.confidence)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.train = QPushButton(Form)
        self.train.setObjectName(u"train")

        self.verticalLayout_5.addWidget(self.train)

        self.evaluate = QPushButton(Form)
        self.evaluate.setObjectName(u"evaluate")

        self.verticalLayout_5.addWidget(self.evaluate)

        self.load_model = QPushButton(Form)
        self.load_model.setObjectName(u"load_model")

        self.verticalLayout_5.addWidget(self.load_model)

        self.save_model = QPushButton(Form)
        self.save_model.setObjectName(u"save_model")

        self.verticalLayout_5.addWidget(self.save_model)


        self.gridLayout.addLayout(self.verticalLayout_5, 5, 2, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout.addWidget(self.label_3)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout.addWidget(self.label_5)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.verticalLayout.addWidget(self.label_8)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.verticalLayout.addWidget(self.label_7)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.verticalLayout.addWidget(self.label_9)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.class_name = QLineEdit(Form)
        self.class_name.setObjectName(u"class_name")

        self.verticalLayout_2.addWidget(self.class_name)

        self.count = QLineEdit(Form)
        self.count.setObjectName(u"count")

        self.verticalLayout_2.addWidget(self.count)

        self.epochs = QLineEdit(Form)
        self.epochs.setObjectName(u"epochs")

        self.verticalLayout_2.addWidget(self.epochs)

        self.loss = QLineEdit(Form)
        self.loss.setObjectName(u"loss")

        self.verticalLayout_2.addWidget(self.loss)

        self.accuracy = QLineEdit(Form)
        self.accuracy.setObjectName(u"accuracy")

        self.verticalLayout_2.addWidget(self.accuracy)

        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout_2.addWidget(self.progressBar)

        self.model_path = QLineEdit(Form)
        self.model_path.setObjectName(u"model_path")

        self.verticalLayout_2.addWidget(self.model_path)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 2)

        self.capture = QPushButton(Form)
        self.capture.setObjectName(u"capture")

        self.gridLayout.addWidget(self.capture, 2, 0, 1, 1)

        self.image_feed = QLabel(Form)
        self.image_feed.setObjectName(u"image_feed")
        self.image_feed.setScaledContents(True)

        self.gridLayout.addWidget(self.image_feed, 0, 0, 2, 1)

        self.cancel = QPushButton(Form)
        self.cancel.setObjectName(u"cancel")

        self.gridLayout.addWidget(self.cancel, 3, 0, 1, 1)

        self.live_demo = QRadioButton(Form)
        self.live_demo.setObjectName(u"live_demo")

        self.gridLayout.addWidget(self.live_demo, 0, 1, 1, 2)

        self.dataset_name = QLineEdit(Form)
        self.dataset_name.setObjectName(u"dataset_name")

        self.gridLayout.addWidget(self.dataset_name, 4, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"TATA_Motors-Model trainer and Predictor", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Prediction", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Confidence", None))
        self.train.setText(QCoreApplication.translate("Form", u"Train", None))
        self.evaluate.setText(QCoreApplication.translate("Form", u"Evaluate", None))
        self.load_model.setText(QCoreApplication.translate("Form", u"Load model", None))
        self.save_model.setText(QCoreApplication.translate("Form", u"Save model", None))
        self.label.setText(QCoreApplication.translate("Form", u"Dataset", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Class", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Count", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Epochs", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Accuracy", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Progress", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Model path", None))
        self.capture.setText(QCoreApplication.translate("Form", u"Capture", None))
        self.image_feed.setText("")
        self.cancel.setText(QCoreApplication.translate("Form", u"cancel", None))
        self.live_demo.setText(QCoreApplication.translate("Form", u"LIVE DEMO", None))
    # retranslateUi

