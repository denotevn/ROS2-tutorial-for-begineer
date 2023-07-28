#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__("py_test")
        self.counter_ = 0
        self.get_logger().info("Tuan Dinh Helo ROS2")
        self.create_timer(0.5, self.timer_callback)
    
    def timer_callback(self):
        self.counter_ += 1
        self.get_logger().info("Hello em nha que "+str(self.counter_))

def main(args = None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node=node)
    rclpy.shutdown()

# def main(args = None):
#     rclpy.init(args=args)
#     node = Node("py_test")
#     node.get_logger().info("Hello ROS2")
#     rclpy.spin(node) # dung thong xuyen torng tat ca cac chuong trinh
#     rclpy.shutdown()

if __name__ == "__main__":
    main()