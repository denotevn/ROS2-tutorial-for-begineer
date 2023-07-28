#include "rclcpp/rclcpp.hpp"

class MyNode: public rclcpp::Node  // mofify name
{
    public:
        MyNode(): Node("cpp_test") // modify name
        {
        }
    private:
};
int main(int argc, char **argv)
{
    rclcpp::init(argc,argv);
    auto node = std::make_shared<MyNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}