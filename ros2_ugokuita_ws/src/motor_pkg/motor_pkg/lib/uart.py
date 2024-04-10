import serial
import time
from subprocess import run
import json

jetson_port = '/dev/uart_pico'
#run(f'sudo chmod 777 {jetson_port}', shell=True)

BAUDRATE = 115200
TIMEOUT  = 0.01
STOPBITS = serial.STOPBITS_ONE
PARITY   = serial.PARITY_NONE
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
    threshold = 1000
    if -threshold < speed < threshold:
        return 5001
    CONTROLLER_MAX_VALUE = 32767
    UART_MAX_VALUE = 5000
    UART_MIN_VALUE = 2000
    CONV_RATE = (UART_MAX_VALUE - UART_MIN_VALUE) / CONTROLLER_MAX_VALUE
    speed = UART_MAX_VALUE - abs(speed) * CONV_RATE
    return int(speed)
    
# 通信Protocol: 0xFF,R,R_D,L,L_D\r\n
# R: 右モーターの速度 500 ~ 5000
# R_D: 右モーターの方向 0 ~ 1 (0: 正転, 1: 逆転)
# L: 左モーターの速度 500 ~ 5000
# L_D: 左モーターの方向 0 ~ 1 (0: 正転, 1: 逆転)
# 5001を送ると停止する
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
    # send_data_dict = {
    #     "rspeed": 3000,
    #     "lspeed": 3000,
    #     "rIsForward": True,
    #     "lIsForward": True
    # }
    send_data_str = json.dumps(send_data_dict)
    port.write(f'{send_data_str}\n\r'.encode())
    

def main():
    try:
        while True:
            for i in range(900,32767):
                # send_data = bytes([i])
                # uart_port.write(send_data)
                send_to_motordriver(uart_port, i,i)
                receive_data = uart_port.readline()
                print(i, receive_data)
                
                time.sleep(TIMEOUT)
    except KeyboardInterrupt:
        uart_port.close()

if __name__ == '__main__':
    main()
