# CMake generated Testfile for 
# Source directory: /home/iccd/Documents/Ugokuita_ws/YDLidar-SDK/python
# Build directory: /home/iccd/Documents/Ugokuita_ws/YDLidar-SDK/build/python
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(ydlidar_py_test "/usr/bin/python" "/home/iccd/Documents/Ugokuita_ws/YDLidar-SDK/python/test/pytest.py")
set_tests_properties(ydlidar_py_test PROPERTIES  ENVIRONMENT "PYTHONPATH=/opt/ros/dashing/lib/python3.6/site-packages:/home/iccd/Documents/Ugokuita_ws/YDLidar-SDK/build/python")
subdirs("examples")
