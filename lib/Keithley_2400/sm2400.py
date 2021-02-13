"""
    close con:  close()
    ID:         id()
    Reset:      rst()

    DISPLAY:
        enable/disable Display:     (ON, OFF)
            Set:    set_display(state)  Get:    get_display()
                    display = state             display

    OUTPUT:
        enable/disable output:      (ON, OFF)
            Set:    set_out(state)  Get:    get_out()
                    output = state          output

"""

import serial
import time

TIMEOUT = 1
DEFAULT_BAUDRATE = 9600

ON = 'on'
OFF = 'off'

VOLT = 'volt'
CURR = 'curr'

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
                data = self.serial_con.readline()
                data = str(data, 'utf-8')
                return data.rstrip()
        except:
            raise Exception('Error: Writing and/or reading data')

    '''ID OF DEVICE'''
    def id(self):
        try:
            msg = bytearray('*IDN?\r\n', 'utf-8')
            data = self.send_msg(msg, True)
            return data
        except:
            raise

    '''RESET DEVICE'''
    def rst(self):
        try:
            msg = bytearray('*RST\r\n', 'utf-8')
            self.send_msg(msg, False)
        except:
            raise

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
            raise

    # get state of display
    def get_display(self):
        try:
            msg = bytearray(':DISP:ENAB?\r\n', 'utf-8')                             # get state of display
            data = self.send_msg(msg, True)

            if data == '1':                                                         # if display is on -> return on
                return ON
            elif data == '0':                                                       # if display is off -> return off
                return OFF
        except:
            raise

    '''OUTPUT'''
    # set output
    def set_out(self, state):
        try:
            if self.check_state(state) is False:                                    # check if state is available
                raise Exception('Error: State is unavailable')

            array_state = self.convert_state(state)                                 # convert state to array for msg

            msg = bytearray(':OUTP ' + array_state + '\r\n', 'utf-8')               # set output
            self.send_msg(msg, False)
        except:
            raise

    # get output
    def get_out(self):
        try:
            msg = bytearray(':OUTP?\r\n', 'utf-8')                                  # get output
            data = self.send_msg(msg, True)

            if data == '1':                                                         # if output is on -> return on
                return ON
            elif data == '0':                                                       # if output is off -> return off
                return OFF
        except:
            raise

    # -----------------------------------------------------------------------
    # SOURCE
    # -----------------------------------------------------------------------

    '''SOURCE MODE'''
    # set source mode
    def set_sour_mode(self, mode):
        try:
            if self.check_sour_mode(mode) is False:                             # check if source mode is available
                raise Exception('Error: Mode is unavailable')

            array_mode = self.convert_sour_mode(mode)                           # convert mode to array for msg

            msg = bytearray(':SOUR:FUNC ' + array_mode + '\r\n', 'utf-8')       # set source mode
            self.send_msg(msg, False)
        except:
            raise

    #get source mode
    def get_sour_mode(self):
        try:
            msg = bytearray(':SOUR:FUNC?\r\n', 'utf-8')                         # get source mode
            data = self.send_msg(msg, True)

            if data == 'VOLT':                                                  # if source mode is volt -> return volt
                return VOLT
            elif data == 'CURR':                                                # if source mode is curr -> return curr
                return CURR
        except:
            raise

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

    # check if source mode is available
    def check_sour_mode(self, mode):
        try:
            mode_ok = False
            if mode == VOLT or mode == CURR:
                mode_ok = True
            return mode_ok
        except:
            return False

    '''CONVERT'''
    # convert state to array
    def convert_state(self, state):
        try:
            if state == ON:
                array_state = '1'
            elif state == OFF:
                array_state = '0'
            return array_state
        except:
            raise Exception('Error: Could not convert state')

    # convert source mode to array
    def convert_sour_mode(self, mode):
        try:
            if mode == VOLT:
                array_mode = 'VOLT'
            elif mode == CURR:
                array_mode = 'CURR'
            return array_mode
        except:
            raise Exception('Error: Could not convert source mode')

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

    # output
    def _get_out(self):
        try:
            return self.get_out()
        except:
            raise

    def _set_out(self, state):
        try:
            self.set_out(state)
        except:
            raise

    # source mode
    def _get_sour_mode(self):
        try:
            return self.get_sour_mode()
        except:
            raise

    def _set_sour_mode(self, mode):
        try:
            self.set_sour_mode(mode)
        except:
            raise

    '''PROPERTY'''
    # display
    display = property(_get_display, _set_display)

    # output
    output = property(_get_out, _set_out)

    # source mode
    sour_mode = property(_get_sour_mode, _set_sour_mode)