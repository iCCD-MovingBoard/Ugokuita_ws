from setuptools import find_packages, setup

package_name = 'controller_pkg'
submodules = 'controller_pkg/lib'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name, submodules],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='canada',
    maintainer_email='acavalkyrie@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'controller_publisher = controller_pkg.controller_publisher:main',
            'controller_subscriber = controller_pkg.controller_subscriber:main',
        ],
    },
)
