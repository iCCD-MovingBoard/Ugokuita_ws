import serial
import time

class DebugDisplay:
    def __init__(self, device_name='/dev/debug_display'):
        self.port = serial.Serial(device_name, '115200', timeout=0.1)
    def write(self, message):
        self.port.write(bytes(f'{message}', encoding='ascii'))
    def close(self):
        self.port.close()

debug = DebugDisplay()

def main():
    for i in range(100):
        message = ''
        for j in range(i):
            message += f'{i}'
        message+='\n'
        debug.write( message )
        print( message , end='')
        time.sleep(0.1)

if __name__ == '__main__':
    main()