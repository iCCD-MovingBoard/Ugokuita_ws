![構成図](./構成図.drawio.svg)

# 環境構築

1. ros2のインストール
```bash
$ ./install_ros2.sh
```
2. YDLidar-SDKのインストール
```bash
$ cd YDLidar-SDK
$ ./build_sdk_env.sh
```
3. packageのbuild
```bash
$ cd ros2_ugokuita_ws
$ ./run.sh build
```