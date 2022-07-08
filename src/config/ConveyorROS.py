#!/usr/bin/env python3
"""
	Ros configuration with publish to control a on/off action.
	Need a config/config.py file.
"""
import rospy
from std_msgs.msg import Int8
from config.config import *

class Conveyor:
	def __init__(self, name):
		#Values to publsih
		self.val_Int8 = Int8()
		#Atributes of element
		self.emergency = False
			
		#Init publisher
		self.pub_act = rospy.Publisher(name+'/action', Int8, queue_size=2)

		#Init Sunscriptors
		print("Inicializando Subscriptores...")
		rospy.Subscriber(name+'/get_emergency', Int8, self.recive_emergency)
		
	# Function to suscribe
	def recive_emergency(self,data):
		if data.data == 0:
			self.emergency = False
		else:
			self.emergency = True
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
		
