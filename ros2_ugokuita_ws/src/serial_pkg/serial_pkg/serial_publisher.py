import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from .lib import uart

class SerialPublisher(Node):
    def __init__(self):
        super().__init__('serial_publisher')
        self.publisher_ = self.create_publisher(String, 'serial_recieve_topic', 10)
        timer_period = 0.0001  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        data = uart.receive_data()
        msg.data = str(data)
        
        self.publisher_.publish(msg)
        self.i += 1

def main(args=None):
    try:
        rclpy.init(args=args)
        serial_publisher = SerialPublisher()
        rclpy.spin(serial_publisher)
    except KeyboardInterrupt:
        pass
    finally:
        serial_publisher.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()