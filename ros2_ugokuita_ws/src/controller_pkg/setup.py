from setuptools import setup

package_name = 'controller_pkg'

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
  maintainer='canada',
  maintainer_email='acavalkyrie@gmail.com',
  description='controllelr publisher and subscriber',
  license='Apache License 2.0',
  tests_require=['pytest'],
  entry_points={
    'console_scripts': [
      'controller_publisher = controller_pkg.controller_publisher:main',
      'controller_subscriber = controller_pkg.controller_subscriber:main',
    ],
  },
)