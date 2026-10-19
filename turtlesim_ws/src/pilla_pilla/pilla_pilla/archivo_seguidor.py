import rclpy
from rclpy.node import Node

from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math

class NodoSeguidor (Node):

    def __init__(self):
        super().__init__('NodoSeguidor')

        # Prámetros - 1. los declaramos
        self.declare_parameter('linear_speed', 1.0)
        self.declare_parameter('angular_speed', 1.0)
        self.declare_parameter('k_linear', 1.0)
        self.declare_parameter('k_angular', 1.0)
        self.declare_parameter('cl_period', 0.05)

        # Parámetros - 2. Pillamos los valores de un archivo de parámetros
        self.linear_speed = self.get_parameter('linear_speed').value
        self.angular_speed = self.get_parameter('angular_speed').value
        self.k_linear = self.get_parameter('k_linear').value
        self.k_angular = self.get_parameter('k_angular').value
        self.cl_period = self.get_parameter('cl_period').value

        # Estados
        self.seguidor_pose = None
        self.controlado_pose = None

        # Suscriptores
        self.create_subscription(Pose,'/turtle2/pose', self.seguidor_callback, 10)
        self.create_subscription(Pose, '/turtle1/pose', self.controlado_callback, 10)

        # Publicadores
        self.seguidor_cmd = self.create_publisher(Twist, '/turtle2/cmd_vel', 10)

        # Timers 
        self.timer = self.create_timer(self.cl_period, self.control_loop)
