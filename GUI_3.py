import shutil
import sys
# from tkinter import Image
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import cv2 as cv
import os
import os.path
from shutil import move


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(1169, 767)
        Form.setMinimumSize(QtCore.QSize(1169, 767))
        Form.setMaximumSize(QtCore.QSize(1169, 767))

        self.capture = QtWidgets.QPushButton(Form)
        self.capture.setGeometry(QtCore.QRect(20, 510, 191, 31))
        self.capture.setObjectName("capture")
        self.capture.clicked.connect(self.DataCapture)

        self.image_feed = QtWidgets.QLabel(Form)
        self.image_feed.setGeometry(QtCore.QRect(9, 9, 640, 480))
        self.image_feed.setMinimumSize(QtCore.QSize(640, 480))
        self.image_feed.setMaximumSize(QtCore.QSize(640, 480))
        self.image_feed.setText("")
        self.image_feed.setScaledContents(True)
        self.image_feed.setObjectName("image_feed")

        self.live_prediction = QtWidgets.QRadioButton(Form)
        self.live_prediction.setGeometry(QtCore.QRect(720, 120, 121, 31))
        self.live_prediction.setObjectName("live_prediction")

        self.capture_2 = QtWidgets.QPushButton(Form)
        self.capture_2.setGeometry(QtCore.QRect(220, 510, 191, 31))
        self.capture_2.setObjectName("capture_2")
        self.capture_2.clicked.connect(self.CancelFeed)

        self.accuracy = QtWidgets.QTextBrowser(Form)
        self.accuracy.setGeometry(QtCore.QRect(580, 610, 241, 31))
        self.accuracy.setObjectName("accuracy")

        self.epochs = QtWidgets.QLineEdit(Form)
        self.epochs.setGeometry(QtCore.QRect(580, 500, 241, 31))
        self.epochs.setObjectName("epochs")

        self.progressBar_2 = QtWidgets.QProgressBar(Form)
        self.progressBar_2.setGeometry(QtCore.QRect(930, 500, 241, 31))
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")

        self.model_name = QtWidgets.QLineEdit(Form)
        self.model_name.setGeometry(QtCore.QRect(580, 720, 371, 31))
        self.model_name.setObjectName("model_name")

        self.count = QtWidgets.QTextBrowser(Form)
        self.count.setGeometry(QtCore.QRect(90, 700, 241, 31))
        self.count.setObjectName("count")

        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(450, 510, 20, 261))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.loss = QtWidgets.QTextBrowser(Form)
        self.loss.setGeometry(QtCore.QRect(580, 660, 241, 31))
        self.loss.setObjectName("loss")

        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(480, 670, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 590, 52, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(480, 510, 45, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 640, 33, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 710, 38, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(480, 620, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(850, 510, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(480, 730, 72, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.class_name = QtWidgets.QLineEdit(Form)
        self.class_name.setGeometry(QtCore.QRect(90, 640, 241, 31))
        self.class_name.setObjectName("class_name")

        self.DatasetLineEdit = QtWidgets.QLineEdit(Form)
        self.DatasetLineEdit.setGeometry(QtCore.QRect(90, 580, 241, 31))
        self.DatasetLineEdit.setObjectName("Dataset")

        self.evaluate = QtWidgets.QPushButton(Form)
        self.evaluate.setGeometry(QtCore.QRect(730, 560, 91, 31))
        self.evaluate.setObjectName("evaluate")

        self.load_model = QtWidgets.QPushButton(Form)
        self.load_model.setGeometry(QtCore.QRect(1020, 720, 101, 31))
        self.load_model.setObjectName("load_model")

        self.train = QtWidgets.QPushButton(Form)
        self.train.setGeometry(QtCore.QRect(580, 560, 91, 31))
        self.train.setObjectName("train")

        self.save_model = QtWidgets.QPushButton(Form)
        self.save_model.setGeometry(QtCore.QRect(1020, 680, 101, 31))
        self.save_model.setObjectName("save_model")

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(720, 180, 65, 16))

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(720, 260, 71, 16))

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.prediction = QtWidgets.QTextBrowser(Form)
        self.prediction.setGeometry(QtCore.QRect(807, 170, 341, 41))
        self.prediction.setObjectName("prediction")

        self.confidence = QtWidgets.QTextBrowser(Form)
        self.confidence.setGeometry(QtCore.QRect(810, 240, 341, 41))
        self.confidence.setObjectName("confidence")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.Worker1 = worker1()
        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        self.Worker1.CountUpdate.connect(self.CountUpdateSlot)

    def ImageUpdateSlot(self, Image):
        self.image_feed.setPixmap(QPixmap.fromImage(Image))

    def CountUpdateSlot(self, value):
        self.count.append(str(value))

    def CancelFeed(self):
        self.Worker1.stop()

    def DataCapture(self):
        print(
            f"Data of class \"{self.FetchClass()}\" for dataset \"{self.FetchDataset()}\" Captured")
        cwd_path = os.getcwd()
        DatasetDir = str(self.FetchDataset())
        path = os.path.join(cwd_path, DatasetDir)
        path2 = os.path.join(path, str(self.FetchClass()))
        # print(path)
        # print(path2)
        if os.path.exists(path):
            # print("dataset dir found")
            if os.path.exists(path2):
                # print("class found")
                self.Worker1.InstanceInitiate(path2)

            else:
                # print("class not found")
                os.mkdir(path2)
                self.Worker1.InstanceInitiate(path2)

        else:
            # print("dataset dir not found")
            os.mkdir(path)
            os.mkdir(path2)
            self.Worker1.InstanceInitiate(path2)

    def FetchClass(self):
        return(self.class_name.text())

    def FetchDataset(self):
        return(self.DatasetLineEdit.text())

    def FetchEpoch(self):
        return(self.epochs.text())

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate(
            "Form", "TATA_Motors-Model trainer and Predictor"))
        self.capture.setText(_translate("Form", "Capture"))
        self.live_prediction.setText(_translate("Form", "LIVE PREDICTION"))
        self.capture_2.setText(_translate("Form", "Cancel"))
        self.label_11.setText(_translate("Form", "Loss"))
        self.label.setText(_translate("Form", "Dataset"))
        self.label_5.setText(_translate("Form", "Epochs"))
        self.label_2.setText(_translate("Form", "Class"))
        self.label_3.setText(_translate("Form", "Count"))
        self.label_8.setText(_translate("Form", "Accuracy"))
        self.label_7.setText(_translate("Form", "Progress"))
        self.label_9.setText(_translate("Form", "Model path"))
        self.evaluate.setText(_translate("Form", "Evaluate"))
        self.load_model.setText(_translate("Form", "Load model"))
        self.train.setText(_translate("Form", "Train"))
        self.save_model.setText(_translate("Form", "Save model"))
        self.label_4.setText(_translate("Form", "Prediction"))
        self.label_10.setText(_translate("Form", "Confidence"))


class worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)
    CountUpdate = pyqtSignal(int)

    def run(self):
        self.ThreadActive = True
        self.instance = False
        self.cnt = 0
        self.path = ''
        self.path_prev=''
        capture = cv.VideoCapture(0)
        while self.ThreadActive:
            ret, frame = capture.read()
            if ret:
                # print(self.instance)
                if self.instance:
                    if (self.path_prev==self.path):
                        pass
                    else:
                        self.cnt=0
                    cv.imwrite("image_no" + str(self.cnt) + ".jpg", frame)
                    cwd = os.getcwd()
                    impath = os.path.join(
                        cwd, ("image_no" + str(self.cnt) + ".jpg"))
                    shutil.move(impath, self.path)
                    self.instance = False
                    self.cnt += 1
                    self.path_prev=self.path
                    self.CountUpdate.emit(self.cnt)

                frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
                flip_frame = cv.flip(frame, 1)
                ConvertedFrame = QImage(
                    flip_frame.data, flip_frame.shape[1], flip_frame.shape[0], QImage.Format_RGB888)
                pic = ConvertedFrame.scaled(640, 480, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(pic)
            else:
                break

    def stop(self):
        self.ThreadActive = False

    def InstanceInitiate(self, path2):
        self.instance = True
        self.path = path2
        # print(path2)

class worker2(QThread): #Training Thread
    
    def train_model():
        pass
        

# class worker3(QThread): #Live prediction Thread
    # pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
