from serial import Serial
from message import Message as message
import time


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
        super().__init__(port, baudrate, bytesize, parity, stopbits, timeout, xonxoff, rtscts, write_timeout, dsrdtr, inter_byte_timeout, exclusive)
        
        
    def __del__(self) -> None:
        super().close()
        return super().__del__()
        

    def send(self, msg: str) -> (int | None):
        if isinstance(msg, str) is False:
            self.close()
            raise ValueError("Input data must be of type {} instead of {}.".format(str, type(msg)))
        return self.write(data=message(msg))
        
        
    def receive(self, length: int,time_out: int = 0, decode=True):
        if isinstance(length, int) is False:
            self.close()
            raise ValueError("Input data must be of type {} instead of {}.".format(int, type(length)))
        
        msg = self.readline(length)
        if decode == True:
            msg = msg.decode()
        return msg
        

    def send_lines(self, msgs: list[str], confirm_word: str = None, delay: float = 0.1) -> (int | None):
        if isinstance(msgs, list) is False:
            self.close()
            raise ValueError("Input data must be of type {} instead of {}.".format(str, type(msgs)))
        if isinstance(delay, float) is False:
            self.close()
            raise ValueError("Input data must be of type {} instead of {}.".format(int, type(delay)))
        
        for msg in msgs:
            self.send(msg)
            time.sleep(delay)