"""
    close con:  close()
    ID:         id()
    Reset:      rst()

    DISPLAY:    (ON, OFF)
        Set:    set_display(state)  Get:    get_display()
                display = state             display

    OUTPUT:     (ON, OFF)
        Set:    set_ena_out(state)  Get:    get_ena_out()
                output = state              output

    SOURCE MODE:    (VOLT, CURR)
        Set:    set_sour_mode(func) Get:    get_sour_mode()
                sour_mode = func            sour_mode

    VOLTAGE:
        max output:     (-210 to 210)
            Set:    set_max_out(FUNC_VOLT, value)
                    volt_max_out = value
            Get:    get_max_out(FUNC_VOLT, value)
                    volt_max_out
        output:         (-210 to 210)
            Set:    set_out(FUNC_VOLT, value)
                    volt_out = value
            Get:    get_out(FUNC_VOLT)
                    volt_out
        Measurement range:  (-210 to 210)
            Set:    set_range(FUNC_VOLT, range)
                    volt_range = range
            Get:    get_range(FUNC_VOLT)
                    volt_range

    CURRENT:
        max output:     (-1.05 to 1.05)
            Set:    set_max_out(FUNC_CURR, value)
                    curr_max_out = value
            Get:    get_max_out(FUNC_CURR, value)
                    curr_max_out
        output:         (-1.05 to 1.05)
            Set:    set_out(FUNC_CURR, value)
                    curr_out = value
            Get:    get_out(FUNC_CURR)
                    curr_out
        Measurement range:  (-1.05 to 1.05)
            Set:    set_range(FUNC_CURR, range)
                    curr_range = range
            Get:    get_range(FUNC_CURR)
                    curr_range

    RESISTANCE:
        Measurement range:  (0 to 2.1e8)
            Set:    set_range(FUNC_RES, range)
                    res_range = range
            Get:    get_range(FUNC_RES)
                    res_range

"""

import serial
import time

TIMEOUT = 1
DEFAULT_BAUDRATE = 9600
TIME_SLEEP = 1

ON = 'on'
OFF = 'off'
AUTO = 'auto'

