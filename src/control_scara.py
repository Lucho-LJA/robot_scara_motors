#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
from config.config import *
from config import RobotROS as Rros
from PyQt5 import QtCore, QtGui, QtWidgets
from lib.hmi import *

r_scara = Rros.Robot_Scara(NAME_ROBOT ,N_SERVO,TYPE_ACTUATOR)


if __name__ == "__main__":
	#globales.dir_work=os.path.dirname(os.path.abspath(__file__))
	#globales.dir_work_aux=os.path.dirname(os.path.abspath(__file__))
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())