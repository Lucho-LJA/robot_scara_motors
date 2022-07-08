#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
from config.config import *
from PyQt5 import QtCore, QtGui, QtWidgets
#from lib.hmi import *
from config.initROS import *
from config.configHmiWindow import *

if __name__ == "__main__":
	#globales.dir_work=os.path.dirname(os.path.abspath(__file__))
	#globales.dir_work_aux=os.path.dirname(os.path.abspath(__file__))
    import sys
    app = QtWidgets.QApplication([])
    ui = Ui_MainWindow()
    ui.show()
    app.exec_()