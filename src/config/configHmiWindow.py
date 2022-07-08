#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
from config.config import *
from lib.hmi import *
from lib.visionFunctions import *
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
        self.captura= cv2.VideoCapture(CAM_INPUT,cv2.CAP_V4L2)
        self.captura.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
        self.captura.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        #General Variables
        self.operation = 0
        self.in_action = False
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self) 
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.capture_cam)
        self.timer.start()

        #Events of pushbuttons
        self.button_start.clicked.connect(self.start_production)
        self.button_stop.clicked.connect(self.stop_production)
    
    def start_production(self):
        self.operation = 1
        print("ok")
        self.button_start.setEnabled(False)
        self.button_stop.setEnabled(True)
        #Set to home all

    def stop_production(self):
        self.operation = 0
        self.button_start.setEnabled(True)
        self.button_stop.setEnabled(False)
        #Set to home all

    def capture_cam(self):
        self.mostrar_cam()

    def mostrar_cam(self):
        pos1x=0
        pos1y=0
        pos2x=0
        pos2y=0  
        # Capture with cam.
        (ok, img) = self.captura.read()
        if not ok:
            return
        imag_rect=img.copy()
        #imag_rect=cv2.rectangle(imag_rect.copy(), (0,0), (25,480), (255,255,255),-1)
        imag_rect,red_coord,green_coord=detecPos(imag_rect.copy(),img.copy())
        if red_coord[0]==0 and red_coord[1]==0:
            #print("Red object no found")
            pos_red=[0,0]
            detec_red = False
        else:
            #print ("red:"+str(red_coord))
            pos_red=red_coord
            detec_red = True
        if green_coord[0]==0 and green_coord[1]==0:
            #print("Green object no found")
            pos_green=[0,0]
            detec_green = False
        else:
            #print ("Green:"+str(green_coord))
            pos_green=green_coord
            detec_green = True
        
        if (detec_green == True and detec_red == False) or (detec_green == False and detec_red == True):
            if self.operation == 1 and not self.in_action:
                self.in_action = True

        if self.tabWidget.currentIndex() == 2 or self.tabWidget.currentIndex() == 3:
            image = QtGui.QImage(imag_rect, imag_rect.shape[1], imag_rect.shape[0], imag_rect.shape[1] * imag_rect.shape[2], QtGui.QImage.Format_RGB888)
            pixmap = QtGui.QPixmap()
            pixmap.convertFromImage(image.rgbSwapped())
            # Mostramos el QPixmap en la QLabel.
            if self.tabWidget.currentIndex() == 2:
                self.label.setPixmap(pixmap)
            else:
                self.label_18.setPixmap(pixmap)