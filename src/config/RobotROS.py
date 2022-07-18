#!/usr/bin/env python3
"""
	Ros configuration with publish and subscriptor
	Create a class of the robot and init the variables following the type robot 
	and type actuator
"""
import rospy
from std_msgs.msg import Int32MultiArray
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Int8
from config.config import *

class Robot:
	def __init__(self, name, n_motor):
		#Values to publsih
		self.val_arrayInt32=Int32MultiArray()
		self.val_arrayFloat32=Float32MultiArray()
		self.val_Int8 = Int8()
		self.rate = 0
		#Init variable of Position, current and control of motors
		self.position =[]
		self.sensor = []
		#Only PID Control
		self.kp = []
		self.ki = []
		self.kd = []
		for i in range(n_motor):
			self.position.append(0)
			self.sensor.append(0)
			if TYPE_CONTROL == "PID":
				self.kp.append(0)
				self.ki.append(0)
				self.kd.append(0)
		

			
		#Init publisher
		self.pub_pos = rospy.Publisher(name+'/set_position', Float32MultiArray, queue_size=2)
		self.pub_act = rospy.Publisher(name+'/set_actuator', Int8, queue_size=2)
		self.pub_stop = rospy.Publisher(name+'/stop', Int8, queue_size=2)
		if TYPE_CONTROL == "PID":
			self.pub_kp = rospy.Publisher(name+'/set_kp', Int8, queue_size=2)
			self.pub_ki = rospy.Publisher(name+'/set_ki', Int8, queue_size=2)
			self.pub_kd = rospy.Publisher(name+'/set_kd', Int8, queue_size=2)

		print("Inicializando Subscriptores...")
		rospy.Subscriber(name+'/get_position', Float32MultiArray, self.recive_position)
		if AMPER_CONTROL:
			rospy.Subscriber(name+'/get_sensor', Float32MultiArray, self.recive_sensor)
		if TYPE_CONTROL == "PID":
			rospy.Subscriber(name+'/get_kp', Float32MultiArray, self.recive_kp)
			rospy.Subscriber(name+'/get_ki', Float32MultiArray, self.recive_ki)
			rospy.Subscriber(name+'/get_kd', Float32MultiArray, self.recive_kd)
		
		
	# Function to suscribe
	def recive_position(self,data):
		self.positon = self.changeScalePos(data.data)
	
	def recive_sensor(self,data):
		self.sensor = data.data
	
	#Only PID CONTROL
	def recive_kp(self,data):
		self.kp = data.data
	def recive_kd(self,data):
		self.kd = data.data
	def recive_ki(self,data):
		self.ki = data.data


	# Function to publish
	#Emergency stop
	def stopAll(self,data):
		if data:
			self.val_Int8.data = 1
		else:
			self.val_Int8.data = 0
		self.pub_stop.publish(self.val_Int8)
		self.rate.sleep()
	#Position
	def moveTo(self,data):
		self.val_arrayFloat32.data = data
		self.pub_pos.publish(self.val_arrayFloat32)
		self.rate.sleep()

	#Actuator
	def actuator(self,option):
		if option:
			self.val_Int8.data = 1
		else:
			self.val_Int8.data = 0
		self.pub_act.publish(self.val_Int8)
		self.rate.sleep()
	#Control PID
	def set_pid(self,data):
		if TYPE_CONTROL == "PID":
			self.val_arrayFloat32.data = data[0]
			self.pub_kp.publish(self.val_arrayFloat32)
			self.rate.sleep()
			self.val_arrayFloat32.data = data[1]
			self.pub_ki.publish(self.val_arrayFloat32)
			self.rate.sleep()
			self.val_arrayFloat32.data = data[2]
			self.pub_kd.publish(self.val_arrayFloat32)
			self.rate.sleep()
		else:
			pass
	
	def changeScalePos(self,pos):
		data1=(245-76.93*pos[0])*2
		data2=(245-76.93*pos[1])*2
		data3=(245-76.93*pos[2])*2
		return [data1,data2,data3]
	
	def pubHome(self,posHome):
		self.val_arrayFloat32.data = posHome
		self.val_Int8.data = 0
		self.pub_act.publish(self.val_Int8)
		self.pub_pos.publish(self.val_arrayFloat32)
		self.rate.sleep()
	
	

		
