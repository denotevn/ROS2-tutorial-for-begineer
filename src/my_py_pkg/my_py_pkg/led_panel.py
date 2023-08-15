#!/usr/bin/env python3
import rclpy
# activity 4
from rclpy.node import Node
from my_robot_interfaces.msg import LedStateArray
from my_robot_interfaces.srv import SetLed

'''
Battery is empty - led panel have led_state[3] = 1
Battery is full - led panel have led_state = [0, 0, 0]
'''
class LedPanelNode(Node):
    def __init__(self):
        super().__init__("led_panel") # modify name
        self.led_states_ = [0, 0, 0]
        self.led_states_publisher_ = self.create_publisher(LedStateArray, "led_state", 10)
        self.led_states_timer_ = self.create_timer(3, self.publish_led_states)
        self.set_led_service_ = self.create_service(
            SetLed, "set_led", self.callback_set_led)

        self.get_logger().info("LED panel node has been started.")

    def publish_led_states(self):
        msg = LedStateArray()
        msg.led_state = self.led_states_
        self.led_states_publisher_.publish(msg=msg)
    
    def callback_set_led(self, request, response):
        led_number = request.led_number
        state = request.state

        if led_number > len(self.led_states_) or led_number <= 0:
            response.success = False
            return response
        if state not in [0,1]:
            response.success = False
            return response 
        # update data in led state
        self.led_states_[led_number - 1] = state
        response.success = True
        # cap nhat state moi cho led
        self.publish_led_states()
        return response

def main(args = None):
    rclpy.init(args=args)
    node = LedPanelNode() # modify name
    rclpy.spin(node=node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()