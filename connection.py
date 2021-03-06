import serial
import struct
from frame import Frame


class Connect(object):
    def __init__(self):
        self.connection = serial.Serial()

    '''
    bufor = []
    wykryto_start = 0
    bufor_index = 0

    while 1:
        bufor.append(connection.read())

        if wykryto_start == 0 and bufor_index > 1 and bufor[bufor_index] == 170 and bufor[bufor_index-1] == 15 and \
                bufor[bufor_index-2] == 195:
            wykryto_start = 1
            bufor_index = -1

        if wykryto_start == 1 and bufor_index > 0 and bufor_index == bufor[0]+2:
            bufor_index = 0
            wykryto_start = 0
            break
        else:
            bufor_index += 1
    '''

    def send(self, frame_type=0, data_array=None):
        if data_array is None:
            data_array = list()
        f = Frame(frame_type, data_array)
        self.connection.write(f.get_array)
        return struct.unpack("B", self.connection.read())[0]

    def is_open(self):
        return self.connection.isOpen()

    def open(self, port):
        try:
            self.connection = serial.Serial(
                port='\\.\\' + port,
                baudrate=9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS
            )
            print("Connected to {}".format(port))
            return True
        except serial.SerialException:
            print("Could not open port {}".format(port))
            return False

    def close(self):
        self.connection.close()
