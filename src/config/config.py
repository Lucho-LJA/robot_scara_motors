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
    TYPE_SERVO: Especify the type of robot 
        Servo2: The scara only use 2 servos (2FOD)
        (For now only there is one)
        Servo3: The scara use 3 servos (3FOD)

    TYPE_ACTUATOR: Especify the type of actuator
        NoAct : No use a actuator.
        ImanServo : Use a iman to catch metalic pieces and the last servo to remove
                    the piece. Is necesary a specyfic mecanic design
        OnOff:  Use a actutor on/off such as electroiman, gripper or others, which only
                need a action true or false to start/stop. 
"""
# Input name of robot
NAME_ROBOT = "scara1"
# Input the type of scara: Servo2only - Servo3_without_act - Servo3_with_act
TYPE_SERVO = "Servo2"
#Input the type of actuator: NoAct - ImanServo - OnOff
TYPE_ACTUATOR = "NoAct"


"""
Default Config - If you aren't a deveploment, don't modify it
    dir_work: path of main.py file
    dir_work_aux: auxiliar path of main.py file
    N_SERVO : Number of servos that the robot has
"""
dir_work=''
dir_work_aux=''
if TYPE_SERVO == "Servo2":
    N_SERVO = 2
elif TYPE_SERVO == 'Servo3':
    N_SERVO = 3


