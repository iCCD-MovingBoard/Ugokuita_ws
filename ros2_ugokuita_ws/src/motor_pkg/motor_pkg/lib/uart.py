import serial
import time
from subprocess import run
import json

jetson_port = '/dev/uart_pico'
#run(f'sudo chmod 777 {jetson_port}', shell=True)

BAUDRATE = 115200
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

UART_MAX_VALUE = 4

# -32768 ~ 32767の範囲の値を 0 ~ 256の範囲に変換する
def scale_speed(speed):
    # 入力された値が一定以上小さい場合は入力を無効とする。
    # 今は閾値が1000になっているが割と適当に決めている。
    threshold = 100
    if -threshold < speed < threshold: return 0
    CONTROLLER_MAX_VALUE = 32767
    CONV_RATE = UART_MAX_VALUE / CONTROLLER_MAX_VALUE
    scaled_speed = speed * CONV_RATE
    return round(scaled_speed, 2)

def send_to_motordriver(port, speed_r: int, speed_l:int):
    scaled_speed_r = scale_speed(speed_r)
    scaled_speed_l = scale_speed(speed_l)
    threshold = UART_MAX_VALUE*0.9
    if scaled_speed_r > threshold and scaled_speed_l > threshold:
        scaled_speed_r = UART_MAX_VALUE
        scaled_speed_l = UART_MAX_VALUE
    if scaled_speed_r < -threshold and scaled_speed_l < -threshold:
        scaled_speed_r = -UART_MAX_VALUE
        scaled_speed_l = -UART_MAX_VALUE

    port.write(bytes(f'R{float(scaled_speed_r)}\n', encoding='ascii'))
    port.write(bytes(f'L{float(scaled_speed_l)}\n', encoding='ascii'))

def main():
    try:
        while True:
            for i in range(-1100, 1100, 10):
                send_to_motordriver(uart_port, i, i)
                receive_data = uart_port.readline()
                print(receive_data)
                receive_data = uart_port.readline()
                print(receive_data)
                
                time.sleep(TIMEOUT)
    except KeyboardInterrupt:
        uart_port.close()

if __name__ == '__main__':
    main()
