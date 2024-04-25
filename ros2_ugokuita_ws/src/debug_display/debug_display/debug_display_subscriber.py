import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from .lib.debug_display import debug

class DebugDisplaySubscriber(Node):
  def __init__(self):
    super().__init__('debug_display_subscriber')
    self.subscription = self.create_subscription(String, 'debug_display_topic', self.listener_callback, 10)
    self.subscription  # prevent unused variable warning
    debug.write('start debug write\n')

  def listener_callback(self, msg):
    debug.write(str(msg.data))

def main(args=None):
  try:
    rclpy.init(args=args)
    debug_display_subscriber = DebugDisplaySubscriber()
    rclpy.spin(debug_display_subscriber)
  except KeyboardInterrupt:
    pass
  finally:
    debug_display_subscriber.destroy_node()
    debug.close()
    rclpy.shutdown()

if __name__ == '__main__':
  main()