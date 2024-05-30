#!/bin/bash
for option in "$@"
do
  if [ "${option}" = "build" ]; then
    # echo "build"
    colcon build --symlink --packages-select controller_pkg serial_pkg debug_launch ydlidar_ros2_driver collision_lidar_pkg command_integrator_pkg custom_msg
  fi
done

. install/setup.bash

# echo "run"
if [ $# -eq 0 ]; then
    ./kill_ros2_nodes.sh
    ros2 launch debug_launch controller_controll.launch.py
    exit
fi

for option in "$@"
do
  if [ "${option}" = "view" ]; then
    ros2 launch ydlidar_ros2_driver ydlidar_launch_view.py
  fi
done

#ros2 launch debug_launch controller_controll.launch.py
