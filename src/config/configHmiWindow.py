#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
from config.config import *
from lib.hmi import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from config.initROS import *
import cv2
import numpy as np
import math
import time

###################################################################################
###################################################################################
########################VENTANA DE CONTROL#########################################
###################################################################################
class Ui_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        self.captura= cv2.VideoCapture(CAM_INPUT)
        self.captura.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
        self.captura.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self) 
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.capture_cam)
        self.timer.start()

    def capture_cam(self):
        pass