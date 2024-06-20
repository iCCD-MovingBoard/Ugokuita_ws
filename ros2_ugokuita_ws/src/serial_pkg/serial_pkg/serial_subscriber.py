import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from .lib import uart

class SerialSubscriber(Node):
  def __init__(self):
    super().__init__('serial_subscriber')
    self.subscription = self.create_subscription(String, 'serial_send_topic', self.listener_callback, 10)
    self.subscription  # prevent unused variable warning
    # self.publisher = self.create_publisher(String, 'serial_receive_topic', 10)

  def listener_callback(self, msg):
    # self.get_logger().info('I heard: "%s"' % msg)
    commands = msg.data.split(',')
    for command in commands:
      self.getlogger().info('Sending command: "%s"' % command)
      uart.send_command(command)

def main(args=None):
  try:
    rclpy.init(args=args)
    serial_subscriber = SerialSubscriber()
    rclpy.spin(serial_subscriber)
  except KeyboardInterrupt:
    pass
  finally:
    uart.send_command(f'R0')
    uart.send_command(f'L0')
    uart.send_command(f'H0')
    uart.send_command(f'B0')
    
    serial_subscriber.destroy_node()
    uart.uart_port.close()
    rclpy.shutdown()

if __name__ == '__main__':
  main()