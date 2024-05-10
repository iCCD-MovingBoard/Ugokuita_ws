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
    self.isLightOn = False
    self.beforeXinput = 0

  def listener_callback(self, msg):
    self.get_logger().info('I heard: "%s"' % msg.data)
    if msg.data == '#stop':
      if self.canMove == True:
        self.get_logger().warn('STOP')
      self.canMove = False
      return # msg.dataにコントローラーの入力は含まれていないので、ここで処理を終了する
    
    if msg.data == '#start':
      if self.canMove == False:
        self.get_logger().warn('START')
      self.canMove = True
      return # msg.dataにコントローラーの入力は含まれていないので、ここで処理を終了する
    
    controller_inputs: dict = str_converter.to_dict(msg.data)
    
    axis_x = int(controller_inputs['L_Axis_x'])
    axis_y = int(controller_inputs['L_Axis_y'])
    right = -axis_x - axis_y
    left  =  axis_x - axis_y
    
    if self.canMove == False:
      if right > 0: right = 0
      if left > 0: left = 0
      uart.send_to_motordriver('B300')
    
    scaled_speed_r = uart.scale_speed(right)
    scaled_speed_l = uart.scale_speed(left)
    adjusted_speed_r, adjusted_speed_l = uart.adjust_speed(scaled_speed_r, scaled_speed_l)
    
    uart.send_to_motordriver(f'R{adjusted_speed_r}')
    uart.send_to_motordriver(f'L{adjusted_speed_l}')

    currentXinput = controller_inputs["X"]
    if currentXinput == 1 and self.beforeXinput == 0:
      self.isLightOn = not self.isLightOn
    uart.send_to_motordriver(f'H{int(self.isLightOn)}')
    
    if controller_inputs["Y"] == 1:
      uart.send_to_motordriver('B300')

def main(args=None):
  try:
    rclpy.init(args=args)
    controller_subscriber = MotorSubscriber()
    rclpy.spin(controller_subscriber)
  except KeyboardInterrupt:
    pass
  finally:
    uart.send_to_motordriver(0, 0, 0, 0)
    controller_subscriber.destroy_node()
    uart.uart_port.close()
    rclpy.shutdown()

if __name__ == '__main__':
  main()