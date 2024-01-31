
import ros2_ugokuita_ws.src.motor_pkg.motor_pkg.lib.uart as uart
import ros2_ugokuita_ws.src.motor_pkg.motor_pkg.lib.str_converter as str_converter
import time
import ros2_ugokuita_ws.src.controller_pkg.controller_pkg.lib.controller as controller
from logging import getLogger
logger = getLogger(__name__)

def main():
    joycon = controller.Joycon("/dev/input/js0")
    try:
        while True:
            # ここにコントローラーの入力を受け取る処理を書く

            #controller_data = '99, -3444'
            controller_data: str = joycon.get()

            # UARTでデータを送信
            speeds: list[int] = str_converter.to_speeds(controller_data)
            #print(speeds)

            uart.send_to_motordriver(uart.uart_port, speeds['left'])
            receive_data1 = uart.uart_port.readline()

            uart.send_to_motordriver(uart.uart_port2, speeds['right'])
            receive_data2 = uart.uart_port2.readline()
            
            receive_data = ', '.join([str(receive_data1), str(receive_data2)])
            print(receive_data)

            time.sleep(uart.TIMEOUT)
            #break

    except KeyboardInterrupt:
        uart.uart_port.close()
        uart.uart_port2.close()

if __name__ == '__main__':
    main()
