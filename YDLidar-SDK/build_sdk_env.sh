sudo apt install cmake pkg-config
sudo apt-get install swig
sudo apt-get install python3-pip
cd build
cmake ..
make
sudo make install
cd ..
pip install .