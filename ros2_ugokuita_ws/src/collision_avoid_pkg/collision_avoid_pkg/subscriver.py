import rclpy
from rclpy.node import Node
from typing import List, Dict

from sensor_msgs.msg import PointCloud2

class RealsenseSubscriver(Node):
    def __init__(self):
        super().__init__('realsense_subscriver') # type: ignore
        self.subscription = self.create_subscription(PointCloud2, '/camera/aligned_depth_to_color/color/points', self.listener_callback, 10)
        self.subscription

    def convert_dict(self, msg: PointCloud2) -> List[Dict[str, float]]:
        points:List[Dict[str, float]] = []
        is_bigendian = msg.is_bigendian
        data = msg.data
        index = 0

        for index in range(msg.width * msg.height):
            x = float(data[index * 4])
            y = float(data[index *4 + 1])
            z = float(data[index *4 + 2])
            rgb = float(data[index *4 + 3])
            points.append({'x':x,'y':y,'z':z, 'rgb':rgb})
        return points

    def listener_callback(self, msg: PointCloud2):
        points = self.convert_dict(msg)
        # 前方にあるものだけを絞り込む
        width = msg.width
        height = msg.height
        # 前の座標を中心としてベクトルの大きさを計算
        min_z = 0.0
        for point in points:
            z = point['z']
            if(z == 0.0): continue
            min_z = min(min_z, z)

        self.get_logger().info("最も近いよ: {0}".format(min_z))

def main(args=None):
    try:
        rclpy.init()
        realsense_subscriver = RealsenseSubscriver()
        rclpy.spin(realsense_subscriver)
    except KeyboardInterrupt:
        pass
    finally:
        realsense_subscriver.destroy_node()
        rclpy.shutdown()