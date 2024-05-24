from setuptools import find_packages, setup

package_name = 'serial_pkg'
submodules = 'serial_pkg/lib'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name, submodules, 'common'],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'common'],
    zip_safe=True,
    maintainer='canada',
    maintainer_email='acavalkyrie@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'serial_subscriber = serial_pkg.serial_subscriber:main',
        ],
    },
)
