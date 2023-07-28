#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import Int64

class NumberCounterNode(Node):
    def __init__(self):
        super().__init__("number_counter") # modify name
        
        self.counter_ = 0
        # # create publisher to topics "numbber_count" when recieve message from topic "number"
        self.number_count_publisher_ = self.create_publisher(
                                Int64, 'number_count', 10)
        # Create subscriber to topic number for recieving data
        self.number_subscriber_ = self.create_subscription(Int64, 'number', 
                                self.callback_number_count, 10)
        self.get_logger().info("Number Coounter Node has been started!")

    def callback_number_count(self, msg):
        self.counter_ += msg.data
        new_msg = Int64()
        new_msg.data = self.counter_
        self.number_count_publisher_.publish(new_msg)

def main(args = None):
    rclpy.init(args=args)
    node = NumberCounterNode() # modify name
    rclpy.spin(node=node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()