FUNC_VOLT = 'volt'
FUNC_CURR = 'curr'
FUNC_RES = 'res'

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
    # set enable/disable output
    def set_ena_out(self, state):
        try:
            if self.check_state(state) is False:                                    # check if state is available
                raise Exception('Error: State is unavailable')

            array_state = self.convert_state(state)                                 # convert state to array for msg

            msg = bytearray(':OUTP ' + array_state + '\r\n', 'utf-8')               # set output
            self.send_msg(msg, False)
        except:
            raise

    # get enable/disable output
    def get_ena_out(self):
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
    def set_sour_mode(self, func):
        try:
            if self.check_func('source', func) is False:                        # check if func is available
                raise Exception('Error: Func is unavailable')

            array_func = self.convert_func('std', func)                                # convert func to array for msg

            msg = bytearray(':SOUR:FUNC ' + array_func + '\r\n', 'utf-8')       # set source mode
            self.send_msg(msg, False)
        except:
            raise

    #get source mode
    def get_sour_mode(self):
        try:
            msg = bytearray(':SOUR:FUNC?\r\n', 'utf-8')                         # get source mode
            data = self.send_msg(msg, True)

            if data == 'VOLT':                                                  # if source mode is volt -> return volt
                return FUNC_VOLT
            elif data == 'CURR':                                                # if source mode is curr -> return curr
                return FUNC_CURR
        except:
            raise

    '''MAX OUTPUT VALUE'''
    # set max output value
    def set_max_out(self, func, value):
        try:
            if self.check_func('source', func) is False:                                  # check if func is available
                raise Exception('Error: Func is unavailable')
            if self.check_value('max_out', func, value) is False:               # check if value is available
                raise Exception('Error: Value is not available')

            array_func = self.convert_func('std', func)                                # convert func to array for msg
            array_value = self.convert_value('max_out', value)                  # convert value to array for msg
            
            msg = bytearray(':SENS:' + array_func + ':PROT ' + array_value + '\r\n', 'utf-8')    # set max out
            self.send_msg(msg, False)
        except:
            raise

    # get max output value
    def get_max_out(self, func):
        try:
            if self.check_func('source', func) is False:                                  # check if func is available
                raise Exception('Error: Func is unavailable')

            array_func = self.convert_func('std', func)                                # convert func to array for msg

            msg = bytearray(':SENS:' + array_func + ':PROT?\r\n', 'utf-8')      # get max out
            data = self.send_msg(msg, True)
            data = float(data)
            return data
        except:
            raise

    '''OUTPUT VALUE'''
    # set output value
    def set_out(self, func, value):
        try:
            if self.check_func('source', func) is False:                                  # check if func is available
                raise Exception('Error: Func is unavailable')
            if self.check_value('out', func, value) is False:                   # check if value is available
                raise Exception('Error: Value is not available')

            array_func = self.convert_func('std', func)                                # convert func to array for msg
            array_value = self.convert_value('out', value)                      # convert value to array for msg

            msg = bytearray(':SOUR:' + array_func + ':RANG:AUTO 1\r\n', 'utf-8')    # set source range to auto
            self.send_msg(msg, False)

            time.sleep(TIME_SLEEP)

            msg = bytearray(':SOUR:' + array_func + ' ' + array_value + '\r\n', 'utf-8')    # set output value
            self.send_msg(msg, False)
        except:
            raise

    # get output value
    def get_out(self, func):
        try:
            if self.check_func('source', func) is False:                        # check if func is available
                raise Exception('Error: Func is unavailable')

            array_func = self.convert_func('std', func)                                # convert func to array for msg

            msg = bytearray(':SOUR:' + array_func + '?\r\n', 'utf-8')           # get output value
            data = self.send_msg(msg, True)
            data = float(data)
            return data
        except:
            raise

    # -----------------------------------------------------------------------
    # MEASURE
    # -----------------------------------------------------------------------

    '''MEASUREMENT FUNCTION'''
    # set measurement function
    def set_meas_func(self, func1=None, func2=None, func3=None):
        try:
            if func1 is not None:
                if self.check_func('meas', func1) is False:                     # check if func1 is available
                    raise Exception('Error: Func1 is unavailable')
            if func2 is not None:
                if self.check_func('meas', func2) is False:                     # check if func2 is available
                    raise Exception('Error: Func2 is unavailable')
            if func3 is not None:
                if self.check_func('meas', func3) is False:                     # check if func3 is available
                    raise Exception('Error: Func3 is unavailable')

            array_func1 = self.convert_func('meas_func', func1)                 # convert func1 to array for msg
            array_func2 = self.convert_func('meas_func', func2)                 # convert func2 to array for msg
            array_func3 = self.convert_func('meas_func', func3)                 # convert func3 to array for msg

            msg = bytearray(':FUNC:CONC 1\r\n', 'utf-8')                        # enabled multi measurement
            self.send_msg(msg, False)
            time.sleep(TIME_SLEEP)

            msg = bytearray(':FUNC:OFF:ALL\r\n', 'utf-8')                       # disable all measurement functions
            self.send_msg(msg, False)
            time.sleep(TIME_SLEEP)

            msg = bytearray(':FUNC ' + array_func1 + array_func2 + array_func3 + '\r\n', 'utf-8')  # set measurement func
            self.send_msg(msg, False)

            if func1 == FUNC_RES or func2 == FUNC_RES or func3 == FUNC_RES:     # if meas func is res -> set mode to manual
                time.sleep(TIME_SLEEP)
                msg = bytearray(':RES:MODE AUTO\r\n', 'utf-8')
                self.send_msg(msg, False)
        except:
            raise

    # get measurement function
    def get_meas_func(self):
        try:
            list_func = []                                                      # list to save meas func

            list_tryout = ['"VOLT"', '"CURR"', '"RES"']
            list_set = [FUNC_VOLT, FUNC_CURR, FUNC_RES]

            for i in range(0, len(list_tryout)):
                msg = bytearray(':FUNC:STAT? ' + list_tryout[i] + '\r\n', 'utf-8')  # get if meas func is volt
                data = self.send_msg(msg, True)
                if data == '1':
                    list_func.append(list_set[i])

            return list_func
        except:
            raise

    '''RANGE'''
    # set measurement range
    def set_range(self, func, range):
        try:
            if self.check_func('meas', func) is False:                          # check if func is available
                raise Exception('Error: Func is unavailable')
            if self.check_value('range', func, range) is False:                 # check if range is available
                raise Exception('Error: Range is not available')

            array_func = self.convert_func('std', func)                         # convert func to array for msg

            if range == AUTO:
                msg = bytearray(':' + array_func + ':RANG:AUTO 1\r\n', 'utf-8') # if range is auto -> set range on auto
                self.send_msg(msg, False)
            else:
                msg = bytearray(':' + array_func + ':RANG:AUTO 0\r\n', 'utf-8') # if range is not auto -> disable
                self.send_msg(msg, False)
                time.sleep(TIME_SLEEP)
                array_range = self.convert_value('range', range)                # convert range to array for msg
                msg = bytearray(':' + array_func + ':RANG ' + array_range + '\r\n', 'utf-8')    # set range
                self.send_msg(msg, False)
        except:
            raise

    # get measurement range
    def get_range(self, func):
        try:
            if self.check_func('meas', func) is False:                          # check if func is available
                raise Exception('Error: Func is unavailable')

            array_func = self.convert_func('std', func)                         # convert func to array for msg

            msg = bytearray(':' + array_func + ':RANG:AUTO?\r\n', 'utf-8')      # get if range is auto
            data = self.send_msg(msg, True)

            if data == '1':                                                     # if range is auto -> return auto
                return AUTO
            elif data == '0':
                msg = bytearray(':' + array_func + ':RANG?\r\n', 'utf-8')       # get range
                data = self.send_msg(msg, True)
                data = float(data)
                return data
        except:
            raise

    '''MEASURE'''
    def meas(self, func):
        try:
            if self.check_func('meas', func) is False:                          # check if func is available
                raise Exception('Error: Func is unavailable')

            array_func = self.convert_func('std', func)                         # convert func to array for msg

            msg = bytearray(':MEAS:' + array_func + '?\r\n', 'utf-8')           # get measurement
            data = self.send_msg(msg, True)
            data = float(data)
            return data
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

    # check if func is available
    def check_func(self, prg, func):
        try:
            func_ok = False
            if prg == 'source':
                if func == FUNC_VOLT or func == FUNC_CURR:
                    func_ok = True
            elif prg == 'meas':
                if func == FUNC_VOLT or func == FUNC_CURR or func == FUNC_RES:
                    func_ok = True
            return func_ok
        except:
            return False

    # deck if value for max out is available
    def check_value(self, prg, func, value):
        try:
            value_ok = False
            if prg == 'max_out' or prg == 'out':
                value = float(value)
                if func == FUNC_VOLT:
                    if -210 <= value <= 210:
                        value_ok = True
                elif func == FUNC_CURR:
                    if -1.05 <= value <= 1.05:
                        value_ok = True
            elif prg == 'range':
                if value == AUTO:
                    value_ok = True
                else:
                    value = float(value)
                    if func == FUNC_VOLT:
                        if -210 <= value <= 210:
                            value_ok = True
                    elif func == FUNC_CURR:
                        if -1.05 <= value <= 1.05:
                            value_ok = True
                    elif func == FUNC_RES:
                        if 0 <= value <= 2.1e8:
                            value_ok = True
            return value_ok
        except:
            return False

    '''CONVERT'''
    # convert state to array
    def convert_state(self, state):
        try:
            array_state = ''
            if state == ON:
                array_state = '1'
            elif state == OFF:
                array_state = '0'
            return array_state
        except:
            raise Exception('Error: Could not convert state')

    # convert func to array
    def convert_func(self, prg, func):
        try:
            array_func = ''
            if prg == 'std':
                if func == FUNC_VOLT:
                    array_func = 'VOLT'
                elif func == FUNC_CURR:
                    array_func = 'CURR'
                elif func == FUNC_RES:
                    array_func = 'RES'
            elif prg == 'meas_func':
                if func == FUNC_VOLT:
                    array_func = '"VOLT",'
                elif func == FUNC_CURR:
                    array_func = '"CURR",'
                elif func == FUNC_RES:
                    array_func = '"RES",'
            return array_func
        except:
            raise Exception('Error: Could not convert func')

    # convert value to array
    def convert_value(self, prg, value):
        try:
            array_value = ''
            if prg == 'max_out' or prg == 'out' or prg == 'range':
                array_value = str(value)
            return array_value
        except:
            raise Exception('Error: Could not convert value')


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
    def _get_ena_out(self):
        try:
            return self.get_ena_out()
        except:
            raise

    def _set_ena_out(self, state):
        try:
            self.set_ena_out(state)
        except:
            raise

    # source mode
    def _get_sour_mode(self):
        try:
            return self.get_sour_mode()
        except:
            raise

    def _set_sour_mode(self, func):
        try:
            self.set_sour_mode(func)
        except:
            raise

    # voltage max output value
    def _get_max_out_volt(self):
        try:
            return self.get_max_out(FUNC_VOLT)
        except:
            raise

    def _set_max_out_volt(self, value):
        try:
            self.set_max_out(FUNC_VOLT, value)
        except:
            raise

    # current max output value
    def _get_max_out_curr(self):
        try:
            return self.get_max_out(FUNC_CURR)
        except:
            raise

    def _set_max_out_curr(self, value):
        try:
            self.set_max_out(FUNC_CURR, value)
        except:
            raise

    # voltage output value
    def _get_out_volt(self):
        try:
            return self.get_out(FUNC_VOLT)
        except:
            raise

    def _set_out_volt(self, value):
        try:
            self.set_out(FUNC_VOLT, value)
        except:
            raise

    # current output value
    def _get_out_curr(self):
        try:
            return self.get_out(FUNC_CURR)
        except:
            raise

    def _set_out_curr(self, value):
        try:
            self.set_out(FUNC_CURR, value)
        except:
            raise

    # voltage range
    def _get_range_volt(self):
        try:
            return self.get_range(FUNC_VOLT)
        except:
            raise

    def _set_range_volt(self, range):
        try:
            self.set_range(FUNC_VOLT, range)
        except:
            raise

    # current range
    def _get_range_curr(self):
        try:
            return self.get_range(FUNC_CURR)
        except:
            raise

    def _set_range_curr(self, range):
        try:
            self.set_range(FUNC_CURR, range)
        except:
            raise

    # resistance range
    def _get_range_res(self):
        try:
            return self.get_range(FUNC_RES)
        except:
            raise

    def _set_range_res(self, range):
        try:
            self.set_range(FUNC_RES, range)
        except:
                raise

    '''PROPERTY'''
    # display
    display = property(_get_display, _set_display)

    # output
    output = property(_get_ena_out, _set_ena_out)

    # source mode
    sour_mode = property(_get_sour_mode, _set_sour_mode)

    # voltage
    volt_max_out = property(_get_max_out_volt, _set_max_out_volt)
    volt_out = property(_get_out_volt, _set_out_volt)
    volt_range = property(_get_range_volt, _set_range_volt)

    # current
    curr_max_out = property(_get_max_out_curr, _set_max_out_curr)
    curr_out = property(_get_out_curr, _set_out_curr)
    curr_range = property(_get_range_curr, _set_range_curr)

    # resistance
    res_range = property(_get_range_res, _set_range_res)