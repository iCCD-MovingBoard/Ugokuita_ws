import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from .lib.controller import Joycon
class ControllerPublisher(Node):
  
  def __init__(self):
    super().__init__('controller_publisher')
    self.publisher_ = self.create_publisher(String, 'motor_topic', 10)
    timer_period = 0.0001  # seconds
    self.timer = self.create_timer(timer_period, self.timer_callback)
    self.i = 0
    self.joycon = Joycon("/dev/input/js0")

  def timer_callback(self):
    msg = String()
    controller_data: str = self.joycon.get()
    msg.data = '%s' % controller_data
    self.publisher_.publish(msg)
    self.get_logger().info('Publishing: "%s"' % msg.data)
    self.i += 1

def main(args=None):
  try:
    rclpy.init(args=args)
    controller_publisher = ControllerPublisher()
    rclpy.spin(controller_publisher)
  except KeyboardInterrupt:
    pass
  finally:
    controller_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
  main()