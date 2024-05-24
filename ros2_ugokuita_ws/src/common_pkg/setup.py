from setuptools import find_packages, setup

package_name = 'common_pkg'
# submodules = 'common/lib'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],#, submodules],
    py_modules=['common_pkg.lib.type_difinition'],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='canada',
    maintainer_email='acavalkyrie@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
