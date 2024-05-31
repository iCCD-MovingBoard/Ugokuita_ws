import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from .lib.controller import Joycon
from custom_msg.msg import RequestCommand
CONTROLLER_ID = 2
from .lib import str_converter

class ControllerPublisher(Node):
  
  def __init__(self):
    super().__init__('controller_publisher')
    self.publisher_ = self.create_publisher(dict, 'serial_topic', 10)
    timer_period = 0.0001  # seconds
    self.timer = self.create_timer(timer_period, self.timer_callback)
    self.i = 0
    self.joycon = Joycon("/dev/input/js0")
    self.beforeXinput = 0
    self.isLightOn = False

  def timer_callback(self):
    controller_data: str = self.joycon.get()

    axis_x = int(controller_data['L_Axis_x'])
    axis_y = int(controller_data['L_Axis_y'])
    right = str_converter.scale_speed(-axis_x - axis_y)
    left  = str_converter.scale_speed( axis_x - axis_y)
    right, left = str_converter.adjust_speed(right, left)
    
    beforeXinput = currentXinput
    currentXinput = controller_data["X"]
    if currentXinput == 1 and beforeXinput == 0:
      self.isLightOn = not self.isLightOn
    buzzer_frequency = -1
    if controller_data["Y"] == 1:
      buzzer_furequency = 300

    msg = {
      "id": CONTROLLER_ID,
      "r": right,
      "l": left,
      "h": self.isLightOn,
      "b": buzzer_furequency
    }
    self.publisher_.publish(msg)
    self.get_logger().info('Publishing: "%s"' % str(msg))
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