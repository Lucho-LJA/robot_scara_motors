#!/usr/bin/env python3
"""
	Ros configuration with publish and subscriptor
	in order to control a feeder that rotate in intervals
	Have 2 sensors on/off to control the parts stocks
"""
from sympy import false, true
import rospy
from std_msgs.msg import Int8
from config.config import *

class Feeder:
	def __init__(self, name):
		#Values to publsih
		self.val_Int8 = Int8()
		self.sensor1 = False
		self.sensor2 = False
		#Init publisher
		self.pub_act = rospy.Publisher(name+'/action', Int8, queue_size=2)

		print("Inicializando Subscriptores...")
		rospy.Subscriber(name+'/get_sensor1', Int8, self.recive_sensor1)
		rospy.Subscriber(name+'/get_sensor2', Int8, self.recive_sensor2)
		
	# Function to suscribe
	def recive_sensor1(self,data):
		if data.data == 0:
			self.sensor1 = False
		else:
			self.sensor1 = True
	def recive_sensor2(self,data):
		if data.data == 0:
			self.sensor2 = False
		else:
			self.sensor2 = True
	

	# Function to publish
	#Action
	def action(self,option):
		if option=='clock':
			self.val_Int8.data = 1
		elif option=='counter':
			self.val_Int8.data = 2
		else:
			self.val_Int8.data = 0
		self.pub_act.publish(self.val_Int8)
		self.rate.sleep()
	

		
