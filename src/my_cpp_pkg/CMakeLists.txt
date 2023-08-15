cmake_minimum_required(VERSION 3.8)
project(my_cpp_pkg)

# default to C++14
if (NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(example_interfaces REQUIRED)
find_package(my_robot_interfaces REQUIRED)

add_executable(cpp_node src/my_first_node.cpp)
ament_target_dependencies(cpp_node rclcpp)


## them file moi de chay vao add_excutable()
add_executable(robot_news_station src/robot_news_station.cpp) # trung voi file name and node name
ament_target_dependencies(robot_news_station rclcpp example_interfaces) # them cac thu vin can thiet duoi nay

add_executable(smartphone src/smartphone.cpp)
ament_target_dependencies(smartphone rclcpp example_interfaces)

add_executable(add_two_ints_server src/add_two_ints_server.cpp)
ament_target_dependencies(add_two_ints_server rclcpp example_interfaces)

add_executable(add_two_ints_client_no_oop src/add_two_ints_client_no_oop.cpp)
ament_target_dependencies(add_two_ints_client_no_oop rclcpp example_interfaces)

add_executable(add_two_ints_client src/add_two_ints_client.cpp)
ament_target_dependencies(add_two_ints_client rclcpp example_interfaces)

add_executable(hardware_status_publisher src/hw_status_publisher.cpp)
ament_target_dependencies(hardware_status_publisher rclcpp my_robot_interfaces)

# we asked to create an executable and then to place this executable into the lib folder here
install(TARGETS
  cpp_node
  # add publisher_node
  robot_news_station
  smartphone
  add_two_ints_server
  add_two_ints_client
  add_two_ints_client_no_oop
  hardware_status_publisher
  DESTINATION lib/${PROJECT_NAME}

)


ament_package()
