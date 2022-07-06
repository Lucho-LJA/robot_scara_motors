"""
Script to init ROS with all topict to recive into the aplication
"""
import rospy
from config.config import *
from config import RobotROS as Rros
from config import ConveyorROS as Cros
from config import FeederROS as Fros
scara1 = Rros.Robot(NAME_ROBOT ,N_MOTOR)
scara2 = Rros.Robot(NAME_ROBOT2 ,N_MOTOR)
conveyor = Cros.Conveyor(NAME_CONVEYOR)
feeder = Fros.Feeder(NAME_FEEDER )
print("Inicializando nodo...")
rospy.init_node("CELL_ROBOT", anonymous=True)
rospy.loginfo('Control Robot SCARA: '+ "CELL_ROBOT")
print("Nodo Inicializado")
scara1.rate = rospy.Rate(10) # 10hz
scara2.rate = rospy.Rate(10) # 10hz
conveyor.rate = rospy.Rate(10) # 10hz
feeder.rate = rospy.Rate(10) # 10hz