from setuptools import setup

package_name = 'my_py_ex2_pkg'

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
            "number_publisher=my_py_ex2_pkg.number_publisher:main",
            "number_counter=my_py_ex2_pkg.number_counter:main"
        ],
    },
)
