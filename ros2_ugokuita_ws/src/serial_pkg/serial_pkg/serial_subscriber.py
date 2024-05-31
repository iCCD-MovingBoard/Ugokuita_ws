import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from .lib import uart
from custom_msg.msg import SendCommand, RecieveCommand

class SerialSubscriber(Node):
  def __init__(self):
    super().__init__('serial_subscriber')
    self.subscription = self.create_subscription(SendCommand, 'serial_send_topic', self.listener_callback, 10)
    self.subscription  # prevent unused variable warning
    self.publisher = self.create_publisher(RecieveCommand, 'serial_receive_topic', 10)

  def listener_callback(self, msg):
    self.get_logger().info('I heard: "%s"' % msg)
    
    if msg.r: uart.send_to_motordriver(f'R{msg.r}')
    if msg.l: uart.send_to_motordriver(f'L{msg.l}')
    if msg.h: uart.send_to_motordriver(f'H{msg.h}')
    if msg.b: uart.send_to_motordriver(f'B{msg.b}')

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