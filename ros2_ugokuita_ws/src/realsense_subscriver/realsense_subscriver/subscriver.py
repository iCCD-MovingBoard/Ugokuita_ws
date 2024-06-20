import rclpy
from rclpy.node import Node
from typing import List, Dict
import pyrealsense2 as rs
import numpy as np

from sensor_msgs.msg import PointCloud2


class RealsenseSubscriver(Node):
    def __init__(self):
        conf = rs.config()
        conf.enable_stream(rs.stream.color, 1280, 720, rs.format.bgr8, 30)
        conf.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 30)
        self.pipeline = rs.pipeline()
        self.pipeline.start(conf)
        try:
            self.callback(self.pipeline)
        except KeyboardInterrupt:
            pass

    def callback(self, pipeline):
        while True:
            camera = pipeline.wait_for_frames()
            # color_frame = camera.get_color_frame()
            depth_frame = camera.get_depth_frame()
            depth_data = depth_frame.get_distance(640, 360)
            print(depth_data)


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
