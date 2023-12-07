# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Japanese Notes Study Buddy\Japanese-Notes-Study-Buddy\ui\TypeFlashCardWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TypeFlashCardWidget(object):
    def setupUi(self, TypeFlashCardWidget):
        TypeFlashCardWidget.setObjectName("TypeFlashCardWidget")
        TypeFlashCardWidget.resize(480, 640)
        TypeFlashCardWidget.setMinimumSize(QtCore.QSize(480, 640))
        TypeFlashCardWidget.setMaximumSize(QtCore.QSize(480, 640))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        TypeFlashCardWidget.setFont(font)
        TypeFlashCardWidget.setStyleSheet("background-color:rgb(30, 30, 30); color:white;")
        self.PassButton = QtWidgets.QPushButton(TypeFlashCardWidget)
        self.PassButton.setGeometry(QtCore.QRect(320, 570, 90, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PassButton.sizePolicy().hasHeightForWidth())
        self.PassButton.setSizePolicy(sizePolicy)
        self.PassButton.setMinimumSize(QtCore.QSize(90, 30))
        self.PassButton.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.PassButton.setFont(font)
        self.PassButton.setStyleSheet("background-color:rgb(20,80,20); border-radius:5px; border: 2px solid rgb(100,255,200);")
        self.PassButton.setObjectName("PassButton")
        self.FailButton = QtWidgets.QPushButton(TypeFlashCardWidget)
        self.FailButton.setGeometry(QtCore.QRect(60, 570, 90, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FailButton.sizePolicy().hasHeightForWidth())
        self.FailButton.setSizePolicy(sizePolicy)
        self.FailButton.setMinimumSize(QtCore.QSize(90, 30))
        self.FailButton.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.FailButton.setFont(font)
        self.FailButton.setStyleSheet("background-color:rgb(80,20,20); border-radius:5px; border: 2px solid rgb(255,200,100)")
        self.FailButton.setObjectName("FailButton")
        self.AnswerLabel = QtWidgets.QLabel(TypeFlashCardWidget)
        self.AnswerLabel.setGeometry(QtCore.QRect(70, 360, 341, 171))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.AnswerLabel.setFont(font)
        self.AnswerLabel.setStyleSheet("background-color:rgb(5,10,40); border: 2px solid rgb(30, 60, 120); border-radius:10px;")
        self.AnswerLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.AnswerLabel.setLineWidth(5)
        self.AnswerLabel.setTextFormat(QtCore.Qt.PlainText)
        self.AnswerLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.AnswerLabel.setWordWrap(True)
        self.AnswerLabel.setObjectName("AnswerLabel")
        self.line = QtWidgets.QFrame(TypeFlashCardWidget)
        self.line.setGeometry(QtCore.QRect(0, 320, 480, 10))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QtCore.QSize(480, 0))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.QuestionLabel = QtWidgets.QLabel(TypeFlashCardWidget)
        self.QuestionLabel.setGeometry(QtCore.QRect(70, 50, 341, 151))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.QuestionLabel.setFont(font)
        self.QuestionLabel.setStyleSheet("background-color:rgb(5,10,40); border: 2px solid rgb(30, 60, 120); border-radius:10px;")
        self.QuestionLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.QuestionLabel.setLineWidth(5)
        self.QuestionLabel.setTextFormat(QtCore.Qt.PlainText)
        self.QuestionLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.QuestionLabel.setWordWrap(True)
        self.QuestionLabel.setObjectName("QuestionLabel")
        self.lineEdit = QtWidgets.QLineEdit(TypeFlashCardWidget)
        self.lineEdit.setGeometry(QtCore.QRect(72, 239, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("background-color:black;\n"
"color:white;\n"
" border-radius: 5px;\n"
" border: 1px solid white;")
        self.lineEdit.setObjectName("lineEdit")
        self.FlipButton = QtWidgets.QPushButton(TypeFlashCardWidget)
        self.FlipButton.setGeometry(QtCore.QRect(190, 570, 90, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FlipButton.sizePolicy().hasHeightForWidth())
        self.FlipButton.setSizePolicy(sizePolicy)
        self.FlipButton.setMinimumSize(QtCore.QSize(90, 30))
        self.FlipButton.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.FlipButton.setFont(font)
        self.FlipButton.setStyleSheet("background-color:rgb(20,20,80); border-radius:5px; border: 2px solid rgb(100,200,255);")
        self.FlipButton.setObjectName("FlipButton")

        self.retranslateUi(TypeFlashCardWidget)
        QtCore.QMetaObject.connectSlotsByName(TypeFlashCardWidget)

    def retranslateUi(self, TypeFlashCardWidget):
        _translate = QtCore.QCoreApplication.translate
        TypeFlashCardWidget.setWindowTitle(_translate("TypeFlashCardWidget", "Review"))
        self.PassButton.setText(_translate("TypeFlashCardWidget", "Pass"))
        self.FailButton.setText(_translate("TypeFlashCardWidget", "Fail"))
        self.AnswerLabel.setText(_translate("TypeFlashCardWidget", "Answer"))
        self.QuestionLabel.setText(_translate("TypeFlashCardWidget", "Question"))
        self.FlipButton.setText(_translate("TypeFlashCardWidget", "Flip"))
