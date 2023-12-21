import serial
import time
from subprocess import run

jetson_port = '/dev/ttyUSB0'
run(f'sudo chmod 777 {jetson_port}', shell=True)

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

# 0 ~ 32767の範囲の値を 0 ~ 256の範囲に変換する
def scale_speed(speed):
    CONTROLLER_MAX_VALUE = 32767
    UART_MAX_VALUE = 254
    CONV_RATE = UART_MAX_VALUE / CONTROLLER_MAX_VALUE
    speed = int(speed * CONV_RATE)
    if speed < 10: speed = 0
    return speed

def send_to_motordriver(port, speed_r: int, speed_l:int):
    scaled_speed_r = scale_speed(speed_r)
    scaled_speed_l = scale_speed(speed_l)
    port.write(bytes([0xFF]))
    port.write(b',')
    port.write(bytes([scaled_speed_r]))
    port.write(b',')
    port.write(bytes([scaled_speed_l]))
    port.write(b'\r\n')

def main():
    try:
        while True:
            for i in range(256):
                send_data = bytes([i])
                uart_port.write(send_data)
                receive_data = uart_port.readline()
                
                time.sleep(TIMEOUT)
    except KeyboardInterrupt:
        uart_port.close()

if __name__ == '__main__':
    main()
