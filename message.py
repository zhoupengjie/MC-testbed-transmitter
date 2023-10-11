from dataclasses import dataclass

@dataclass
class Message(object):
    def __new__(self, text: str) -> bytes:
        if isinstance(text, str) is False:
            raise ValueError("Input data must be of type {} instead of {}.".format(str, type(text)))
        txt = text.replace('\r\n', '') + '\r\n'
        obj = txt.encode()
        return obj
    
    @classmethod
    def decode(self):
        return self.decode()