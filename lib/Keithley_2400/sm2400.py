"""
    close con:  close()
    ID:         id()
    Reset:      rst()

    DISPLAY:
        enable/disable Display:     (ON, OFF)
            Set:    set_display(state)  Get:    get_display()
                    display = state             display

"""

import serial
import time

TIMEOUT = 1
BUFFER = 1024
DEFAULT_BAUDRATE = 9600

ON = 'on'
OFF = 'off'


class SM2400:

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

    '''SEND GET MSG'''
    def send_msg(self, msg, receive):
        try:
            self.serial_con.reset_input_buffer()
            self.serial_con.reset_output_buffer()

            self.serial_con.write(msg)
            self.serial_con.flush()

            if receive is True:
                data = self.serial_con.read_until('\n', BUFFER)
                data = str(data, 'utf-8')
                return data
        except:
            raise Exception('Error: Writing and/or reading data')

    '''ID OF DEVICE'''
    def id(self):
        try:
            msg = bytearray('*IDN?\r\n', 'utf-8')
            data = self.send_msg(msg, True)
            return data
        except:
            raise Exception('Error: Could not get ID')

    '''RESET DEVICE'''
    def rst(self):
        try:
            msg = bytearray('*RST\r\n', 'utf-8')
            self.send_msg(msg, False)
        except:
            raise Exception('Error: Could not reset device')

    '''DISPLAY'''
    # enable/disable display
    def set_display(self, state):
        try:
            if self.check_state(state) is False:                                    # check if state is available
                raise Exception('Error: State is unavailable')

            array_state = self.convert_state(state)                                 # convert state to array for msg

            msg = bytearray(':DISP:ENAB ' + array_state + '\r\n', 'utf-8')          # set display
            self.send_msg(msg, False)
        except:
            raise Exception('Error: Could not set display')

    # get state of display
    def get_display(self):
        try:
            msg = bytearray(':DISP:ENAB?\r\n', 'utf-8')                             # get state of display
            data = self.send_msg(msg, True)

            if data == 'ON' or data == '1':                                         # if display is on -> return on
                return ON
            elif data == 'OFF' or data == '0':                                      # if display is off -> return off
                return OFF
        except:
            raise Exception('Error: Could not get state of display')

    # -----------------------------------------------------------------------
    # CHECK/CONVERT
    # -----------------------------------------------------------------------

    '''CHECK'''
    # check if selected state is available
    def check_state(self, state):
        try:
            state_ok = False
            if state == ON or state == OFF:
                state_ok = True
            return state_ok
        except:
            return False

    '''CONVERT'''
    # convert state to array
    def convert_state(self, state):
        try:
            if state == ON:
                array_state = 'ON'
            elif state == OFF:
                array_state = 'OFF'
            return array_state
        except:
            raise Exception('Error: Could not convert state')

    # -----------------------------------------------------------------------
    # PROPERTY
    # -----------------------------------------------------------------------

    '''PRG FOR PROPERTY'''
    # display
    def _get_display(self):
        try:
            return self.get_display()
        except:
            raise

    def _set_display(self, state):
        try:
            self.set_display(state)
        except:
            raise

    '''PROPERTY'''
    # display
    display = property(_get_display, _set_display)