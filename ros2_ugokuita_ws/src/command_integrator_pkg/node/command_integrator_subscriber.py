import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from custom_msg.msg import RequestCommand, SendCommand
LIDAR_ID = 1

class CommandIntegrator(Node):
    def __init__(self):
        super().__init__('command_integrator_subscriber')
        self.subscription = self.create_subscription(RequestCommand, 'request_topic', 10)
        self.subscription  # prevent unused variable warning
        self.publisher = self.create_publisher(SendCommand, 'serial_send_topic', 10)

    def listener_callback(self, msg):
        send = SendCommand()
        send.r = msg.r
        send.l = msg.l
        send.h = msg.h
        send.b = msg.b
        self.publisher.publish(send)
        

def main(args=None):
    try:
        rclpy.init(args=args)
        command_integrator = CommandIntegrator()
        rclpy.spin(command_integrator)
    except KeyboardInterrupt:
        pass
    finally:
        command_integrator.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()