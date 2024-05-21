import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class ControllerSubscriber(Node):
  def __init__(self):
    super().__init__('controller_subscriber')
    self.subscription = self.create_subscription(String, 'serial_topic', self.listener_callback, 10)
    self.subscription  # prevent unused variable warning

  def listener_callback(self, msg):
    self.get_logger().info('I heard: "%s"' % msg.data)

def main(args=None):
  try:
    rclpy.init(args=args)
    controller_subscriber = ControllerSubscriber()
    rclpy.spin(controller_subscriber)
  except KeyboardInterrupt:
    pass
  finally:
    controller_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
  main()