#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

using std::placeholders::_1;

class MotorSubscriber : public rclcpp::Node
{
  public:
    MotorSubscriber(): Node("motor_subscriber"){
      subscription = this->create_subscription<std_msgs::msg::String>(
        "motor_topic", 10, std::bind(&MotorSubscriber::sub_callback, this, _1));
    }

  private:
    void sub_callback(const std_msgs::msg::String::SharedPtr msg) const
    {
      RCLCPP_INFO(this->get_logger(), "I heard: '%s'", msg->data.c_str());
    }
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription;
};

int main(int argc, char* argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<MotorSubscriber>());
  rclcpp::shutdown();
  return 0;
}