# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guis/interface.ui'
#
# Created: Wed Jul 12 14:12:22 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(681, 638)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Tabwi = QtGui.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Tabwi.setFont(font)
        self.Tabwi.setTabPosition(QtGui.QTabWidget.North)
        self.Tabwi.setTabShape(QtGui.QTabWidget.Rounded)
        self.Tabwi.setObjectName("Tabwi")
        self.program_text = QtGui.QWidget()
        self.program_text.setObjectName("program_text")
        self.horizontalLayout = QtGui.QHBoxLayout(self.program_text)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtGui.QLabel(self.program_text)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.plainTextEdit_2 = QtGui.QPlainTextEdit(self.program_text)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.verticalLayout_6.addWidget(self.plainTextEdit_2)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.camera = QtGui.QFrame(self.program_text)
        self.camera.setMinimumSize(QtCore.QSize(320, 240))
        self.camera.setMaximumSize(QtCore.QSize(320, 240))
        self.camera.setFrameShape(QtGui.QFrame.StyledPanel)
        self.camera.setFrameShadow(QtGui.QFrame.Raised)
        self.camera.setObjectName("camera")
        self.verticalLayout_5.addWidget(self.camera)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_3 = QtGui.QPushButton(self.program_text)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_5.addWidget(self.pushButton_3)
        self.pushButton_4 = QtGui.QPushButton(self.program_text)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_5.addWidget(self.pushButton_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.Tabwi.addTab(self.program_text, "")
        self.program_visual = QtGui.QWidget()
        self.program_visual.setObjectName("program_visual")
        self.gridLayout = QtGui.QGridLayout(self.program_visual)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtGui.QSplitter(self.program_visual)
        self.splitter.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.tabWidget_2 = QtGui.QTabWidget(self.splitter)
        self.tabWidget_2.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(50)
        font.setItalic(False)
        font.setStrikeOut(False)
        font.setBold(False)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setTabPosition(QtGui.QTabWidget.West)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.control = QtGui.QWidget()
        self.control.setObjectName("control")
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.control)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.tableControl = QtGui.QTableWidget(self.control)
        self.tableControl.setObjectName("tableControl")
        self.tableControl.setColumnCount(0)
        self.tableControl.setRowCount(0)
        self.verticalLayout_12.addWidget(self.tableControl)
        self.tabWidget_2.addTab(self.control, "")
        self.move = QtGui.QWidget()
        self.move.setObjectName("move")
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.move)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.tableMotor = QtGui.QTableWidget(self.move)
        self.tableMotor.setObjectName("tableMotor")
        self.tableMotor.setColumnCount(0)
        self.tableMotor.setRowCount(0)
        self.verticalLayout_11.addWidget(self.tableMotor)
        self.tabWidget_2.addTab(self.move, "")
        self.sensors = QtGui.QWidget()
        self.sensors.setObjectName("sensors")
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.sensors)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.tablePerceptual = QtGui.QTableWidget(self.sensors)
        self.tablePerceptual.setObjectName("tablePerceptual")
        self.tablePerceptual.setColumnCount(0)
        self.tablePerceptual.setRowCount(0)
        self.verticalLayout_10.addWidget(self.tablePerceptual)
        self.tabWidget_2.addTab(self.sensors, "")
        self.operators = QtGui.QWidget()
        self.operators.setObjectName("operators")
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.operators)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.tablePropioperceptive = QtGui.QTableWidget(self.operators)
        self.tablePropioperceptive.setObjectName("tablePropioperceptive")
        self.tablePropioperceptive.setColumnCount(0)
        self.tablePropioperceptive.setRowCount(0)
        self.verticalLayout_9.addWidget(self.tablePropioperceptive)
        self.tabWidget_2.addTab(self.operators, "")
        self.vars = QtGui.QWidget()
        self.vars.setObjectName("vars")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.vars)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tableOperadores = QtGui.QTableWidget(self.vars)
        self.tableOperadores.setObjectName("tableOperadores")
        self.tableOperadores.setColumnCount(0)
        self.tableOperadores.setRowCount(0)
        self.verticalLayout_7.addWidget(self.tableOperadores)
        self.tabWidget_2.addTab(self.vars, "")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_6 = QtGui.QPushButton(self.tab)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_5 = QtGui.QPushButton(self.tab)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.tableVariables = QtGui.QTableWidget(self.tab)
        self.tableVariables.setObjectName("tableVariables")
        self.tableVariables.setColumnCount(0)
        self.tableVariables.setRowCount(0)
        self.verticalLayout.addWidget(self.tableVariables)
        self.tabWidget_2.addTab(self.tab, "")
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtGui.QFrame(self.layoutWidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3.addWidget(self.frame)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton = QtGui.QPushButton(self.layoutWidget)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 27))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        self.Tabwi.addTab(self.program_visual, "")
        self.horizontalLayout_2.addWidget(self.Tabwi)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 681, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionHola = QtGui.QAction(MainWindow)
        self.actionHola.setObjectName("actionHola")
        self.actionCreate_New_block = QtGui.QAction(MainWindow)
        self.actionCreate_New_block.setObjectName("actionCreate_New_block")
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionOpen_Proyect = QtGui.QAction(MainWindow)
        self.actionOpen_Proyect.setObjectName("actionOpen_Proyect")
        self.actionSave_As = QtGui.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.menuFile.addAction(self.actionCreate_New_block)
        self.menuFile.addAction(self.actionOpen_Proyect)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.Tabwi.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.Tabwi.setWhatsThis(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>H</p><p><br/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Program", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("MainWindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.Tabwi.setTabText(self.Tabwi.indexOf(self.program_text), QtGui.QApplication.translate("MainWindow", "Text Code", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.control), QtGui.QApplication.translate("MainWindow", "Control", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.move), QtGui.QApplication.translate("MainWindow", "Motor", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.sensors), QtGui.QApplication.translate("MainWindow", "Perceptual", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.operators), QtGui.QApplication.translate("MainWindow", "Proprioceptive", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.vars), QtGui.QApplication.translate("MainWindow", "Operators", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(QtGui.QApplication.translate("MainWindow", "Add List", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("MainWindow", "Add Variable", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Variables", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.Tabwi.setTabText(self.Tabwi.indexOf(self.program_visual), QtGui.QApplication.translate("MainWindow", "LearnBlock", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHola.setText(QtGui.QApplication.translate("MainWindow", "Añadir Nueva Metodo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCreate_New_block.setText(QtGui.QApplication.translate("MainWindow", "Create New block", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save Proyect", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_Proyect.setText(QtGui.QApplication.translate("MainWindow", "Open Proyect", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_As.setText(QtGui.QApplication.translate("MainWindow", "Save As", None, QtGui.QApplication.UnicodeUTF8))

