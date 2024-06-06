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

def send_command(send_data: str):
    uart_port.write(bytes(f'{send_data}\n', encoding='ascii'))

def main():
    try:
        while True:
            for i in range(-1100, 1100, 10):
                send_command(f'R{i}')
                send_command(f'L{i}')
                receive_data = uart_port.readline()
                print(receive_data)
                receive_data = uart_port.readline()
                print(receive_data)
                
                time.sleep(TIMEOUT)
    except KeyboardInterrupt:
        uart_port.close()

if __name__ == '__main__':
    main()
