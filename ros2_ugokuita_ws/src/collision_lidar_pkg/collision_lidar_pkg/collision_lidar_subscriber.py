import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from rclpy.qos import QoSDurabilityPolicy, QoSHistoryPolicy, QoSReliabilityPolicy, QoSProfile
from sensor_msgs.msg import LaserScan

class ControllerSubscriber(Node):
    def __init__(self):
        super().__init__('collision_lidar_subscriber')

        qos_profile = QoSProfile(depth=10)
        qos_profile.reliability = QoSReliabilityPolicy.BEST_EFFORT
        qos_profile.durability = QoSDurabilityPolicy.VOLATILE

        self.subscription = self.create_subscription(LaserScan, 'scan', self.listener_callback, qos_profile)
        self.subscription  # prevent unused variable warning

        self.publisher = self.create_publisher(String, 'motor_topic', 10)


    def listener_callback(self, msg):
        value = msg.ranges[252]
        if value == 0.0: return
        if value > 1: return
        self.get_logger().warn('I heard: "%s"' % value)
        self.publisher.publish(String(data='#stop'))

def main(args=None):
    try:
        rclpy.init(args=args)
        controller_subscriber = ControllerSubscriber()
        rclpy.spin(controller_subscriber)
    except KeyboardInterrupt:
        pass
    finally:
        controller_subscriber.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()