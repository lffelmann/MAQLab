'''
    close con:  close()
    id:         id()
    reset:      rst()

    VOLTAGE:
        max output:
            Set:    set_max_value(func=FUNC_VOLT, value)
                    volt_max_out = value
            Get:    get_max_value(func=FUNC_VOLT)
                    volt_max_out
        output:
            Set:    set_value(func=FUNC_VOLT, value)
                    volt_out = value
            Get:    get_value(func=FUNC_VOLT)
                    volt_out
        measure:
            meas(func=FUNC_VOLT)
            volt

    CURRENT:
        max output:
            Set:    set_max_value(func=FUNC_CURR, value)
                    curr_max_out = value
            Get:    get_max_value(func=FUNC_CURR)
                    curr_max_out
        output:
            Set:    set_value(func=FUNC_CURR, value)
                    curr_out = value
            Get:    get_value(func=FUNC_CURR)
                    curr_out
        measure:
            meas(func=FUNC_CURR)
            curr

    POWER:
        measure:
            meas(func=FUNC_PWR)
            pwr
'''

import socket

BUFFER = 1024

DEFAULT_PORT = 8462

MAX_VOLT = 70
MAX_CURR = 24

FUNC_VOLT = 'volt'
FUNC_CURR = 'curr'

class SM70AR24:

    # value of max output voltage and current
    value_max_volt = MAX_VOLT
    value_max_curr = MAX_CURR

    '''CONNECTION + INITIAL'''
    # initial SM70AR24, establish connection
    def __init__(self, ip_add, port=DEFAULT_PORT):
        try:
            self.tcp_con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.tcp_con.settimeout(10)
            self.tcp_con.connect((ip_add, port))
        except:
            raise Exception("Error: Could not connect")

    # close connection
    def close(self):
        try:
            self.tcp_con.close()
        except:
            raise Exception('Error: Could not close connection')

    '''SEND GET MSG'''
    def send_msg(self, msg, receive):
        try:
            self.tcp_con.send(msg)
            if receive is True:
                data = self.tcp_con.recv(BUFFER)
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
            self.value_max_volt = MAX_VOLT
            self.value_max_curr = MAX_CURR
        except:
            raise Exception('Error: Could not reset device')

    '''MAX VALUE'''
    # set max output value of voltage and current
    def set_max_out(self, func, value):
        try:
            if self.check_func(func) is False:                               # check if func is available
                raise Exception('Error: Function is unavailable')
            if self.check_value(func, value) is False:                              # check if value is available
                raise Exception('Error: Value is unavailable')

            array_func = self.convert_func(func)                                    # convert func into array for msg
            array_value = self.convert_value(value)                                 # convert value into array for msg

            msg = bytearray('SOUR:' + array_func + ':MAX ' + array_value + '\r\n', 'utf-8')     # set max output value
            self.send_msg(msg, False)

            if func == FUNC_VOLT:                                                   # if func is volt -> value in variable max volt
                self.value_max_volt = value
            elif func == FUNC_CURR:                                                 # if func is curr -> value in variable max curr
                self.value_max_curr = value
        except:
            raise Exception('Error: Could not set max output value')

    # get set max output voltage and current
    def get_max_out(self, func):
        try:
            if self.check_func(func) is False:                               # check if func is available
                raise Exception('Error: Function is unavailable')

            array_func = self.convert_func(func)                                    # convert func into array for msg

            msg = bytearray('SOUR:'+ array_func +':MAX?\r\n', 'utf-8')                # get max output value
            data = self.send_msg(msg, True)

            if func == FUNC_VOLT:                                                   # if func is volt -> data in variable max volt
                self.value_max_volt = data
            elif func == FUNC_CURR:                                                 # if func is curr -> data in variable max curr
                self.value_max_curr = data

            return float(data)
        except:
            raise Exception('Error: Could not get max output value')

    '''SOURCE'''
    # set output voltage and current
    def set_out(self, func, value):
        try:
            if self.check_func(func) is False:                               # check if func is available
                raise Exception('Error: Function is unavailable')
            if self.check_value(func, value) is False:                              # check if value is available
                return 'Error: Value out of range or other error'

            array_func = self.convert_func(func)                                    # convert func into array for msg
            array_value = self.convert_value(value)                                 # convert value into array for msg

            msg = bytearray('SOUR:' + array_func + ' ' + array_value + '\r\n', 'utf-8')     # set output value
            self.send_msg(msg, False)
        except:
            raise Exception('Error: Could not set output value')

    # get set output voltage and current
    def get_out(self, func):
        try:
            if self.check_func(func) is False:                               # check if func is available
                raise Exception('Error: Function is unavailable')

            array_func = self.convert_func(func)                                    # convert func into array for msg

            msg = bytearray('SOUR:' + array_func + '?\r\n', 'utf-8')                # get output value
            data = self.send_msg(msg, True)
            return float(data)
        except:
            raise Exception('Error: Could not get output value')

    '''MEASURE'''
    # measure voltage, current and power
    def meas(self, func):
        try:
            if self.check_func(func) is False:                              # check if func is available
                raise Exception('Error: Function is unavailable')

            array_func = self.convert_func(func)                                    # convert func into array for msg

            msg = bytearray('MEAS:' + array_func + '?\r\n', 'utf-8')                # get measurement
            data = self.send_msg(msg, True)
            return float(data)
        except:
            raise Exception('Error: Could not get measurement')

    # ------------------------------------------------------
    # CHECK + CONVERT
    # ------------------------------------------------------

    '''CHECK'''
    # check if func exist
    def check_func(self, prg, func):
        try:
            func_ok = False
            if func == FUNC_VOLT or func == FUNC_CURR:
                func_ok = True
            return func_ok
        except:
            return False

    # check if value is in range
    def check_value(self, func, value):
        try:
            value = float(value)
            value_ok = False
            if func == FUNC_VOLT and 0 <= value <= self.value_max_volt:
                value_ok = True
            elif func == FUNC_CURR and 0 <= value <= self.value_max_curr:
                value_ok = True
            return value_ok
        except:
            return False

    '''CONVERT'''
    # convert func to array
    def convert_func(self, func):
        try:
            array_func = ''
            if func == FUNC_VOLT:
                array_func = 'VOLT'
            elif func == FUNC_CURR:
                array_func = 'CURR'
            return array_func
        except:
            raise Exception('Error: Could not convert func')

    # convert value to array with 2 decimal
    def convert_value(self, value):
        try:
            value = float(value)
            array_value = '%.2f' % value
            return array_value
        except:
            raise Exception('Error: Could not convert value')

    # -----------------------------------------------------------------------
    # PROPERTY
    # -----------------------------------------------------------------------

    '''PRG FOR PROPERTY'''
    # current
    def _get_max_curr(self):
        try:
            return self.get_max_out(FUNC_CURR)
        except:
            raise

    def _set_max_curr(self, value):
        try:
            self.set_max_out(FUNC_CURR, value)
        except:
            raise

    def _get_curr(self):
        try:
            return self.get_out(FUNC_CURR)
        except:
            raise

    def _set_curr(self, value):
        try:
            self.set_out(FUNC_CURR, value)
        except:
            raise

    def _meas_curr(self):
        try:
            return self.meas(FUNC_CURR)
        except:
            raise

    # voltage
    def _get_max_volt(self):
        try:
            return self.get_max_out(FUNC_VOLT)
        except:
            raise

    def _set_max_volt(self, value):
        try:
            self.set_max_out(FUNC_VOLT, value)
        except:
            raise

    def _get_volt(self):
        try:
            return self.get_out(FUNC_VOLT)
        except:
            raise

    def _set_volt(self, value):
        try:
            self.set_out(FUNC_VOLT, value)
        except:
            raise

    def _meas_volt(self):
        try:
            return self.meas(FUNC_VOLT)
        except:
            raise

    '''PROPERTY'''
    # current
    curr_max_out = property(_get_max_curr, _set_max_curr)
    curr_out     = property(_get_curr, _set_curr)
    curr         = property(_meas_curr)

    # voltage
    volt_max_out = property(_get_max_volt, _set_max_volt)
    volt_out = property(_get_volt, _set_volt)
    volt = property(_meas_volt)