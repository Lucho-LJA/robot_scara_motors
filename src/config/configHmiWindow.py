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
        self.button_stop_emer.clicked.connect(self.stop_emergency)


        self.button_manual.clicked.connect(self.change_manual)

        self.button_bm_clock.clicked.connect(self.moveScaraBaseClock)
        self.button_bm_counter.clicked.connect(self.moveScaraBaseCounter)
        self.button_bodym_clock.clicked.connect(self.moveScaraBodyClock)
        self.button_bodym_counter.clicked.connect(self.moveScaraBodyCounter)
        self.button_lm_up.clicked.connect(self.moveScaraLinealUp)
        self.button_lm_down.clicked.connect(self.moveScaraLinealDown)
        self.button_act_start.clicked.connect(self.actuatoScaraOn)
        self.button_act_stop.clicked.connect(self.actuatoScaraOff)
        self.button_home.clicked.connect(self.goHOme)

    def moveScaraBaseClock(self):
        if self.scara1_man.isChecked():
            aux=scara1.position
            if aux[0]+DELTA_ANG > MOTOR1_MAX:
                aux[0]=MOTOR1_MAX
            else:
                aux[0]=aux[0]+DELTA_ANG
            scara1.moveTo(aux)
        else:
            aux=scara2.position
            if aux[0]+DELTA_ANG > MOTOR1_MAX:
                aux[0]=MOTOR1_MAX
            else:
                aux[0]=aux[0]+DELTA_ANG
            scara2.moveTo(aux)
    def moveScaraBaseCounter(self):
        if self.scara1_man.isChecked():
            aux=scara1.position
            if aux[0]-DELTA_ANG < MOTOR1_MIN:
                aux[0]=MOTOR1_MIN
            else:
                aux[0]=aux[0]-DELTA_ANG
            scara1.moveTo(aux)
        else:
            aux=scara2.position
            if aux[0]-DELTA_ANG > MOTOR1_MIN:
                aux[0]=MOTOR1_MIN
            else:
                aux[0]=aux[0]-DELTA_ANG
            scara2.moveTo(aux)
    def moveScaraBodyClock(self):
        if self.scara1_man.isChecked():
            aux=scara1.position
            if aux[1]+DELTA_ANG > MOTOR2_MAX:
                aux[1]=MOTOR2_MAX
            else:
                aux[1]=aux[1]+DELTA_ANG
            scara1.moveTo(aux)
        else:
            aux=scara2.position
            if aux[1]+DELTA_ANG > MOTOR2_MAX:
                aux[1]=MOTOR2_MAX
            else:
                aux[1]=aux[1]+DELTA_ANG
            scara2.moveTo(aux)
    def moveScaraBodyCounter(self):
        if self.scara1_man.isChecked():
            aux=scara1.position
            if aux[1]-DELTA_ANG < MOTOR2_MIN:
                aux[1]=MOTOR2_MIN
            else:
                aux[1]=aux[1]-DELTA_ANG
            scara1.moveTo(aux)
        else:
            aux=scara2.position
            if aux[1]-DELTA_ANG > MOTOR2_MIN:
                aux[1]=MOTOR2_MIN
            else:
                aux[1]=aux[1]-DELTA_ANG
            scara2.moveTo(aux)
    def moveScaraLinealUp(self):
        if self.scara1_man.isChecked():
            aux=scara1.position
            if aux[2]+DELTA_LONG > MOTOR3_MAX:
                aux[2]=MOTOR3_MAX
            else:
                aux[2]=aux[2]+DELTA_LONG
            scara1.moveTo(aux)
        else:
            aux=scara2.position
            if aux[2]+DELTA_LONG > MOTOR3_MAX:
                aux[2]=MOTOR3_MAX
            else:
                aux[2]=aux[2]+DELTA_LONG
            scara2.moveTo(aux)
    def moveScaraLinealDown(self):
        if self.scara1_man.isChecked():
            aux=scara1.position
            if aux[2]-DELTA_LONG < MOTOR3_MIN:
                aux[2]=MOTOR3_MIN
            else:
                aux[2]=aux[2]-DELTA_LONG
            scara1.moveTo(aux)
        else:
            aux=scara2.position
            if aux[2]-DELTA_LONG < MOTOR3_MIN:
                aux[2]=MOTOR3_MIN
            else:
                aux[2]=aux[2]-DELTA_LONG
            scara2.moveTo(aux)
    def actuatoScaraOn(self):
        if self.scara1_man.isChecked():
            scara1.actuator(True)
        else:
            scara2.actuator(True)
        self.button_act_start.setEnabled(False)
        self.button_act_stop.setEnabled(True)
    def actuatoScaraOff(self):
        if self.scara1_man.isChecked():
            scara1.actuator(False)
        else:
            scara2.actuator(False)
        self.button_act_start.setEnabled(True)
        self.button_act_stop.setEnabled(False)

    def goHome(self):
        if self.scara1_man.isChecked():
            scara1.pubHome(SCARA1_HOME)
        else:
            scara2.pubHome(SCARA2_HOME)

    def change_manual(self):
        if self.button_manual.text() == "PARAR TODO E INICIAR CONTROL MANUAL":
            self.button_manual.setText("APAGAR MODO MANUAL")
            self.stop_production()
            self.button_start.setEnabled(False)
            self.manual_1.setEnabled(True)
            self.manual_2.setEnabled(True)
            self.in_action = False
            self.operation = 2
        else:
            self.button_manual.setText("PARAR TODO E INICIAR CONTROL MANUAL")
            self.button_start.setEnabled(True)
            self.manual_1.setEnabled(False)
            self.manual_2.setEnabled(False)
            self.in_action = False
            self.operation = 0



    def stop_emergency(self):
        self.operation = 0
        self.button_start.setEnabled(True)
        self.button_stop.setEnabled(False)
        #Set config emergency
    def start_production(self):
        self.operation = 1
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
            if self.tabWidget.currentIndex() == 3:
                self.label_18.setPixmap(pixmap)
            else:
                if self.scara2_man.isChecked() and self.operation == 2:
                    self.label.setPixmap(pixmap)
                else:
                    self.label.clear()