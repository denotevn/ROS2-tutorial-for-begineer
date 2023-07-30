#include "rclcpp/rclcpp.hpp"
# include "example_interfaces/srv/add_two_ints.hpp"

class AddTwoIntsClientNode: public rclcpp::Node  // mofify name
{
    public:
        AddTwoIntsClientNode(): Node("cpp_test") // modify name
        {
            thread1_ = std::thread(std::bind(&AddTwoIntsClientNode::callAddTwoIntsService, this, 1, 4));
            // send multiple to the server
            threads_.push_back(std::thread(std::bind(&AddTwoIntsClientNode::callAddTwoIntsService, this, 1, 4)));
            

        }

        void callAddTwoIntsService(int a, int b)
        {
            auto client = this->create_client<example_interfaces::srv::AddTwoInts>("add_two_ints");
            while (!client->wait_for_service(std::chrono::seconds(1)))
            {
                RCLCPP_WARN(this->get_logger(), "Waiting for the server to be up ...");
            }

            auto request = std::make_shared<example_interfaces::srv::AddTwoInts::Request>();
            request->a = a;
            request->b = b;

            auto future = client->async_send_request(request);

            try{
                auto respone = future.get();
                RCLCPP_INFO(this->get_logger(), "%ld + %ld = %ld", request->a, request->b, respone->sum);

            }catch(const std::exception &e)
            {
                RCLCPP_ERROR(this->get_logger(), "Service call failed !");
            }
        }

    private:
        std::thread thread1_;
        // multiple send
        std::vector<std::thread> threads_;
};
int main(int argc, char **argv)
{
    rclcpp::init(argc,argv);
    auto node = std::make_shared<AddTwoIntsClientNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}