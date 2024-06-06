import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from .lib.controller import Joycon
CONTROLLER_ID = 2
from .lib import str_converter

class ControllerPublisher(Node):
  def __init__(self):
    super().__init__('controller_publisher')
    self.publisher_ = self.create_publisher(String, 'request_topic', 10)
    timer_period = 0.0001  # seconds
    self.timer = self.create_timer(timer_period, self.timer_callback)
    self.i = 0
    self.joycon = Joycon("/dev/input/js0")
    self.beforeXinput = 0
    self.isLightOn = False

  def timer_callback(self):
    controller_data: dict = self.joycon.get()

    axis_x = controller_data['L_Axis_x']
    axis_y = controller_data['L_Axis_y']
    right = str_converter.scale_speed(-axis_x - axis_y)
    left  = str_converter.scale_speed( axis_x - axis_y)
    right, left = str_converter.adjust_speed(right, left)
    msg = String()
    msg.data = f"ID{CONTROLLER_ID},R{right},L{left},H{self.isLightOn}"
    
    beforeXinput = currentXinput
    currentXinput = controller_data["X"]
    if currentXinput == 1 and beforeXinput == 0:
      self.isLightOn = not self.isLightOn
    if controller_data["Y"] == 1:
      buzzer_furequency = 300
      msg.data += f",B{buzzer_furequency}"

    self.publisher_.publish(msg)
    self.get_logger().warning('Publishing: "%s"' % str(msg))
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