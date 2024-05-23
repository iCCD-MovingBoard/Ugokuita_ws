import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from .lib import str_converter
from .lib import uart
from ...common.type_difinition import SendCommand, RecieveCommand

class SerialSubscriber(Node):
  def __init__(self):
    super().__init__('serial_subscriber')
    self.subscription = self.create_subscription(SendCommand, 'serial_send_topic', self.listener_callback, 10)
    self.subscription  # prevent unused variable warning
    self.publisher = self.create_publisher(RecieveCommand, 'serial_recieve_topic', 10)

  def listener_callback(self, msg):
    self.get_logger().info('I heard: "%s"' % msg.data)
    
    right = msg.r
    if right: uart.send_to_motordriver(f'R{right}')
    left = msg.l
    if left: uart.send_to_motordriver(f'L{left}')
    h = msg.h
    if h: uart.send_to_motordriver(f'H{h}')
    b = msg.b
    if b: uart.send_to_motordriver(f'B{b}')

def main(args=None):
  try:
    rclpy.init(args=args)
    serial_subscriber = SerialSubscriber()
    rclpy.spin(serial_subscriber)
  except KeyboardInterrupt:
    pass
  finally:
    uart.send_to_motordriver(0, 0, 0, 0)
    serial_subscriber.destroy_node()
    uart.uart_port.close()
    rclpy.shutdown()

if __name__ == '__main__':
  main()