#!/usr/bin/env python3
"""
	Ros configuration with publish and subscriptor
	Create a class of the robot and init the variables following the type robot 
	and type actuator
"""
import rospy
from std_msgs.msg import Int32MultiArray
from std_msgs.msg import Int8
from config.config import *

class Robot_Scara:
	def __init__(self, name, n_servo, type_actuator):
		if type_actuator == "OnOff":
			self.actuator=Int8()
			self.actuator.data=0
		else:
			self.actuator=Int8()
			self.actuator.data=0
		
		self.ang=Int32MultiArray()
		if n_servo == 2:
			self.ang.data=[0,0]
		elif n_servo == 3:
			self.ang.data=[0,0,0]

		self.pub_ang = rospy.Publisher(name+'/angs', Int32MultiArray, queue_size=2)
		self.pub_act = rospy.Publisher(name+'/actuator', Int8, queue_size=2)
		print("Inicializando Nodo...")
		rospy.Subscriber(name+'/ang_state', Int32MultiArray, self.update_state)
		rospy.init_node(name, anonymous=True)
		rospy.loginfo('Control Robot SCARA: '+name)
		print("Nodo Inicializado")
		self.rate = rospy.Rate(10) # 10hz
		

	def update_state(self,data):
		self.ang_servo = data.data
	
	def pubHome(self):
		self.actuator.data=2
		self.pub_act.publish(self.actuator)
		self.rate.sleep()

	def moveRobot(self,ang3):
		self.ang.data=ang3
		self.pub_ang.publish(self.ang)
		self.rate.sleep()
