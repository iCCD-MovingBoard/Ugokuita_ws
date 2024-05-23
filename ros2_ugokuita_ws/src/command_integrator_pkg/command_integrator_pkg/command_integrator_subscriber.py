import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from ...common.type_difinition import RequestCommand, SendCommand
from ...common.type_difinition import LIDAR_ID


class CommandIntegrator(Node):
    def __init__(self):
        super().__init__('command_integrator_subscriber')
        self.subscription = self.create_subscription(RequestCommand, 'request_topic', 10)
        self.subscription  # prevent unused variable warning
        self.publisher = self.create_publisher(SendCommand, 'serial_send_topic', 10)

    def listener_callback(self, msg):
        self.publisher.publish(SendCommand(msg.r, msg.l, msg.h, msg.b))
        

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