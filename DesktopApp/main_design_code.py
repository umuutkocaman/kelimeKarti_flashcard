# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(885, 844)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gbUploadFile = QtWidgets.QGroupBox(self.centralwidget)
        self.gbUploadFile.setGeometry(QtCore.QRect(10, 10, 181, 121))
        self.gbUploadFile.setObjectName("gbUploadFile")
        self.btnBrowse = QtWidgets.QPushButton(self.gbUploadFile)
        self.btnBrowse.setGeometry(QtCore.QRect(60, 30, 75, 23))
        self.btnBrowse.setObjectName("btnBrowse")
        self.lblBrowseRead = QtWidgets.QLabel(self.gbUploadFile)
        self.lblBrowseRead.setGeometry(QtCore.QRect(10, 70, 161, 41))
        self.lblBrowseRead.setText("")
        self.lblBrowseRead.setObjectName("lblBrowseRead")
        self.gbGame = QtWidgets.QGroupBox(self.centralwidget)
        self.gbGame.setGeometry(QtCore.QRect(200, 20, 591, 331))
        self.gbGame.setObjectName("gbGame")
        self.layoutWidget = QtWidgets.QWidget(self.gbGame)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 200, 411, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnAsk = QtWidgets.QPushButton(self.layoutWidget)
        self.btnAsk.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAsk.sizePolicy().hasHeightForWidth())
        self.btnAsk.setSizePolicy(sizePolicy)
        self.btnAsk.setObjectName("btnAsk")
        self.horizontalLayout_2.addWidget(self.btnAsk)
        self.btnCheck = QtWidgets.QPushButton(self.layoutWidget)
        self.btnCheck.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCheck.sizePolicy().hasHeightForWidth())
        self.btnCheck.setSizePolicy(sizePolicy)
        self.btnCheck.setMaximumSize(QtCore.QSize(1677721, 16777215))
        self.btnCheck.setObjectName("btnCheck")
        self.horizontalLayout_2.addWidget(self.btnCheck)
        self.btnFinish = QtWidgets.QPushButton(self.layoutWidget)
        self.btnFinish.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnFinish.sizePolicy().hasHeightForWidth())
        self.btnFinish.setSizePolicy(sizePolicy)
        self.btnFinish.setObjectName("btnFinish")
        self.horizontalLayout_2.addWidget(self.btnFinish)
        self.lblAnswer = QtWidgets.QLabel(self.gbGame)
        self.lblAnswer.setGeometry(QtCore.QRect(370, 130, 201, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblAnswer.setFont(font)
        self.lblAnswer.setText("")
        self.lblAnswer.setObjectName("lblAnswer")
        self.wordInput = QtWidgets.QLineEdit(self.gbGame)
        self.wordInput.setGeometry(QtCore.QRect(100, 130, 261, 51))
        self.wordInput.setObjectName("wordInput")
        self.lblReply = QtWidgets.QLabel(self.gbGame)
        self.lblReply.setGeometry(QtCore.QRect(10, 140, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblReply.setFont(font)
        self.lblReply.setObjectName("lblReply")
        self.lblQuestionWord = QtWidgets.QLabel(self.gbGame)
        self.lblQuestionWord.setGeometry(QtCore.QRect(100, 80, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblQuestionWord.setFont(font)
        self.lblQuestionWord.setText("")
        self.lblQuestionWord.setObjectName("lblQuestionWord")
        self.lblResult = QtWidgets.QLabel(self.gbGame)
        self.lblResult.setGeometry(QtCore.QRect(100, 260, 301, 51))
        self.lblResult.setText("")
        self.lblResult.setObjectName("lblResult")
        self.gbType = QtWidgets.QGroupBox(self.gbGame)
        self.gbType.setGeometry(QtCore.QRect(80, 20, 451, 61))
        self.gbType.setObjectName("gbType")
        self.layoutWidget1 = QtWidgets.QWidget(self.gbType)
        self.layoutWidget1.setGeometry(QtCore.QRect(60, 10, 321, 41))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rbWordDefinition = QtWidgets.QRadioButton(self.layoutWidget1)
        self.rbWordDefinition.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.rbWordDefinition.setFont(font)
        self.rbWordDefinition.setObjectName("rbWordDefinition")
        self.horizontalLayout.addWidget(self.rbWordDefinition)
        self.rbDefinitionWord = QtWidgets.QRadioButton(self.layoutWidget1)
        self.rbDefinitionWord.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.rbDefinitionWord.setFont(font)
        self.rbDefinitionWord.setObjectName("rbDefinitionWord")
        self.horizontalLayout.addWidget(self.rbDefinitionWord)
        self.gbAddDeleteWord_SaveFile = QtWidgets.QGroupBox(self.centralwidget)
        self.gbAddDeleteWord_SaveFile.setGeometry(QtCore.QRect(10, 360, 781, 421))
        self.gbAddDeleteWord_SaveFile.setObjectName("gbAddDeleteWord_SaveFile")
        self.lblEnterFileName = QtWidgets.QLabel(self.gbAddDeleteWord_SaveFile)
        self.lblEnterFileName.setGeometry(QtCore.QRect(70, 280, 491, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblEnterFileName.setFont(font)
        self.lblEnterFileName.setObjectName("lblEnterFileName")
        self.layoutWidget_3 = QtWidgets.QWidget(self.gbAddDeleteWord_SaveFile)
        self.layoutWidget_3.setGeometry(QtCore.QRect(70, 170, 341, 30))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lblWord2 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblWord2.setFont(font)
        self.lblWord2.setObjectName("lblWord2")
        self.horizontalLayout_6.addWidget(self.lblWord2)
        self.etDeleteWord = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.etDeleteWord.setObjectName("etDeleteWord")
        self.horizontalLayout_6.addWidget(self.etDeleteWord)
        self.btnDelete = QtWidgets.QPushButton(self.layoutWidget_3)
        self.btnDelete.setEnabled(False)
        self.btnDelete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnDelete.setObjectName("btnDelete")
        self.horizontalLayout_6.addWidget(self.btnDelete)
        self.layoutWidget_4 = QtWidgets.QWidget(self.gbAddDeleteWord_SaveFile)
        self.layoutWidget_4.setGeometry(QtCore.QRect(70, 320, 591, 30))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lblFileName = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblFileName.setFont(font)
        self.lblFileName.setObjectName("lblFileName")
        self.horizontalLayout_7.addWidget(self.lblFileName)
        self.etFilneName = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.etFilneName.setObjectName("etFilneName")
        self.horizontalLayout_7.addWidget(self.etFilneName)
        self.btnSave = QtWidgets.QPushButton(self.layoutWidget_4)
        self.btnSave.setEnabled(False)
        self.btnSave.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout_7.addWidget(self.btnSave)
        self.lblDosyaKaydet = QtWidgets.QLabel(self.gbAddDeleteWord_SaveFile)
        self.lblDosyaKaydet.setGeometry(QtCore.QRect(70, 250, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblDosyaKaydet.setFont(font)
        self.lblDosyaKaydet.setObjectName("lblDosyaKaydet")
        self.lblDeleteWord = QtWidgets.QLabel(self.gbAddDeleteWord_SaveFile)
        self.lblDeleteWord.setGeometry(QtCore.QRect(70, 140, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblDeleteWord.setFont(font)
        self.lblDeleteWord.setObjectName("lblDeleteWord")
        self.lblWordDeleted = QtWidgets.QLabel(self.gbAddDeleteWord_SaveFile)
        self.lblWordDeleted.setGeometry(QtCore.QRect(70, 210, 571, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblWordDeleted.setFont(font)
        self.lblWordDeleted.setText("")
        self.lblWordDeleted.setObjectName("lblWordDeleted")
        self.lblFileSaved = QtWidgets.QLabel(self.gbAddDeleteWord_SaveFile)
        self.lblFileSaved.setGeometry(QtCore.QRect(70, 360, 591, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblFileSaved.setFont(font)
        self.lblFileSaved.setText("")
        self.lblFileSaved.setObjectName("lblFileSaved")
        self.lblWordAdded = QtWidgets.QLabel(self.gbAddDeleteWord_SaveFile)
        self.lblWordAdded.setGeometry(QtCore.QRect(70, 100, 581, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblWordAdded.setFont(font)
        self.lblWordAdded.setText("")
        self.lblWordAdded.setObjectName("lblWordAdded")
        self.layoutWidget_5 = QtWidgets.QWidget(self.gbAddDeleteWord_SaveFile)
        self.layoutWidget_5.setGeometry(QtCore.QRect(70, 60, 581, 30))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lblWord = QtWidgets.QLabel(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblWord.setFont(font)
        self.lblWord.setObjectName("lblWord")
        self.horizontalLayout_8.addWidget(self.lblWord)
        self.etAddWord = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.etAddWord.setObjectName("etAddWord")
        self.horizontalLayout_8.addWidget(self.etAddWord)
        self.lblDefinition = QtWidgets.QLabel(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblDefinition.setFont(font)
        self.lblDefinition.setObjectName("lblDefinition")
        self.horizontalLayout_8.addWidget(self.lblDefinition)
        self.etAddDefinition = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.etAddDefinition.setObjectName("etAddDefinition")
        self.horizontalLayout_8.addWidget(self.etAddDefinition)
        self.btnAdd = QtWidgets.QPushButton(self.layoutWidget_5)
        self.btnAdd.setEnabled(False)
        self.btnAdd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAdd.setObjectName("btnAdd")
        self.horizontalLayout_8.addWidget(self.btnAdd)
        self.lblKelimeEkle = QtWidgets.QLabel(self.gbAddDeleteWord_SaveFile)
        self.lblKelimeEkle.setGeometry(QtCore.QRect(70, 25, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblKelimeEkle.setFont(font)
        self.lblKelimeEkle.setObjectName("lblKelimeEkle")
        self.gbCreateFile = QtWidgets.QGroupBox(self.centralwidget)
        self.gbCreateFile.setGeometry(QtCore.QRect(10, 140, 181, 211))
        self.gbCreateFile.setObjectName("gbCreateFile")
        self.btnCreate = QtWidgets.QPushButton(self.gbCreateFile)
        self.btnCreate.setGeometry(QtCore.QRect(60, 30, 75, 23))
        self.btnCreate.setObjectName("btnCreate")
        self.lblFileCreated = QtWidgets.QLabel(self.gbCreateFile)
        self.lblFileCreated.setEnabled(True)
        self.lblFileCreated.setGeometry(QtCore.QRect(10, 70, 161, 121))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lblFileCreated.setFont(font)
        self.lblFileCreated.setMouseTracking(True)
        self.lblFileCreated.setTabletTracking(False)
        self.lblFileCreated.setAcceptDrops(False)
        self.lblFileCreated.setAutoFillBackground(False)
        self.lblFileCreated.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lblFileCreated.setText("")
        self.lblFileCreated.setTextFormat(QtCore.Qt.PlainText)
        self.lblFileCreated.setScaledContents(False)
        self.lblFileCreated.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblFileCreated.setWordWrap(True)
        self.lblFileCreated.setOpenExternalLinks(False)
        self.lblFileCreated.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.lblFileCreated.setObjectName("lblFileCreated")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 885, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.gbUploadFile.setTitle(_translate("MainWindow", "Upload File"))
        self.btnBrowse.setText(_translate("MainWindow", "Browse"))
        self.gbGame.setTitle(_translate("MainWindow", "Game"))
        self.btnAsk.setText(_translate("MainWindow", "ASK"))
        self.btnCheck.setText(_translate("MainWindow", "CHECK"))
        self.btnFinish.setText(_translate("MainWindow", "FINISH AND SHOW RESULT"))
        self.lblReply.setText(_translate("MainWindow", "REPLY:"))
        self.gbType.setTitle(_translate("MainWindow", "Type"))
        self.rbWordDefinition.setText(_translate("MainWindow", "Word -> Definition"))
        self.rbDefinitionWord.setText(_translate("MainWindow", "Definition -> Word"))
        self.gbAddDeleteWord_SaveFile.setTitle(_translate("MainWindow", "Add / Delete Word and File Save"))
        self.lblEnterFileName.setText(_translate("MainWindow", "Enter the filename with the .json extension"))
        self.lblWord2.setText(_translate("MainWindow", "Word"))
        self.btnDelete.setText(_translate("MainWindow", "Delete"))
        self.lblFileName.setText(_translate("MainWindow", "File Name"))
        self.btnSave.setText(_translate("MainWindow", "Save"))
        self.lblDosyaKaydet.setText(_translate("MainWindow", "File Save"))
        self.lblDeleteWord.setText(_translate("MainWindow", "Delete Word"))
        self.lblWord.setText(_translate("MainWindow", "Word:"))
        self.lblDefinition.setText(_translate("MainWindow", "Definition"))
        self.btnAdd.setText(_translate("MainWindow", "Add"))
        self.lblKelimeEkle.setText(_translate("MainWindow", "Add Word"))
        self.gbCreateFile.setTitle(_translate("MainWindow", "Create File"))
        self.btnCreate.setText(_translate("MainWindow", "Create"))
