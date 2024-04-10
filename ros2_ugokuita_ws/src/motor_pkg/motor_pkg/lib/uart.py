import serial
import time
from subprocess import run

jetson_port = '/dev/uart_usb'
#run(f'sudo chmod 777 {jetson_port}', shell=True)

BAUDRATE = 9600
TIMEOUT = 0.01
STOPBITS = serial.STOPBITS_ONE
PARITY = serial.PARITY_NONE
BYTESIZE = serial.EIGHTBITS

uart_port = serial.Serial(jetson_port,
                            baudrate=BAUDRATE,
                            timeout=TIMEOUT,
                            stopbits=STOPBITS,
                            parity=PARITY,
                            bytesize=BYTESIZE)

# -32768 ~ 32767の範囲の値をモーターの指令値に変換する
# 指令値: [速] 500 ~ 5000 [遅]
# 安全な範囲が5000 ~ 2000ぐらいらしいので、-32768 ~ 32767の範囲をこの範囲に収める
def scale_speed(speed):
    # 入力された値が一定以上小さい場合は入力を無効とする。
    # 今は閾値が1000になっているが割と適当に決めている。
    if speed < 1000:
        return 5001
    CONTROLLER_MAX_VALUE = 32767
    UART_MAX_VALUE = 5000
    UART_MIN_VALUE = 2000
    CONV_RATE = (UART_MAX_VALUE - UART_MIN_VALUE) / CONTROLLER_MAX_VALUE
    speed = UART_MAX_VALUE - speed * CONV_RATE
    return speed
    
# 通信Protocol: 0xFF,R,R_D,L,L_D\r\n
# R: 右モーターの速度 500 ~ 5000
# R_D: 右モーターの方向 0 ~ 1 (0: 正転, 1: 逆転)
# L: 左モーターの速度 500 ~ 5000
# L_D: 左モーターの方向 0 ~ 1 (0: 正転, 1: 逆転)
# 5001を送ると停止する
def send_to_motordriver(port, speed_r: int, speed_l:int):
    scaled_speed_r = scale_speed(speed_r)
    scaled_speed_l = scale_speed(speed_l)
    direction_r = 0 if scaled_speed_r > 0 else 1
    direction_l = 0 if scaled_speed_l > 0 else 1
    port.write(0xff)
    port.write(f',{scaled_speed_r},{direction_r}')
    port.write(f',{scaled_speed_l},{direction_l}\r\n')

def main():
    try:
        while True:
            for i in range(256):
                send_data = bytes([i])
                uart_port.write(send_data)
                receive_data = uart_port.readline()
                print(receive_data)
                
                time.sleep(TIMEOUT)
    except KeyboardInterrupt:
        uart_port.close()

if __name__ == '__main__':
    main()
