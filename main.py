from uart import Uart
from datetime import datetime
import time


def main() -> None:
    try:
        uart = Uart('COM3', 115200)
        
        uart.send('V')
        print('Software version on board: \r\n{}'.format(
            uart.receive(length=128)))
        
        # ack = uart.send_lines(['F100','P1V125', 'P2V125'], wait_ack=True)
        # print(ack)
        
        stream = "10110010"
        bits = [*stream]
        V0 = 125
        VLOW = 0
        VHIGH = 37.5
        toVolt =lambda V0, Vlow, Vhigh, bit: V0+Vhigh if (bool(int(bit)) == True) else V0+Vlow
        for idx, bit in enumerate(bits):
            volt1 = toVolt(V0, VLOW, VHIGH, not bool(int(bit)))
            volt2 = toVolt(V0, VLOW, VHIGH, bit)
            print('Bit {}: {}. Pump1, pump2 voltages are {} and {} [Volt]'.format(idx, bit,volt1, volt2))
            ack1 = uart.send('P1V'+str(volt1), wait_ack=True)
            ack2 = uart.send('P2V'+str(volt2), wait_ack=True)
            print('Pump1 ack: {}\tPump2 ack: {}'.format(ack1, ack2))
            idx += 1
            time.sleep(1)
            
            
    except ValueError as e:
        print("Error:")
        import traceback
        print(traceback.format_exc())
            
            
    finally:
        print('Turn off all pumps....')
        print('Close uart')
        uart.close()


if __name__ == '__main__':
    print("Hello, time: {}".format(datetime.now()))
    main()