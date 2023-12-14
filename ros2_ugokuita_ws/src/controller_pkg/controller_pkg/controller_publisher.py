import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class ControllerPublisher(Node):
  def __init__(self):
    super().__init__('controller_publisher')
    self.publisher_ = self.create_publisher(String, 'controller_topic', 10)
    timer_period = 1  # seconds
    self.timer = self.create_timer(timer_period, self.timer_callback)
    self.i = 0

  def timer_callback(self):
    msg = String()
    msg.data = 'Hello World: %d' % self.i
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