#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import Int64

class NumberPublisherNode(Node):
    def __init__(self):
        super().__init__("number_publisher") # modify name
        # declare new param
        # need to add type of param (it is very important)
        # self.declare_parameter("test123") # no set value
        # self.declare_parameter("another_param", type=String) 
        # lam viec voi parameter cua minh
        self.declare_parameter("number_to_publish", 2)
        self.declare_parameter("publish_frequency", 1.0)


        self.number_ = self.get_parameter("number_to_publish").value  # 2
        self.publish_frequency_ = self.get_parameter("publish_frequency").value
        self.number_publisher_ = self.create_publisher(Int64, 'number', 10) # number - topic
        self.number_timer_ = self.create_timer(1.0 / self.publish_frequency_, self.publish_number)
        self.get_logger().info("Number publisher has been started.")

    def publish_number(self):
        msg = Int64()
        msg.data = self.number_
        self.number_publisher_.publish(msg) 

def main(args = None):
    rclpy.init(args=args)
    node = NumberPublisherNode() # modify name
    rclpy.spin(node=node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()