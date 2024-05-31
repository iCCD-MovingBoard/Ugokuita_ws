import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from rclpy.qos import QoSDurabilityPolicy, QoSHistoryPolicy, QoSReliabilityPolicy, QoSProfile
from sensor_msgs.msg import LaserScan
# from custom_msg.msg import RequestCommand
LIDAR_ID = 1

class ControllerSubscriber(Node):
    def __init__(self):
        super().__init__('collision_lidar_subscriber')

        qos_profile = QoSProfile(depth=10)
        qos_profile.reliability = QoSReliabilityPolicy.BEST_EFFORT
        qos_profile.durability = QoSDurabilityPolicy.VOLATILE

        self.subscription = self.create_subscription(LaserScan, 'scan', self.listener_callback, qos_profile)
        self.subscription  # prevent unused variable warning

        self.publisher = self.create_publisher(String, 'request_topic', 10)

    def listener_callback(self, msg):
        half_degrees = 30 # degrees
        half_range = int(251*half_degrees/180)
        collision_distance_threshold = 1.5
        for i in range(251 - half_range, 251 + half_range):
            value = msg.ranges[i]
            if value == 0.0: continue
            if value < collision_distance_threshold:
                request = f"ID{LIDAR_ID},R0,L0"
                self.publisher.publish(request)
                return
        # self.publisher.publish(String(data='#start'))
        # self.get_logger().warn('I heard: "%s"' % value)

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