import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

import subprocess

def detect_os_version():
  version_id: str = (subprocess.Popen('. /etc/os-release && echo $VERSION_ID', stdout=subprocess.PIPE, shell=True).communicate()[0]).decode('utf-8')
  version_id: float = float(version_id)
  return version_id


def generate_launch_description():
  os_version: int = detect_os_version()
  if os_version == 18.04:
    return launch.LaunchDescription([
      launch_ros.actions.Node(package='controller_pkg', node_executable='controller_publisher'),
      launch_ros.actions.Node(package='motor_pkg',      node_executable='motor_subscriber', output='screen')
    ])
  elif os_version == 22.04:
    return launch.LaunchDescription([
      launch_ros.actions.Node(package='controller_pkg', executable='controller_publisher'),
      launch_ros.actions.Node(package='motor_pkg',      executable='motor_subscriber', output='screen')
    ])

if __name__ == '__main__':
  detect_os_version()