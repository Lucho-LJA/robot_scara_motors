# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/resourses/hmi.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1250, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1250, 700))
        MainWindow.setMaximumSize(QtCore.QSize(1250, 700))
        MainWindow.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1250, 700))
        self.tabWidget.setMinimumSize(QtCore.QSize(1250, 700))
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidgetPage1 = QtWidgets.QWidget()
        self.tabWidgetPage1.setObjectName("tabWidgetPage1")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tabWidgetPage1)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 10, 1202, 531))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setMinimumSize(QtCore.QSize(0, 25))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QtCore.QSize(1200, 0))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_9.setMinimumSize(QtCore.QSize(600, 300))
        self.label_9.setMaximumSize(QtCore.QSize(600, 300))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("src/resourses/celdaScara.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9, 0, QtCore.Qt.AlignHCenter)
        self.gridLayoutWidget = QtWidgets.QWidget(self.tabWidgetPage1)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(300, 540, 464, 120))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(150, 25))
        self.label_5.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setMinimumSize(QtCore.QSize(150, 25))
        self.label_6.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(150, 25))
        self.label_4.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QtWidgets.QWidget()
        self.tabWidgetPage2.setObjectName("tabWidgetPage2")
        self.label_10 = QtWidgets.QLabel(self.tabWidgetPage2)
        self.label_10.setGeometry(QtCore.QRect(0, 20, 1202, 25))
        self.label_10.setMinimumSize(QtCore.QSize(0, 25))
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tabWidgetPage2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 49, 1202, 16))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setMinimumSize(QtCore.QSize(1200, 2))
        self.line_2.setMaximumSize(QtCore.QSize(1200, 2))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.ind_table = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.ind_table.setGeometry(QtCore.QRect(519, 120, 150, 150))
        self.ind_table.setMinimumSize(QtCore.QSize(150, 150))
        self.ind_table.setMaximumSize(QtCore.QSize(150, 150))
        self.ind_table.setStyleSheet("border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(136, 138, 133);\n"
"border-radius: 75px;")
        self.ind_table.setObjectName("ind_table")
        self.line_6 = QtWidgets.QFrame(self.tabWidgetPage2)
        self.line_6.setGeometry(QtCore.QRect(800, 60, 16, 600))
        self.line_6.setMinimumSize(QtCore.QSize(16, 600))
        self.line_6.setMaximumSize(QtCore.QSize(16, 600))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.ind_element = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.ind_element.setGeometry(QtCore.QRect(460, 170, 50, 50))
        self.ind_element.setMinimumSize(QtCore.QSize(50, 50))
        self.ind_element.setMaximumSize(QtCore.QSize(50, 50))
        self.ind_element.setStyleSheet("border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(136, 138, 133);\n"
"")
        self.ind_element.setObjectName("ind_element")
        self.ind_scara1_4 = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.ind_scara1_4.setGeometry(QtCore.QRect(230, 160, 50, 100))
        self.ind_scara1_4.setStyleSheet("border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(136, 138, 133);")
        self.ind_scara1_4.setText("")
        self.ind_scara1_4.setObjectName("ind_scara1_4")
        self.ind_scara1_3 = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.ind_scara1_3.setGeometry(QtCore.QRect(230, 140, 100, 25))
        self.ind_scara1_3.setStyleSheet("border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(136, 138, 133);")
        self.ind_scara1_3.setText("")
        self.ind_scara1_3.setObjectName("ind_scara1_3")
        self.ind_scara1_2 = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.ind_scara1_2.setGeometry(QtCore.QRect(280, 120, 100, 25))
        self.ind_scara1_2.setStyleSheet("border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(136, 138, 133);")
        self.ind_scara1_2.setText("")
        self.ind_scara1_2.setObjectName("ind_scara1_2")
        self.ind_scara1_1 = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.ind_scara1_1.setGeometry(QtCore.QRect(380, 120, 25, 75))
        self.ind_scara1_1.setStyleSheet("border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(136, 138, 133);")
        self.ind_scara1_1.setText("")
        self.ind_scara1_1.setObjectName("ind_scara1_1")
        self.ind_banda = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.ind_banda.setGeometry(QtCore.QRect(50, 170, 91, 291))
        self.ind_banda.setStyleSheet("border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(136, 138, 133);")
        self.ind_banda.setObjectName("ind_banda")
        self.ind_scara2_4 = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.ind_scara2_4.setGeometry(QtCore.QRect(230, 530, 50, 100))
        self.ind_scara2_4.setStyleSheet("border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(136, 138, 133);")
        self.ind_scara2_4.setText("")
        self.ind_scara2_4.setObjectName("ind_scara2_4")
        self.ind_scara2_2 = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.ind_scara2_2.setGeometry(QtCore.QRect(280, 490, 100, 25))
        self.ind_scara2_2.setStyleSheet("border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(136, 138, 133);")
        self.ind_scara2_2.setText("")
        self.ind_scara2_2.setObjectName("ind_scara2_2")
        self.ind_scara2_3 = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.ind_scara2_3.setGeometry(QtCore.QRect(230, 510, 100, 25))
        self.ind_scara2_3.setStyleSheet("border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(136, 138, 133);")
        self.ind_scara2_3.setText("")
        self.ind_scara2_3.setObjectName("ind_scara2_3")
        self.ind_scara2_1 = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.ind_scara2_1.setGeometry(QtCore.QRect(380, 490, 25, 75))
        self.ind_scara2_1.setStyleSheet("border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(136, 138, 133);")
        self.ind_scara2_1.setText("")
        self.ind_scara2_1.setObjectName("ind_scara2_1")
        self.ind_class_1 = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.ind_class_1.setGeometry(QtCore.QRect(470, 490, 201, 41))
        self.ind_class_1.setStyleSheet("border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(136, 138, 133);")
        self.ind_class_1.setObjectName("ind_class_1")
        self.ind_class_2 = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.ind_class_2.setGeometry(QtCore.QRect(470, 590, 201, 41))
        self.ind_class_2.setStyleSheet("border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(136, 138, 133);")
        self.ind_class_2.setObjectName("ind_class_2")
        self.label_15 = QtWidgets.QLabel(self.tabWidgetPage2)
        self.label_15.setGeometry(QtCore.QRect(250, 90, 67, 17))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tabWidgetPage2)
        self.label_16.setGeometry(QtCore.QRect(250, 450, 67, 17))
        self.label_16.setObjectName("label_16")
        self.button_start = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.button_start.setGeometry(QtCore.QRect(970, 148, 175, 37))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_start.setFont(font)
        self.button_start.setObjectName("button_start")
        self.button_stop = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.button_stop.setEnabled(False)
        self.button_stop.setGeometry(QtCore.QRect(970, 240, 175, 38))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_stop.setFont(font)
        self.button_stop.setObjectName("button_stop")
        self.button_stop_emer = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.button_stop_emer.setGeometry(QtCore.QRect(970, 330, 175, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_stop_emer.setFont(font)
        self.button_stop_emer.setObjectName("button_stop_emer")
        self.tabWidget.addTab(self.tabWidgetPage2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.manual_1 = QtWidgets.QFrame(self.tab)
        self.manual_1.setEnabled(False)
        self.manual_1.setGeometry(QtCore.QRect(10, 150, 741, 491))
        self.manual_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.manual_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.manual_1.setObjectName("manual_1")
        self.groupBox_3 = QtWidgets.QGroupBox(self.manual_1)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 20, 261, 61))
        self.groupBox_3.setObjectName("groupBox_3")
        self.scara1_man = QtWidgets.QRadioButton(self.groupBox_3)
        self.scara1_man.setGeometry(QtCore.QRect(20, 30, 112, 23))
        self.scara1_man.setChecked(True)
        self.scara1_man.setObjectName("scara1_man")
        self.scara2_man = QtWidgets.QRadioButton(self.groupBox_3)
        self.scara2_man.setGeometry(QtCore.QRect(170, 30, 112, 23))
        self.scara2_man.setObjectName("scara2_man")
        self.label_23 = QtWidgets.QLabel(self.manual_1)
        self.label_23.setGeometry(QtCore.QRect(10, 120, 121, 17))
        self.label_23.setObjectName("label_23")
        self.button_bm_clock = QtWidgets.QPushButton(self.manual_1)
        self.button_bm_clock.setGeometry(QtCore.QRect(30, 140, 89, 25))
        self.button_bm_clock.setObjectName("button_bm_clock")
        self.button_bm_counter = QtWidgets.QPushButton(self.manual_1)
        self.button_bm_counter.setGeometry(QtCore.QRect(130, 140, 89, 25))
        self.button_bm_counter.setObjectName("button_bm_counter")
        self.button_bodym_counter = QtWidgets.QPushButton(self.manual_1)
        self.button_bodym_counter.setGeometry(QtCore.QRect(130, 200, 89, 25))
        self.button_bodym_counter.setObjectName("button_bodym_counter")
        self.button_bodym_clock = QtWidgets.QPushButton(self.manual_1)
        self.button_bodym_clock.setGeometry(QtCore.QRect(30, 200, 89, 25))
        self.button_bodym_clock.setObjectName("button_bodym_clock")
        self.label_24 = QtWidgets.QLabel(self.manual_1)
        self.label_24.setGeometry(QtCore.QRect(10, 180, 121, 17))
        self.label_24.setObjectName("label_24")
        self.button_lm_down = QtWidgets.QPushButton(self.manual_1)
        self.button_lm_down.setGeometry(QtCore.QRect(130, 260, 89, 25))
        self.button_lm_down.setObjectName("button_lm_down")
        self.button_lm_up = QtWidgets.QPushButton(self.manual_1)
        self.button_lm_up.setGeometry(QtCore.QRect(30, 260, 89, 25))
        self.button_lm_up.setObjectName("button_lm_up")
        self.label_25 = QtWidgets.QLabel(self.manual_1)
        self.label_25.setGeometry(QtCore.QRect(10, 240, 121, 17))
        self.label_25.setObjectName("label_25")
        self.button_act_stop = QtWidgets.QPushButton(self.manual_1)
        self.button_act_stop.setEnabled(False)
        self.button_act_stop.setGeometry(QtCore.QRect(130, 330, 89, 25))
        self.button_act_stop.setObjectName("button_act_stop")
        self.button_act_start = QtWidgets.QPushButton(self.manual_1)
        self.button_act_start.setGeometry(QtCore.QRect(30, 330, 89, 25))
        self.button_act_start.setObjectName("button_act_start")
        self.label_26 = QtWidgets.QLabel(self.manual_1)
        self.label_26.setGeometry(QtCore.QRect(10, 310, 121, 17))
        self.label_26.setObjectName("label_26")
        self.label = QtWidgets.QLabel(self.manual_1)
        self.label.setGeometry(QtCore.QRect(240, 120, 480, 300))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.button_home = QtWidgets.QPushButton(self.manual_1)
        self.button_home.setGeometry(QtCore.QRect(80, 370, 89, 25))
        self.button_home.setObjectName("button_home")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 39, 1202, 16))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.line_3 = QtWidgets.QFrame(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy)
        self.line_3.setMinimumSize(QtCore.QSize(1200, 2))
        self.line_3.setMaximumSize(QtCore.QSize(1200, 2))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_6.addWidget(self.line_3)
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(0, 10, 1202, 25))
        self.label_11.setMinimumSize(QtCore.QSize(0, 25))
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.line_7 = QtWidgets.QFrame(self.tab)
        self.line_7.setGeometry(QtCore.QRect(760, 90, 16, 550))
        self.line_7.setMinimumSize(QtCore.QSize(16, 550))
        self.line_7.setMaximumSize(QtCore.QSize(16, 600))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.button_manual = QtWidgets.QPushButton(self.tab)
        self.button_manual.setGeometry(QtCore.QRect(10, 60, 301, 25))
        self.button_manual.setObjectName("button_manual")
        self.label_22 = QtWidgets.QLabel(self.tab)
        self.label_22.setGeometry(QtCore.QRect(300, 100, 161, 17))
        self.label_22.setObjectName("label_22")
        self.manual_2 = QtWidgets.QFrame(self.tab)
        self.manual_2.setEnabled(False)
        self.manual_2.setGeometry(QtCore.QRect(780, 150, 331, 461))
        self.manual_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.manual_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.manual_2.setObjectName("manual_2")
        self.button_cicle_stop = QtWidgets.QPushButton(self.manual_2)
        self.button_cicle_stop.setEnabled(False)
        self.button_cicle_stop.setGeometry(QtCore.QRect(150, 360, 89, 25))
        self.button_cicle_stop.setObjectName("button_cicle_stop")
        self.label_27 = QtWidgets.QLabel(self.manual_2)
        self.label_27.setGeometry(QtCore.QRect(10, 180, 211, 17))
        self.label_27.setObjectName("label_27")
        self.button_conveyor_stop = QtWidgets.QPushButton(self.manual_2)
        self.button_conveyor_stop.setEnabled(False)
        self.button_conveyor_stop.setGeometry(QtCore.QRect(90, 270, 89, 25))
        self.button_conveyor_stop.setObjectName("button_conveyor_stop")
        self.label_43 = QtWidgets.QLabel(self.manual_2)
        self.label_43.setGeometry(QtCore.QRect(10, 310, 211, 17))
        self.label_43.setObjectName("label_43")
        self.button_feeder_counter = QtWidgets.QPushButton(self.manual_2)
        self.button_feeder_counter.setGeometry(QtCore.QRect(140, 60, 89, 25))
        self.button_feeder_counter.setObjectName("button_feeder_counter")
        self.label_21 = QtWidgets.QLabel(self.manual_2)
        self.label_21.setGeometry(QtCore.QRect(10, 10, 121, 17))
        self.label_21.setObjectName("label_21")
        self.button_feeder_clock = QtWidgets.QPushButton(self.manual_2)
        self.button_feeder_clock.setGeometry(QtCore.QRect(20, 60, 89, 25))
        self.button_feeder_clock.setObjectName("button_feeder_clock")
        self.button_conveyor_clock = QtWidgets.QPushButton(self.manual_2)
        self.button_conveyor_clock.setGeometry(QtCore.QRect(30, 230, 89, 25))
        self.button_conveyor_clock.setObjectName("button_conveyor_clock")
        self.button_cicle_start = QtWidgets.QPushButton(self.manual_2)
        self.button_cicle_start.setGeometry(QtCore.QRect(30, 360, 89, 25))
        self.button_cicle_start.setObjectName("button_cicle_start")
        self.button_conveyor_counter = QtWidgets.QPushButton(self.manual_2)
        self.button_conveyor_counter.setGeometry(QtCore.QRect(150, 230, 89, 25))
        self.button_conveyor_counter.setObjectName("button_conveyor_counter")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(0, 11, 1202, 25))
        self.label_12.setMinimumSize(QtCore.QSize(0, 25))
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(0, 40, 1202, 16))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.line_4 = QtWidgets.QFrame(self.verticalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_4.sizePolicy().hasHeightForWidth())
        self.line_4.setSizePolicy(sizePolicy)
        self.line_4.setMinimumSize(QtCore.QSize(1200, 2))
        self.line_4.setMaximumSize(QtCore.QSize(1200, 2))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_7.addWidget(self.line_4)
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(200, 60, 800, 480))
        self.label_18.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_18.setText("")
        self.label_18.setScaledContents(True)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.button_capture = QtWidgets.QPushButton(self.tab_2)
        self.button_capture.setGeometry(QtCore.QRect(910, 580, 89, 25))
        self.button_capture.setObjectName("button_capture")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        self.label_14.setGeometry(QtCore.QRect(0, 0, 1202, 25))
        self.label_14.setMinimumSize(QtCore.QSize(0, 25))
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(0, 29, 1202, 16))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.line_5 = QtWidgets.QFrame(self.verticalLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_5.sizePolicy().hasHeightForWidth())
        self.line_5.setSizePolicy(sizePolicy)
        self.line_5.setMinimumSize(QtCore.QSize(1200, 2))
        self.line_5.setMaximumSize(QtCore.QSize(1200, 2))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_8.addWidget(self.line_5)
        self.groupBox = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox.setGeometry(QtCore.QRect(20, 50, 371, 71))
        self.groupBox.setObjectName("groupBox")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(10, 30, 121, 23))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setGeometry(QtCore.QRect(150, 30, 111, 23))
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_3.setGeometry(QtCore.QRect(280, 30, 81, 23))
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_2.setGeometry(QtCore.QRect(470, 50, 371, 71))
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton.setGeometry(QtCore.QRect(10, 30, 112, 23))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_2.setGeometry(QtCore.QRect(130, 30, 112, 23))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_3.setGeometry(QtCore.QRect(250, 30, 112, 23))
        self.radioButton_3.setObjectName("radioButton_3")
        self.button_export = QtWidgets.QPushButton(self.tab_3)
        self.button_export.setGeometry(QtCore.QRect(1090, 630, 89, 25))
        self.button_export.setObjectName("button_export")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 140, 1191, 471))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Robot Scara"))
        self.label_3.setText(_translate("MainWindow", "INICIO"))
        self.label_2.setText(_translate("MainWindow", "UNIVERSIDAD DE LAS FUERZAS ARMADAS - ESPE"))
        self.label_5.setText(_translate("MainWindow", "ANDRES PEREZ"))
        self.label_6.setText(_translate("MainWindow", "ANDRES REYES"))
        self.label_4.setText(_translate("MainWindow", "INTEGRANTES:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), _translate("MainWindow", "INICIO"))
        self.label_10.setText(_translate("MainWindow", "PRODUCCI??N"))
        self.ind_table.setText(_translate("MainWindow", "ALIMENTADOR"))
        self.ind_element.setText(_translate("MainWindow", "PIEZA"))
        self.ind_banda.setText(_translate("MainWindow", "BANDA"))
        self.ind_class_1.setText(_translate("MainWindow", "ROJO"))
        self.ind_class_2.setText(_translate("MainWindow", "VERDE"))
        self.label_15.setText(_translate("MainWindow", "SCARA1"))
        self.label_16.setText(_translate("MainWindow", "SCARA2"))
        self.button_start.setText(_translate("MainWindow", "INICIO"))
        self.button_stop.setText(_translate("MainWindow", "FIN DE CICLO"))
        self.button_stop_emer.setText(_translate("MainWindow", "EMERGENCIA"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), _translate("MainWindow", "PRODUCCION"))
        self.groupBox_3.setTitle(_translate("MainWindow", "SELECCIONA ROBOT:"))
        self.scara1_man.setText(_translate("MainWindow", "SCARA 1"))
        self.scara2_man.setText(_translate("MainWindow", "SCARA2"))
        self.label_23.setText(_translate("MainWindow", "MOTOR BASE:"))
        self.button_bm_clock.setText(_translate("MainWindow", "Horario"))
        self.button_bm_counter.setText(_translate("MainWindow", "Antihorario"))
        self.button_bodym_counter.setText(_translate("MainWindow", "Antihorario"))
        self.button_bodym_clock.setText(_translate("MainWindow", "Horario"))
        self.label_24.setText(_translate("MainWindow", "MOTOR CUERPO:"))
        self.button_lm_down.setText(_translate("MainWindow", "BAJAR"))
        self.button_lm_up.setText(_translate("MainWindow", "SUBIR"))
        self.label_25.setText(_translate("MainWindow", "MOTOR LINEAL"))
        self.button_act_stop.setText(_translate("MainWindow", "OFF"))
        self.button_act_start.setText(_translate("MainWindow", "ON"))
        self.label_26.setText(_translate("MainWindow", "ACTUADOR"))
        self.button_home.setText(_translate("MainWindow", "HOME"))
        self.label_11.setText(_translate("MainWindow", "CONTROL MANUAL"))
        self.button_manual.setText(_translate("MainWindow", "PARAR TODO E INICIAR CONTROL MANUAL"))
        self.label_22.setText(_translate("MainWindow", "CONTROL DE SCARAS"))
        self.button_cicle_stop.setText(_translate("MainWindow", "OFF"))
        self.label_27.setText(_translate("MainWindow", "BANDA TRANSPAORTADORA:"))
        self.button_conveyor_stop.setText(_translate("MainWindow", "OFF"))
        self.label_43.setText(_translate("MainWindow", "CICLO DE TRABAJO:"))
        self.button_feeder_counter.setText(_translate("MainWindow", "Antihorario"))
        self.label_21.setText(_translate("MainWindow", "ALIMENTADOR:"))
        self.button_feeder_clock.setText(_translate("MainWindow", "Horario"))
        self.button_conveyor_clock.setText(_translate("MainWindow", "Horario"))
        self.button_cicle_start.setText(_translate("MainWindow", "ON"))
        self.button_conveyor_counter.setText(_translate("MainWindow", "Antihorario"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "CONTROL MANUAL"))
        self.label_12.setText(_translate("MainWindow", "VISI??N ARTIFICIAL"))
        self.button_capture.setText(_translate("MainWindow", "CAPTURAR"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "VISION ARTIFICIAL"))
        self.label_14.setText(_translate("MainWindow", "HISTOGRAMAS"))
        self.groupBox.setTitle(_translate("MainWindow", "Graficas:"))
        self.checkBox.setText(_translate("MainWindow", "Piezas Verdes"))
        self.checkBox_2.setText(_translate("MainWindow", "Piezas Rojas"))
        self.checkBox_3.setText(_translate("MainWindow", "Totales"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Escala de tiempo:"))
        self.radioButton.setText(_translate("MainWindow", "Minutos"))
        self.radioButton_2.setText(_translate("MainWindow", "Horas"))
        self.radioButton_3.setText(_translate("MainWindow", "D??as"))
        self.button_export.setText(_translate("MainWindow", "Exportar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "HISTOGRAMAS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
