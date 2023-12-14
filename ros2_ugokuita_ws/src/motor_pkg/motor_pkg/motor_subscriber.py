import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from .lib.str_converter import str_converter
from .lib.uart import uart

class MotorSubscriber(Node):
  def __init__(self):
    super().__init__('motor_subscriber')
    self.subscription = self.create_subscription(String, 'motor_topic', self.listener_callback, 10)
    self.subscription  # prevent unused variable warning

  def listener_callback(self, msg):
    self.get_logger().info('I heard: "%s"' % msg.data)
    speeds: list[int] = str_converter.to_speeds(msg.data)
    uart.send_to_motordriver(uart.uart_port, speeds['right'], speeds['left'])

def main(args=None):
  try:
    rclpy.init(args=args)
    controller_subscriber = MotorSubscriber()
    rclpy.spin(controller_subscriber)
  except KeyboardInterrupt:
    pass
  finally:
    controller_subscriber.destroy_node()
    uart.uart_port.close()
    rclpy.shutdown()

if __name__ == '__main__':
  main()