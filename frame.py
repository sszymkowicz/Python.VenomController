from enum import Enum


class Request(Enum):
    PID, Weights, Setup = range(100, 103)


class Received(Enum):
    PID, Weights, Setup = range(200, 203)


class Set(Enum):
    PID, Weights, Setup, Start, Stop = range(300, 305)


class Frame(object):
    def __init__(self, bit0=113, bit1=21, bit2=134, frame_type=0, data_array=None):
        if data_array is None:
            data_array = list()
        self.bit0 = bit0
        self.bit1 = bit1
        self.bit2 = bit2
        self.frame_type = frame_type
        self.data_array = data_array
        self.quantity = len(self.data_array)
        self.crc = self._crc_sum(self.data_array)

    def get_array(self):
        self.data_array = [
            self.bit0,
            self.bit1,
            self.bit2,
            self.quantity,
            self.frame_type,
        ] + self.data_array
        self.data_array.append(self.crc)
        return bytearray(self.data_array)

    @staticmethod
    def _crc_sum(array):
        import crc
        c = crc.Crc8()
        return c.crc(array)
