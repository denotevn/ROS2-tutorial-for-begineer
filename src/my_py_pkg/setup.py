from setuptools import setup

package_name = 'my_py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tuandinh',
    maintainer_email='dinhngoctuan2131997@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # file path of node you want to install
            # we start from the main function
            "py_node= my_py_pkg.my_first_node:main",
            "robot_news_station=my_py_pkg.robot_news_station:main",
            # robot_news_station so 2 la ten cua file .py
            "smartphone=my_py_pkg.smartphone:main",
            "add_two_ints_server=my_py_pkg.add_two_ints_server:main",
            "add_two_ints_client=my_py_pkg.add_two_ints_client:main",
            "add_two_ints_client_no_oop=my_py_pkg.add_two_ints_client_no_oop:main",
            "hw_status_publisher=my_py_pkg.hw_status_publisher:main",
            "led_panel=my_py_pkg.led_panel:main",
            "battery = my_py_pkg.battery:main"
            
        ],
    },
)
