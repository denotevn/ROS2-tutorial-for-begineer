#!/usr/bin/env python3
# activity 4
import rclpy
from rclpy.node import Node
from functools import partial
from my_robot_interfaces.srv import SetLed

class BatteryNode(Node):
    def __init__(self):
        super().__init__("battery") # modify name
        self.battery_state_ = "full"
        self.last_time_battery_state_changed_ = self.get_current_time_second()
        self.battery_timer_ = self.create_timer(0.1, self.check_battery_state)
        self.get_logger().info("Battery node has been started")
    
    def get_current_time_second(self):
        secs, nsecs = self.get_clock().now().seconds_nanoseconds()
        return secs + nsecs / 100000000.0

    def check_battery_state(self):
        time_now = self.get_current_time_second()
        if self.battery_state_ == "full":
            if time_now - self.last_time_battery_state_changed_ > 4.0:
                self.battery_state_ = "empty"
                self.get_logger().info("Battery is empty ! charging battery ...") 
                self.last_time_battery_state_changed_ = time_now
                # call set_led if battery is full
                self.call_set_led_server(3,1) # 3 la led_number, 1 la state
        else:
            if time_now - self.last_time_battery_state_changed_ > 6.0:
                self.battery_state_ = "full"
                self.get_logger().info("Battery is now full again.")
                self.last_time_battery_state_changed_ = time_now  
                self.call_set_led_server(3,0)

    def call_set_led_server(self, led_number, state):
        client = self.create_client(SetLed, "set_led")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Server Set Led ...")
        request = SetLed.Request()
        request.led_number = led_number
        request.state = state
        # call the service
        future = client.call_async(request=request)
        # Add a callback to be executed when the task is done
        future.add_done_callback(partial(self.callback_call_set_led,led_number=led_number, state = state))
    
    def callback_call_set_led(self, future, led_number, state):
        try:
            response = future.result()
            self.get_logger().info(str(response.success))
        except Exception as e:
            self.get_logger().error("Service call failed %r" % (e,))     


def main(args = None):
    rclpy.init(args=args)
    node = BatteryNode() # modify name
    rclpy.spin(node=node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()