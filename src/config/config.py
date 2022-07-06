#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
import numpy as np

"""
GENERAL CONFIG OF PROJECT
    - In this Script you must config de default varibles
    - Only configure the first section ("User config")
    - The second config is about default variables, so configure them,
        ONLY if you are change the code.
    - Write the correct option according your need.
    
"""



"""
USER CONFIG
    NAME: Name of robot. It is escencial, if you work with several robots
            -If you will do one hmi to control several robots Add more variables
            or use a base name to config the env.
    TYPE_MOTOR: Especify the configuration of motors robot
        MOTOR2DIS: The scara use 2 motors and 1 lineal motor (3FOD)
                    they are controlled sending a angle or distance
        (For now only there is one)

    TYPE_ACTUATOR: Especify the type of actuator
        NoAct : No use a actuator.
        OnOff:  Use a actutor on/off such as electroiman, gripper or others, which only
                need a action true or false to start/stop. 
    
    AMPER_CONTROL: Especify if the robot has a control of current
        True or False 

    CONTROL: Especify if the type of control
        PID :  Control using PID. Recive and send kp, ki, kd parammetres
        ON-OFF : Control using ON-OFF control.
    
    APPLICATION: Especify the aplication
        CELL: A cell of 2 scaras, 1 transporter band and a feeder in order to clasify objects with AV.
"""
# Input name of robots
NAME_ROBOT = "scara1"
NAME_ROBOT2 = "scara2"
NAME_CONVEYOR = "banda"
NAME_FEEDER = "alimentador"

# Input the type of scara: Servo2only - Servo3_without_act - Servo3_with_act
TYPE_MOTOR = "MOTOR2DIS"
#Input the type of actuator: NoAct - ImanServo - OnOff
TYPE_ACTUATOR = "NoAct"
#Input if the robot has a current control
AMPER_CONTROL = True

#Input the type of control
TYPE_CONTROL = "ON-OFF"

#Imput the type o application
TYPE_APP = "CELL"


"""
Default Config - If you aren't a deveploment, don't modify it
    dir_work: path of main.py file
    dir_work_aux: auxiliar path of main.py file
    N_MOTOR : Number of motors that the robot has
"""
dir_work=''
dir_work_aux=''

if TYPE_MOTOR == "MOTOR2DIS":
    N_MOTOR = 2




