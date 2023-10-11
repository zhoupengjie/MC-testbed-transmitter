from serial import PortNotOpenError, Serial
from message import Message as message
import time
import types

def checkType(data: any, tp: types, callback_func : types.FunctionType = None):
    if isinstance(data, tp) is False:
        if callback_func != None:
            callback_func()
        raise ValueError("Input data must be of type {} instead of {}.".format(tp, type(data)))


class Uart(Serial):
    def __init__(
        self, port: str | None = None, 
        baudrate: int = 115200, 
        bytesize: int = 8, 
        parity: str = "N", 
        stopbits: float = 1, 
        timeout: float | None = None, 
        xonxoff: bool = False, rtscts: bool = False, 
        write_timeout: float | None = None, 
        dsrdtr: bool = False, 
        inter_byte_timeout: float | None = None, 
        exclusive: float | None = None
        ) -> None:
        super().__init__(
            port, baudrate, bytesize, parity, stopbits, timeout, xonxoff, rtscts, write_timeout, dsrdtr, inter_byte_timeout, exclusive)
        print('Uart connection at {} is established.'.format(port))
        
        
    def __del__(self) -> None:
        super().close()
        return super().__del__()
    
    
    def close(self) -> None:
        try:
            self.send('POFF')
        except PortNotOpenError:
            pass
        finally:
            super().close()
        

    def send(self, msg: str, wait_ack: bool =False, rx_length:int = 128) -> (int | str| None):
        checkType(msg, str, self.close)
        res = self.write(message(msg))
        if wait_ack:
            res = self.receive(rx_length)
        return res
        
        
    def receive(self, length: int, time_out: int = 0, decode=True):
        checkType(length, int, self.close)
        msg = self.readline(length)
        if decode == True:
            msg = msg.decode().replace('\r\n', '')
        return msg
        

    def send_lines(self, msgs: list[str], wait_ack: bool = False, rx_length: int = 128) -> (int| list[str] | None):
        checkType(msgs, list, self.close)
        acks = [None] * len(msgs)
        for idx,msg in enumerate(msgs):
            ack = self.send(msg, wait_ack, rx_length)
            acks[idx] = ack
            idx += 1
        return acks        
    