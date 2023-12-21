import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

import os
import platform

import re

def detect_os_version():
  os_version: str = platform.version()
  version: str = re.search(r'~[\d]*', os_version).group()
  version: str = version[1:]
  version: int = int(version)
  # print(version)
  return version


def generate_launch_description():
  os_version: int = detect_os_version()
  if os_version == 18:
    return launch.LaunchDescription([
      launch_ros.actions.Node(package='controller_pkg', node_executable='controller_publisher'),
      launch_ros.actions.Node(package='motor_pkg',      node_executable='motor_subscriber')
    ])
  elif os_version == 22:
    return launch.LaunchDescription([
      launch_ros.actions.Node(package='controller_pkg', executable='controller_publisher'),
      launch_ros.actions.Node(package='motor_pkg',      executable='motor_subscriber')
    ])

if __name__ == '__main__':
  detect_os_version()