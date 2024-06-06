import rclpy
from rclpy.node import Node

from std_msgs.msg import String
LIDAR_ID = 1

class CommandIntegrator(Node):
    def __init__(self):
        super().__init__('command_integrator_negotiator')
        self.subscription = self.create_subscription(String, 'request_topic', 10)
        # self.subscription  # prevent unused variable warning
        self.publisher = self.create_publisher(String, 'serial_send_topic', 10)

    def listener_callback(self, msg):
        commands = msg.data.split(',')
        send = String()
        for index, command in enumerate(commands):
            if index == 0: continue
            if index != 1: send.data += ','
            send.data += command

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