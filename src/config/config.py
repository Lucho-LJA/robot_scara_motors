#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
import cv2
import numpy as np

"""
GENERAL CONFIG OF PROJECT ABOUT A Scara Robots Cell
    - In this Script you must config de default varibles
    - Only configure the first section ("User config")
    - The second config is about default variables, so configure them,
        ONLY if you are change the code.
    - Write the correct option according your need.
    
"""


#######################USER CONFIG#######################

# Input name of robots
NAME_ROBOT = "scara1"
NAME_ROBOT2 = "scara2"
NAME_CONVEYOR = "banda"
NAME_FEEDER = "alimentador"

# Input number of motors
N_MOTOR = 3
#Input if the robot has a current control
AMPER_CONTROL = True
#Input the type of control
TYPE_CONTROL = "ON-OFF"
#Input the type of identification
CAM_INPUT = 0




#######################DEFAULT CONFIG#######################
"""
Default Config - If you aren't a deveploment, don't modify it
    dir_work: path of main.py file
    dir_work_aux: auxiliar path of main.py file
    N_MOTOR : Number of motors that the robot has
"""
DIR_WORK=''
DIR_WORK_AUX=''

CAM_AREA_MIN=200
CAM_AREA_MAX=1000

#Mask to color identify
RED_LOW1 = np.array([0, 0, 0], np.uint8)
RED_HIGH1 = np.array([12, 255, 255], np.uint8)
RED_LOW2 = np.array([155, 0, 0], np.uint8)
RED_HIGH2 = np.array([180, 255, 255], np.uint8)

GREEN_LOW = np.array([30, 0, 0], np.uint8)
GREEN_HIGH = np.array([80, 255, 255], np.uint8)

#############ENVIROMENT VARIABLES#############
#formato para escribir letras
CV2_FONT = cv2.FONT_HERSHEY_SIMPLEX
#############EGDE DETECTION VARIABLES#############
UMBRAL_MIN = 50
UMBRAL_MAX = 150

#Variable position
pos_red=[0,0]
pos_green=[0,0]

#Image Detection
##Recorte de video
#limite izquierda video
CAM_LIM_LEFTH=25
#limite derecha video
CAM_LIM_RIGHT=600
#limite superior video
CAM_LIM_TOP=200
#limite inferior video
CAM_LIM_BOTTOM=480-65

#Variables de camara
PT_MAX_X=244
PT_MAX_Y=244
#0.45
#mtx=np.float64([[560.60367017,0,329.90361105],[0,560.1149988,235.11508813],[0,0,1]])
#dist=np.array([[0.18452098, -1.21435869, -0.00522202, 0.00729794, 3.39767196]])
#0.32
mtx=np.float64([[560.95148671,0,331.50395719],[0,559.84861743,235.67879925],[0,0,1]])
dist=np.array([[0.17808722, -1.14977257, -0.00590674, 0.00851292, 3.07708921]])

patron = np.float32([[128,179,0], [128,-179,0], [282,179,0], [291,-179,0]])
centros_ordenados = np.float32([[117,206] , [533,204], [119,374], [540,394]])
retval, rvec, tvec = cv2.solvePnP(objectPoints = patron, imagePoints = centros_ordenados, cameraMatrix = mtx, distCoeffs = dist)


###ROS VARIABLE###
Q1_REAL=0
Q2_REAL=180
Q2_REAL=120

##ROBOT VARIABLE
Q1_HOME=90
Q2_HOME=0
Q3_HOME=0

##Fisic variables
L_A=103
L_B=131
L_C=142
L_D=17
R_A=16
Q_MAX=120

X_HOME=0
Y_HOME=L_A+L_B
Z_HOME=0

##VISON VARIABLES
nTest=100
ptObj=[0,0]
angObj=[0,0,0]
angServo=[0,0,0]
Z_AUX_AP=25

########################


