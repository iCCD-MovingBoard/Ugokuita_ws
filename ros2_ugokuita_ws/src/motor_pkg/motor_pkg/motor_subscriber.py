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

  def listener_callback(self, msg):
    self.get_logger().info('I heard: "%s"' % msg.data)
    controller_inputs: dict = str_converter.to_dict(msg.data)
    axis_x = int(controller_inputs['L_Axis_x'])
    axis_y = int(controller_inputs['L_Axis_y'])
    right = -axis_x - axis_y
    left  =  axis_x - axis_y
    uart.send_to_motordriver( right,
                              left,
                              controller_inputs['X'])

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