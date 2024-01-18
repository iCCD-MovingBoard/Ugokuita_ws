#!/bin/bash
for option in "$@"
do
  if [ "${option}" = "build" ]; then
    echo "build"
    # colcon build --symlink --packages-select controller_pkg motor_pkg  debug_launch ydlidar_ros2_driver
  fi
done

. install/setup.bash

echo "run"
for option in "$@"
do
  if [ "${option}" = "view" ]; then
    ros2 launch ydlidar_ros2_driver ydlidar_launch_view.py
  else
    ros2 launch debug_launch controller_controll.launch.py
  fi
done