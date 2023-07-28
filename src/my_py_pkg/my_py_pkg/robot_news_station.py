#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import String

class RobotNewsStationNode(Node):
    def __init__(self):
        super().__init__("robot_news_station") # modify name the same name with file name

        self.robot_name_ = "KGB_003"
        # 10 looke like a buffer. Keep some msg before they are processed
        # self.create_publisher(String, name of topics)
        self.publisher_ = self.create_publisher(String, "robot_news",10) 
        # create a timer
        self.timer_ = self.create_timer(0.5, self.publish_news)
        self.get_logger().info("Robot news station has been started")

    
    def publish_news(self):
        msg = String()
        msg.data = "Hi, This is " + str(self.robot_name_) + " from the robot news station"
        self.publisher_.publish(msg)

def main(args = None):
    rclpy.init(args=args)
    node = RobotNewsStationNode() # modify name
    rclpy.spin(node=node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()