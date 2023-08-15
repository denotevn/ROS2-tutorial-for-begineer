#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import HardwareStatus

# You can see this code in file is the same as number_publisher.py

class HardwareStatusPublisherNode(Node):
    def __init__(self):
        super().__init__("hardware_status_publisher") # modify name
        # creaate publisher
        # Here /hardware_status_publisher is publisher and /hardware_status is topic
        # self.create_publisher(String, name of topics)
        self.hw_status_publisher_ = self.create_publisher(HardwareStatus, "hardware_status", 10)
        self.timer_ = self.create_timer(1.0, self.publish_hw_status)
        self.get_logger().info("Hardware status publisher has been started !")

    def publish_hw_status(self):
        msg = HardwareStatus()
        msg.temperature = 45
        msg.are_motors_ready = True
        msg.debug_message = "Nothing special here !"
        self.hw_status_publisher_.publish(msg=msg)


def main(args = None):
    rclpy.init(args=args)
    node = HardwareStatusPublisherNode() # modify name
    rclpy.spin(node=node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()