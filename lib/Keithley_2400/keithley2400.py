import serial
import time

DEFAULT_BAUDRATE = 9600


class KEITHLEY2400:

    '''CONNECTION + INITIAL'''
    # initial bk2381e, establish connection
    def __init__(self, port, baudrate=DEFAULT_BAUDRATE):
        try:
            self.serial_con = serial.Serial(port, baudrate, timeout=TIMEOUT)
        except:
            raise Exception('Error: Could not connect')

    # close connection
    def close(self):
        try:
            self.serial_con.close()
        except:
            raise Exception('Error: Could not close connection')