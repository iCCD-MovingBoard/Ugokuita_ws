import rclpy
from rclpy.node import Node
from std_msgs.msg import String

LIDAR_ID = 1

class CommandIntegrator(Node):
    def __init__(self):
        super().__init__('command_integrator_negotiator')
        self.subscription = self.create_subscription(String, 'request_topic', self.listener_callback, 10)
        # self.subscription  # prevent unused variable warning
        self.publisher = self.create_publisher(String, 'serial_send_topic', 10)
        self.stop_count = 0

    def listener_callback(self, msg):
        commands = msg.data.split(',')
        send = String()

        if self.stop_count > 0:
            self.stop_count -= 1
            send.data = '0,0'
            self.publisher.publish(send)
            return
        
        for index, command in enumerate(commands):
            if index == 0: 
                if command == LIDAR_ID:
                    self.stop_count = 200
                continue
            if index != 1: send.data += ','
            
            integrated_command = command
            if self.stop_count > 0:
                if 'R' in command:
                    integrated_command = 'R0'
                    self.stop_count -= 1
                elif 'L' in command:
                    integrated_command = 'L0'
                    self.stop_count -= 1

            send.data += integrated_command

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