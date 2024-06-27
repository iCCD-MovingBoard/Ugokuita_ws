def to_str(byte_str):
    str = byte_str.decode('utf-8')
    return str

def to_dict(str):
    # strを辞書に変換する
    dict = {}
    for key_value in str.split(','):
        key, value = key_value.split(':')
        dict[key] = value
    return dict

UART_MAX_VALUE = 250

# -32768 ~ 32767の範囲の値を 0 ~ 256の範囲に変換する
def toUART(speed, max):
    # 入力された値が一定以上小さい場合は入力を無効とする。
    # 今は閾値が1000になっているが割と適当に決めている。
    threshold = 500
    if -threshold < speed < threshold: return 0
    CONV_RATE = UART_MAX_VALUE / max
    scaled_speed = speed * CONV_RATE
    return round(scaled_speed, 2)# 小数点第2位まで残す

# 左右の速度が両方とも一定値以上の場合はどちらも最大値に変換して直進性を上げる関数
def adjust_speed(speed_r, speed_l):
    threshold = UART_MAX_VALUE*0.9
    if speed_r > threshold and speed_l > threshold:
        speed_r = UART_MAX_VALUE
        speed_l = UART_MAX_VALUE
    if speed_r < -threshold and speed_l < -threshold:
        speed_r = -UART_MAX_VALUE
        speed_l = -UART_MAX_VALUE
    return speed_r, speed_l
