import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from .lib import str_converter
from .lib import uart

class MotorSubscriber(Node):
  def __init__(self):
    super().__init__('motor_subscriber')
    self.subscription = self.create_subscription(String, 'motor_topic', self.listener_callback, 10)
    self.subscription  # prevent unused variable warning
    self.canMove = True

  def listener_callback(self, msg):
    self.get_logger().info('I heard: "%s"' % msg.data)
    if msg.data == '#stop':
      self.get_logger().warn('STOP')
      uart.send_to_motordriver(0, 0, -1, 300)
      self.canMove = False
      return
    if msg.data == '#start':
      self.get_logger().warn('START')
      self.canMove = True
      return
    controller_inputs: dict = str_converter.to_dict(msg.data)
    axis_x = int(controller_inputs['L_Axis_x'])
    axis_y = int(controller_inputs['L_Axis_y'])
    right = -axis_x - axis_y
    left  =  axis_x - axis_y
    if self.canMove == False:
      if right > 0: right = 0
      if left > 0: left = 0
    uart.send_to_motordriver( right,
                              left,
                              controller_inputs['X'], -1)

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