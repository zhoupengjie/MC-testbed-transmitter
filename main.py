
from uart import Uart
from datetime import datetime
import time


def main() -> None:
    try:
        uart = Uart('COM2', 115200)
        msg = "Hello, time: {}".format(datetime.now())
        uart.send_lines([msg,'F100','P1V125', 'P2V125'], delay=0.5)
    finally:
        time.sleep(1)
        uart.send('POFF')
        uart.close()


if __name__ == '__main__':
    main()