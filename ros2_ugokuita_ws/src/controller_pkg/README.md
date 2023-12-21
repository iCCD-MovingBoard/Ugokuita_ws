# controller package
このパッケージは/dev/input/js0に接続されたコントローラーの左スティックの入力を読み出して、motor_topicという名前のトピックを立ててそこにスティックの読み値を書き込むものです。

パッケージ内には２つのノードがあります。
- controller_publisher
- controller_subscriber

## controller_publisher
コントローラーのスティック入力を読み取ってトピックに書き込むノード

## controller_subscriber
motor_topicを読んで画面に出力します。
デバッグ用です。
本番環境では使わないはずです。