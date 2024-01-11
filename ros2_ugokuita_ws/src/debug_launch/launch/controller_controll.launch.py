import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

import subprocess

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import LifecycleNode
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.actions import LogInfo

import lifecycle_msgs.msg
import os

def controller_motor_nodes():
  controller_node = launch_ros.actions.Node(package='controller_pkg', node_executable='controller_publisher')
  motor_node      = launch_ros.actions.Node(package='motor_pkg',      node_executable='motor_subscriber'
                                            # ,output='screen'
                                            )
  return controller_node, motor_node

def lidar_nodes():
  share_dir = get_package_share_directory('ydlidar_ros2_driver')
  parameter_file = LaunchConfiguration('params_file')
  node_name = 'ydlidar_ros2_driver_node'

  params_declare = DeclareLaunchArgument('params_file',
                                          default_value=os.path.join(
                                              share_dir, 'params', 'ydlidar.yaml'),
                                          description='FPath to the ROS2 parameters file to use.')

  driver_node = Node(package='ydlidar_ros2_driver',
                              node_executable='ydlidar_ros2_driver_node',
                              node_name='ydlidar_ros2_driver_node',
                              output='screen',
                              #emulate_tty=True,
                              parameters=[parameter_file],
                              node_namespace='/',
                              )
  tf2_node = Node(package='tf2_ros',
                  node_executable='static_transform_publisher',
                  node_name='static_tf_pub_laser',
                  arguments=['0', '0', '0.02','0', '0', '0', '1','base_link','laser_frame'],
                  )
  return params_declare, driver_node, tf2_node

def generate_launch_description():
  controller_node, motor_node = controller_motor_nodes()
  params_declare, driver_node, tf2_node = lidar_nodes()
  
  return LaunchDescription([
    params_declare,
    driver_node,
    tf2_node,

    controller_node,
    motor_node,
  ])
  

if __name__ == '__main__':
  detect_os_version()