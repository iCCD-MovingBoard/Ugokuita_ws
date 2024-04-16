import serial
import time
from subprocess import run
import json

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

# -32768 ~ 32767の範囲の値を 0 ~ 256の範囲に変換する
def scale_speed(speed):
    # 入力された値が一定以上小さい場合は入力を無効とする。
    # 今は閾値が1000になっているが割と適当に決めている。
    if speed < 1000: speed = 0
    CONTROLLER_MAX_VALUE = 32767
    UART_MAX_VALUE = 1
    CONV_RATE = UART_MAX_VALUE / CONTROLLER_MAX_VALUE
    speed = speed * CONV_RATE
    return speed

def send_to_motordriver(port, speed_r: int, speed_l:int):
    scaled_speed_r = abs(scale_speed(speed_r))
    scaled_speed_l = abs(scale_speed(speed_l))
    is_forward_r = True if speed_r > 0 else False
    is_forward_l = True if speed_l > 0 else False
    send_data_dict = {
        "rspeed": scaled_speed_r,
        "lspeed": scaled_speed_l,
        "rIsForward": is_forward_r,
        "lIsForward": is_forward_l
    }
    send_data_str = json.dumps(send_data_dict)
    if port.is_open:
        port.write(f'{send_data_str}\n\r'.encode())    

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
