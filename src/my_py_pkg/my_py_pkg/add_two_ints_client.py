#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from functools import partial
# functools.partial: 
# Cho phép tạo một phiên bản mới của một hàm với một số đối số mặc định đã được cung cấp.

from example_interfaces.srv import AddTwoInts

class AddTwoIntsClientNode(Node):
    def __init__(self):
        super().__init__("add_two_ints_client") # modify name
        self.call_add_two_ints_server(6,3)
        self.call_add_two_ints_server(5,5)
        self.call_add_two_ints_server(10,10)

    def call_add_two_ints_server(self, a, b):
        client = self.create_client(AddTwoInts, "add_two_ints")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Server Add Two Ints")
        request = AddTwoInts.Request()
        request.a = a
        request.b = b
        future = client.call_async(request=request)
        # Add a callback to be executed when the task is done
        future.add_done_callback(partial(self.callback_call_add_two_ints,a=a, b=b))
    
    def callback_call_add_two_ints(self, future, a, b):
        try:
            response = future.result()
            self.get_logger().info(str(a) + " + " + 
                                str(b) + " = " + str(response.sum))
        except Exception as e:
            self.get_logger().error("Service call failed !")


def main(args = None):
    rclpy.init(args=args)
    node = AddTwoIntsClientNode() # modify name
    rclpy.spin(node=node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()