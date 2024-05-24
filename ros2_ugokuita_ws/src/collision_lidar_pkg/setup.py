from setuptools import find_packages, setup

package_name = 'collision_lidar_pkg'
submodules = 'collision_lidar_pkg/lib'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name, submodules, 'common_pkg'],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'common_pkg'],
    zip_safe=True,
    maintainer='canada',
    maintainer_email='acavalkyrie@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'collision_lidar_subscriber = collision_lidar_pkg.collision_lidar_subscriber:main',
            'collision_lidar_publisher = collision_lidar_pkg.collision_lidar_subscriber:main'
        ],
    },
)
