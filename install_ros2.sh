# ros2インストール用
sudo apt update && sudo apt install -y curl gnupg2 lsb-release
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" \
    | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
sudo apt update && sudo apt install -y ros-dashing-desktop

source /opt/ros/dashing/setup.bash
sudo apt install -y python3-pip
pip3 install -U argcomplete
sudo apt install -y \
    python3-colcon-common-extensions \
    ros-dashing-ros2bag \
    ros-dashing-rosbag2-converter-default-plugins \
    ros-dashing-rosbag2-storage-default-plugins \
    ros-dashing-rqt*
