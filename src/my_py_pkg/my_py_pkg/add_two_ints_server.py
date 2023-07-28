'''
This file: Basic service in ROS2 that return the num of two numbers
'''
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class AddTwoIntsServerNode(Node):
    def __init__(self):
        super().__init__("add_twos_ints_server") # modify name
        self.server_ = self.create_service(
            AddTwoInts, "add_two_ints", self.callback_add_two_ints)
        self.get_logger().info("Add two ints has been started!")

    def callback_add_two_ints(self, request, respone):
        respone.sum = request.a + request.b
        self.get_logger().info(str(request.a) + " + " + str(request.b) + " = " + str(respone.sum))
        return respone
    
def main(args = None):
    rclpy.init(args=args)
    node = AddTwoIntsServerNode() # modify name
    rclpy.spin(node=node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
