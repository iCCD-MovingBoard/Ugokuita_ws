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
    timer_period = 0.001  # seconds
    self.timer = self.create_timer(timer_period, self.timer_callback)
    self.i = 0
    self.joycon = Joycon("/dev/input/js0")
    self.beforeXinput = 0
    self.currentXinput = 0
    self.isLightOn = False

  def timer_callback(self):
    controller_data: dict = self.joycon.state
    forward  = controller_data['RT'] - controller_data['LT']
    axis_x = controller_data['L_Axis_x']
    
    # -1 ~ 1
    to_right = -axis_x
    
    # # -32767 ~ 32767
    right = forward*to_right/32767 + forward*0.5
    left  = -forward*to_right/32767 + forward*0.5
    if to_right > 0:
      right = 0.5*forward
    if to_right < 0:
      left = 0.5*forward
    
    # uart通信の範囲 -400 ~ 400に変換
    right = str_converter.toUART(right, 32767)
    left  = str_converter.toUART(left, 32767)
    
    right, left = str_converter.adjust_speed(right, left)
    
    msg = String()
    msg.data = f"ID{CONTROLLER_ID},R{right},L{left},H{int(self.isLightOn)}"
    
    self.beforeXinput = self.currentXinput
    self.currentXinput = controller_data["X"]
    if self.currentXinput == 1 and self.beforeXinput == 0:
      self.isLightOn = not self.isLightOn
    if controller_data["Y"] == 1:
      buzzer_furequency = 300
      msg.data += f",B{buzzer_furequency}"

    self.publisher_.publish(msg)
    # self.get_logger().warning('Publishing: "%s"' % str(msg))
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