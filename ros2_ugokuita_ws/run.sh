colcon build --symlink --packages-select controller_pkg motor_pkg  debug_launch ydlidar_ros2_driver
. install/setup.bash
ros2 launch debug_launch controller_controll.launch.py
# ros2 launch ydlidar_ros2_driver ydlidar_launch_view.py
```