"""
    close con:  close()
    ID:         id()
    Reset:      rst()

    DISPLAY:
        enable/disable Display:     (ON, OFF)
            Set:    set_display(state)  Get:    get_display()
                    display = state             display

    TRIGGER:
        select Trigger:     (IMM, BUS, MAN)
            Set:    set_trg(trg)        Get:    get_trg()
                    sel_trg = trg               sel_trg
        trigger measurement:
            trg()

    VOLTAGE AC:
        measure:
            meas(func=FUNC_VOLT_AC)
            volt_ac
        range:      (0.2, 2, 20, 200, 750, DEF, MIN, MAX, AUTO)
            Set:    set_range(func=FUNC_VOLT_AC, range)
                    volt_ac_range = range
            Get:    get_range(func=FUNC_VOLT_AC)
                    volt_ac_range
        reference:  (-757.5 to 757.5, DEF, MIN, MAX, OFF, ACQ)
            Set:    set_ref(func=FUNC_VOLT_AC, ref)
                    volt_ac_ref = ref
            Get:    get_ref(func=FUNC_VOLT_AC)
                    volt_ac_ref
        measurement speed:  (FAST, MED, SLOW, MAX, DEF, MIN)
            Set:    set_meas_speed(func=FUNC_VOLT_AC, speed)
                    volt_ac_speed = speed
            Get:    get_meas_speed(func=FUNC_VOLT_AC)
                    volt_ac_speed

    VOLTAGE DC:
        measure:
            meas(func=FUNC_VOLT_DC)
            volt_dc
        range:      (0.2, 2, 20, 200, 1000, DEF, MIN, MAX, AUTO)
            Set:    set_range(func=FUNC_VOLT_DC, range)
                    volt_dc_range = range
            Get:    get_range(func=FUNC_VOLT_DC)
                    volt_dc_range
        reference:  (-1010 to 1010, DEF, MIN, MAX, OFF, ACQ)
            Set:    set_ref(func=FUNC_VOLT_DC, ref)
                    volt_dc_ref = ref
            Get:    get_ref(func=FUNC_VOLT_DC)
                    volt_dc_ref
        measurement speed:  (FAST, MED, SLOW, MAX, DEF, MIN)
            Set:    set_meas_speed(func=FUNC_VOLT_DC, speed)
                    volt_dc_speed = speed
            Get:    get_meas_speed(func=FUNC_VOLT_DC)
                    volt_dc_speed

    CURRENT AC:
        measure:
            meas(func=FUNC_CURR_AC)
            curr_ac
        range:      (0 to 20, DEF, MIN, MAX, AUTO)
            Set:    set_range(func=FUNC_CURR_AC, range)
                    curr_ac_range = range
            Get:    get_range(func=FUNC_CURR_AC)
                    curr_ac_range
        reference:  (-20 to 20, DEF, MIN, MAX, OFF, ACQ)
            Set:    set_ref(func=FUNC_CURR_AC, ref)
                    curr_ac_ref = ref
            Get:    get_ref(func=FUNC_CURR_AC)
                    curr_ac_ref
        measurement speed:  (FAST, MED, SLOW, MAX, DEF, MIN)
            Set:    set_meas_speed(func=FUNC_CURR_AC, speed)
                    curr_ac_speed = speed
            Get:    get_meas_speed(func=FUNC_CURR_AC)
                    curr_ac_speed

    CURRENT DC:
        measure:
            meas(func=FUNC_CURR_DC)
            curr_dc
        range:      (-20 to 20, DEF, MIN, MAX, AUTO)
            Set:    set_range(func=FUNC_CURR_DC, range)
                    curr_dc_range = range
            Get:    get_range(func=FUNC_CURR_DC)
                    curr_dc_range
        reference:  (0 to 20, DEF, MIN, MAX, OFF, ACQ)
            Set:    set_ref(func=FUNC_CURR_DC, ref)
                    curr_dc_ref = ref
            Get:    get_ref(func=FUNC_CURR_DC)
                    curr_dc_ref
        measurement speed:  (FAST, MED, SLOW, MAX, DEF, MIN)
            Set:    set_meas_speed(func=FUNC_CURR_DC, speed)
                    curr_dc_speed = speed
            Get:    get_meas_speed(func=FUNC_CURR_DC)
                    curr_dc_speed

    RESISTANCE:
        measure:
            meas(func=FUNC_RES)
            res
        range:      (0 to 20e6, DEF, MIN, MAX, AUTO)
            Set:    set_range(func=FUNC_RES, range)
                    res_range = range
            Get:    get_range(func=FUNC_RES)
                    res_range
        reference:  (0 to 20e6, DEF, MIN, MAX, OFF, ACQ)
            Set:    set_ref(func=FUNC_RES, ref)
                    res_ref = ref
            Get:    get_ref(func=FUNC_RES)
                    res_ref
        measurement speed:  (FAST, MED, SLOW, MAX, DEF, MIN)
            Set:    set_meas_speed(func=FUNC_RES, speed)
                    res_speed = speed
            Get:    get_meas_speed(func=FUNC_RES)
                    res_speed

    FREQUENCY:
        measure:
            meas(func=FUNC_FREQ)
            freq
        threshold voltage range:    (0 to 1010)
            Set:    set_range(func=FUNC_FREQ, range)
                    freq_range = range
            Get:    get_range(func=FUNC_FREQ)
                    freq_range
        reference:  (0 to 1.0e6, DEF, MIN, MAX, OFF, ACQ)
            Set:    set_ref(func=FUNC_FREQ, ref)
                    freq_ref = ref
            Get:    get_ref(func=FUNC_FREQ)
                    freq_ref

    PERIOD:
        measure:
            meas(func=FUNC_PER)
            per
        threshold voltage range:    (0 to 1010)
            Set:    set_range(func=FUNC_PER, range)
                    per_range = range
            Get:    get_range(func=FUNC_PER)
                    per_range
        reference:  (0 to 1, DEF, MIN, MAX, OFF, ACQ)
            Set:    set_ref(func=FUNC_PER, ref)
                    per_ref = ref
            Get:    get_ref(func=FUNC_PER)
                    per_ref

    DIODE:
        measure:
            meas(func=FUNC_DIOD)
            diod

    CONTINUITY:
        measure:
            meas(func=FUNC_CONT)
            cont
"""

import serial
import time

TIMEOUT = 1
DEFAULT_BAUDRATE = 9600
BUFFER = 1024

FUNC_VOLT_AC = 'voltac'     # array to select VOLTage:AC
FUNC_VOLT_DC = 'voltdc'     # array to select VOLTage:DC
FUNC_CURR_AC = 'currac'     # array to select CURRent:AC
FUNC_CURR_DC = 'currdc'     # array to select CURRent:DC
FUNC_RES     = 'res'        # array to select RESistance
FUNC_FREQ    = 'freq'       # array to select FREQuency
FUNC_PER     = 'per'        # array to select PERiod
FUNC_DIOD    = 'diod'       # array to select DIODe
FUNC_CONT    = 'cont'       # array to select CONTinuity


AUTO = 'auto'       # array to select auto in range
MAX  = 'max'        # array to select max in range/ref/meas speed
MIN  = 'min'        # array to select min in range/ref/meas speed
DEF  = 'def'        # array to select default in range/ref/meas speed
OFF  = 'off'        # array to select off in reference/display
ACQ  = 'acq'        # array to select acquire in reference

ON   = 'on'         # array to select on in display

IMM = 'imm'     # array to select internal trigger
BUS = 'bus'     # array to trigger via Serial interface
MAN = 'man'     # array to select 'Trig' button to trigger

FAST = 'fast'   # array for measurement speed fast
MED  = 'med'    # array for measurement speed medium
SLOW = 'slow'   # array for measurement speed slow

class BK2831E:

    trg_selected = None          # save selected trigger

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
            self.trg_selected = IMM
        except:
            raise Exception('Error: Could not reset device')

    '''TRIGGER MEASUREMENT'''
    def trg(self):
        try:
            if self.trg_selected != BUS:
                raise Exception('Error: Wrong trigger selected')
            msg = bytearray('*TRG\r\n', 'utf-8')
            self.send_msg(msg, False)
        except:
            raise Exception('Error: Could not trigger measurement')

    '''SELECT TRIGGER'''
    # set selected trigger
    def set_trg(self, trg):
        try:
            if self.check_trg(trg) is False:                                  # check if trg is available
                raise Exception('Error: Trigger is unavailable')

            array_trg = self.convert_trg(trg)                                 # convert trg to array for msg

            msg = bytearray(':TRIG:SOUR ' + array_trg + '\r\n', 'utf-8')      # set trigger
            self.send_msg(msg, False)
            self.trg_selected = trg
        except:
            raise Exception('Error: Could not select trigger')

    # get selected trigger
    def get_trg(self):
        try:
            msg = bytearray(':TRIG:SOUR?\r\n', 'utf-8')                       # get selected trigger
            data = self.send_msg(msg, True)

            if data == 'IMMediate':                                           # if trigger is immediate -> return immediate
                return IMM
            elif data == 'BUS':                                               # if trigger is bus -> return bus
                return BUS
            elif data == 'MANual':                                            # if trigger is manual -> return manual
                return MAN

        except:
            raise Exception('Error: Could not get selected trigger')

    '''DISPLAY'''
    # enable/disable display
    def set_display(self, state):
        try:
            if self.check_state(state) is False:                              # check if state is available
                raise Exception('Error: State is unavailable')

            array_state = self.convert_state(state)                           # convert state to array for msg

            msg = bytearray(':DISP:ENAB ' + array_state + '\r\n', 'utf-8')    # set display
            self.send_msg(msg, False)
        except:
            raise Exception('Error: Could not set display')

    # get state of display
    def get_display(self):
        try:
            msg = bytearray(':DISP:ENAB?\r\n', 'utf-8')                       # get state of display
            data = self.send_msg(msg, True)

            if data == 'ON' or data == '1':                                   # if display is on -> return on
                return ON
            elif data == 'OFF' or data == '0':                                # if display is off -> return off
                return OFF
        except:
            raise Exception('Error: Could not get state of display')

    '''MEASUREMENT SPEED'''
    # set measurement speed
    def set_meas_speed(self, func, speed):
        try:
            if self.check_func('speed', func) is False:                       # check if func is available
                raise Exception('Error: Function is unavailable')
            if self.check_speed(speed) is False:                              # check if speed is available
                raise Exception('Error: Speed is unavailable')

            array_func = self.convert_func('speed', func)                     # convert func to array for msg

            array_speed = self.convert_speed(speed)                           # convert speed to array for msg

            msg = bytearray(array_func + ':NPLC ' + array_speed + '\r\n', 'utf-8')  # set measurement speed
            self.send_msg(msg, False)
        except:
            raise Exception('Error: Could not set measurement speed')

    # get measurement speed
    def get_meas_speed(self, func):
        try:
            if self.check_func('speed', func) is False:                       # check if func is available
                raise Exception('Error: Function is unavailable')

            array_func = self.convert_func('speed', func)                     # convert func to array for msg

            msg = bytearray(array_func + ':NPLC?\r\n', 'utf-8')               # get measurement speed
            data = self.send_msg(msg, True)

            if data == '0.1':                                                 # if meas speed is fast -> return fast
                return FAST
            elif data == '1':                                                 # if meas speed is med -> return med
                return MED
            elif data == '10':                                                # if meas speed is slow -> return slow
                return SLOW
        except:
            raise Exception('Error: Could not get measurement speed')

    '''RANGE'''
    # set range
    def set_range(self, func, range):
        try:
            if self.check_func('range', func) is False:                       # check if func is available
                raise Exception('Error: Function is unavailable')
            if self.check_range(func, range) is False:                        # check if range is available
                raise Exception('Error: Range is unavailable')

            array_func = self.convert_func('range', func)                     # convert func to array for msg

            if range == AUTO:                                                 # if range is auto -> enable auto
                msg = bytearray(array_func + ':RANG:AUTO ON\r\n', 'utf-8')
                self.send_msg(msg, False)
            elif func != FUNC_FREQ and func != FUNC_PER:                      # if range can be set on auto -> disable range auto
                msg = bytearray(array_func + ':RANG:AUTO OFF\r\n', 'utf-8')
                self.send_msg(msg, False)
                time.sleep(1)

            if range != AUTO:                                                 # if range is not auto -> set range
                array_range = self.convert_range_ref(range)                   # convert range to array for msg
                msg = bytearray(array_func + ':RANG ' + array_range + '\r\n', 'utf-8')
                self.send_msg(msg, False)
        except:
            raise Exception('Error: Could not set range')

    # get range
    def get_range(self, func):
        try:
            if self.check_func('range', func) is False:                       # check if func is available
                raise Exception('Error: Function is unavailable')

            array_func = self.convert_func('range', func)                     # convert func to array for msg

            if func != FUNC_FREQ and func != FUNC_PER:                        # if range can be set on auto -> check if range is auto
                msg = bytearray(array_func + ':RANG:AUTO?\r\n', 'utf-8')
                data = self.send_msg(msg, True)

            if data == 'ON':                                                  # if range is auto -> return range is auto
                return AUTO
            elif data == 'OFF' or func == FUNC_FREQ or func == FUNC_PER:      # if range is not auto or range cant be set on auto -> get range and return range
                msg = bytearray(array_func + ':RANG?\r\n', 'utf-8')
                data = self.send_msg(msg, True)
                return float(data)
        except:
            raise Exception('Error: Could not get range')

    '''REFERENCE'''
    # set reference
    def set_ref(self, func, ref):
        try:
            if self.check_func('ref', func) is False:                         # check if func is available
                raise Exception('Error: Function is unavailable')
            if self.check_ref(func, ref) is False:                            # check if ref is available
                raise Exception('Error: Reference is unavailable')

            array_func = self.convert_func('ref', func)                       # convert func to array for msg

            if ref == OFF:                                                    # if ref is OFF -> turn ref OFF
                msg = bytearray(array_func + ':REF:STAT OFF\r\n', 'utf-8')
                self.send_msg(msg, False)
            else:                                                             # if ref is not OFF -> turn ref ON
                msg = bytearray(array_func + ':REF:STAT ON\r\n', 'utf-8')
                self.send_msg(msg, False)
                time.sleep(1)
                if ref == ACQ:                                                # if ref is ACQ -> set ref ACQ
                    msg = bytearray(array_func + ':REF:ACQ\r\n', 'utf-8')
                    self.send_msg(msg, False)
                else:                                                         # if ref is ON and not ACQ -> set ref
                    array_ref = self.convert_range_ref(ref)                   # convert ref to array for msg
                    msg = bytearray(array_func + ':REF ' + array_ref + '\r\n', 'utf-8')
                    self.send_msg(msg, False)

        except:
            raise Exception('Error: Could not set reference')

    # get reference
    def get_ref(self, func):
        try:
            if self.check_func('ref', func) is False:                         # check if func is available
                raise Exception('Error: Function is unavailable')

            array_func = self.convert_func('ref', func)                       # convert func to array for msg

            msg = bytearray(array_func + ':REF:STAT?\r\n', 'utf-8')           # ask if reference is ON
            data = self.send_msg(msg, True)

            if data == 'OFF':                                                 # if reference is OFF -> return reference is OFF
                return OFF
            elif data == 'ON':                                                # if reference is ON -> get reference and return reference
                msg = bytearray(array_func + ':REF?\r\n', 'utf-8')
                data = self.send_msg(msg, True)
                return float(data)
        except:
            raise Exception('Error: Could not get reference')

    '''GET MEASUREMENT'''
    def meas(self, func):
        try:
            if self.check_func('meas', func) is False:                        # check if func is available
                raise Exception('Error: Function is unavailable')

            array_func = self.convert_func('meas', func)                      # convert func to array for msg

            msg = bytearray(':FUNC ' + array_func + '\r\n', 'utf-8')          # set measurement to certain func
            self.send_msg(msg, False)
            time.sleep(1)

            msg = bytearray('FETC?\r\n', 'utf-8')                             # get measurement and return measurement
            data = self.send_msg(msg, True)
            return float(data)
        except:
            raise Exception('Error: Could not get measurement')

    # -----------------------------------------------------------------------
    # CHECK/CONVERT
    # -----------------------------------------------------------------------

    '''CHECK'''
    # check if selected func is available
    def check_func(self, prg, func):
        try:
            func_ok = False
            if prg == 'range' or prg == 'ref' or prg == 'meas' or prg == 'speed':
                if func == FUNC_VOLT_AC or func == FUNC_VOLT_DC or func == FUNC_CURR_AC or func == FUNC_CURR_DC or func == FUNC_RES:
                    func_ok = True
            if prg == 'range' or prg == 'ref' or prg == 'meas':
                if func == FUNC_FREQ or func == FUNC_PER:
                    func_ok = True
            if prg == 'meas':
                if func == FUNC_DIOD or func == FUNC_CONT:
                    func_ok = True
            return func_ok
        except:
            return False

    # check if selected range is available
    def check_range(self, func, range_check):
        try:
            range_ok = False
            list_range_volt_ac = [0.2, 2, 20, 200, 750]
            list_range_volt_dc = [0.2, 2, 20, 200, 1000]

            if func == FUNC_FREQ or func == FUNC_PER:
                range_check = float(range_check)
                if 0 <= range_check <= 1010:
                    range_ok = True
            else:
                if range_check == AUTO or range_check== MAX or range_check == MIN or range_check == DEF:
                    range_ok = True
                else:
                    range_check = float(range_check)
                    if func == FUNC_VOLT_AC:
                        for i in range(0, len(list_range_volt_ac)):
                            if range_check == list_range_volt_ac[i]:
                                range_ok = True
                                break
                    elif func == FUNC_VOLT_DC:
                        for i in range(0, len(list_range_volt_dc)):
                            if range_check == list_range_volt_dc[i]:
                                range_ok = True
                                break
                    elif func == FUNC_CURR_AC:
                        if 0 <= range_check <= 20:
                            range_ok = True
                    elif func == FUNC_CURR_DC:
                        if -20 <= range_check <= 20:
                            range_ok = True
                    elif func == FUNC_RES:
                        if 0 <= range_check <= 20e6:
                            range_ok = True
            return range_ok
        except:
            return False

    # check if selected reference is available
    def check_ref(self, func, ref_check):
        try:
            ref_ok = False
            if ref_check == MIN or ref_check == MAX or ref_check == DEF or ref_check == OFF or ref_check == ACQ:
                ref_ok = True
            else:
                ref_check = float(ref_check)
                if func == FUNC_VOLT_AC:
                    if -757.5 <= ref_check <= 757.5:
                        ref_ok = True
                elif func == FUNC_VOLT_DC:
                    if -1010 <= ref_check <= 1010:
                        ref_ok = True
                elif func == FUNC_CURR_AC:
                    if -20 <= ref_check <= 20:
                        ref_ok = True
                elif func == FUNC_CURR_DC:
                    if -0 <= ref_check <= 20:
                        ref_ok = True
                elif func == FUNC_RES:
                    if 0 <= ref_check <= 20e6:
                        ref_ok = True
                elif func == FUNC_FREQ:
                    if 0 <= ref_check <= 1.0e6:
                        ref_ok = True
                elif func == FUNC_PER:
                    if 0 <= ref_check <= 1:
                        ref_ok = True

            return ref_ok
        except:
            return False

    # check if selected trigger is available
    def check_trg(self, trg):
        try:
            trg_ok = False

            if trg == IMM or trg == BUS or trg == MAN:
                trg_ok = True

            return trg_ok
        except:
            return False

    # check if selected state is available
    def check_state(self, state):
        try:
            state_ok = False
            if state == ON or state == OFF:
                state_ok = True
            return state_ok
        except:
            return False

    # check if selected speed is available
    def check_speed(self, speed):
        try:
            speed_ok = False
            if speed == FAST or speed == MED or speed == SLOW or speed == DEF or speed == MIN or speed == MAX:
                speed_ok = True
            return speed_ok
        except:
            return False

    '''CONVERT'''
    # convert func to array
    def convert_func(self, prg, func):
        try:
            if prg == 'range' or prg == 'ref' or prg == 'speed':
                if func == FUNC_VOLT_AC:
                    array_func = ':VOLT:AC'
                elif func == FUNC_VOLT_DC:
                    array_func = ':VOLT:DC'
                elif func == FUNC_CURR_AC:
                    array_func = ':CURR:AC'
                elif func == FUNC_CURR_DC:
                    array_func = ':CURR:DC'
                elif func == FUNC_RES:
                    array_func = ':RES'

            if prg == 'range':
                if func == FUNC_FREQ:
                    array_func = ':FREQ:THR:VOLT'
                elif func == FUNC_PER:
                    array_func = ':PER:THR:VOLT'

            if prg == 'ref':
                if func == FUNC_FREQ:
                    array_func = ':FREQ'
                elif func == FUNC_PER:
                    array_func = ':PER'

            if prg == 'meas':
                if func == FUNC_VOLT_AC:
                    array_func = 'VOLT:AC'
                elif func == FUNC_VOLT_DC:
                    array_func = 'VOLT:DC'
                elif func == FUNC_CURR_AC:
                    array_func = 'CURR:AC'
                elif func == FUNC_CURR_DC:
                    array_func = 'CURR:DC'
                elif func == FUNC_RES:
                    array_func = 'RES'
                elif func == FUNC_FREQ:
                    array_func = 'FREQ'
                elif func == FUNC_PER:
                    array_func = 'PER'
                elif func == FUNC_DIOD:
                    array_func = 'DIOD'
                elif func == FUNC_CONT:
                    array_func = 'CONT'

            return array_func
        except:
            raise Exception('Error: Could not convert func')

    # convert range/ref to array
    def convert_range_ref(self, range_ref):
        try:
            if range_ref == MIN:
                array_range_ref = 'MIN'
            elif range_ref == MAX:
                array_range_ref = 'MAX'
            elif range_ref == DEF:
                array_range_ref = 'DEF'
            else:
                array_range_ref = str(range_ref)

            return array_range_ref
        except:
            raise Exception('Error: Could not convert range/ref')

    # convert trg to array
    def convert_trg(self, trg):
        try:
            if trg == IMM:
                array_trg = 'IMM'
            elif trg == BUS:
                array_trg = 'BUS'
            elif trg == MAN:
                array_trg = 'MAN'

            return array_trg
        except:
            raise Exception('Error: Could not convert trigger')

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

    # convert speed to array
    def convert_speed(self, speed):
        try:
            if speed == FAST or speed == MAX:
                array_speed = 'MAX'
            elif speed == MED or speed == DEF:
                array_speed = 'DEF'
            elif speed == SLOW or speed == MIN:
                array_speed = 'MIN'
            return array_speed
        except:
            raise Exception('Error: Could not convert speed')

    # -----------------------------------------------------------------------
    # PROPERTY
    # -----------------------------------------------------------------------

    '''PRG FOR PROPERTY'''
    # voltage dc
    def _meas_volt_dc(self):
        try:
            return self.meas(FUNC_VOLT_DC)
        except:
            raise

    def _get_range_volt_dc(self):
        try:
            return self.get_range(FUNC_VOLT_DC)
        except:
            raise

    def _set_range_volt_dc(self, range):
        try:
            self.set_range(FUNC_VOLT_DC, range)
        except:
            raise

    def _get_ref_volt_dc(self):
        try:
            return self.get_ref(FUNC_VOLT_DC)
        except:
            raise

    def _set_ref_volt_dc(self, ref):
        try:
            self.set_ref(FUNC_VOLT_DC, ref)
        except:
            raise

    def _get_speed_volt_dc(self):
        try:
            return self.get_meas_speed(FUNC_VOLT_DC)
        except:
            raise

    def _set_speed_volt_dc(self, speed):
        try:
            self.set_meas_speed(FUNC_VOLT_DC, speed)
        except:
            raise

    # voltage ac
    def _meas_volt_ac(self):
        try:
            return self.meas(FUNC_VOLT_AC)
        except:
            raise

    def _get_range_volt_ac(self):
        try:
            return self.get_range(FUNC_VOLT_AC)
        except:
            raise

    def _set_range_volt_ac(self, range):
        try:
            self.set_range(FUNC_VOLT_AC, range)
        except:
            raise

    def _get_ref_volt_ac(self):
        try:
            return self.get_ref(FUNC_VOLT_AC)
        except:
            raise

    def _set_ref_volt_ac(self, ref):
        try:
            self.set_ref(FUNC_VOLT_AC, ref)
        except:
            raise

    def _get_speed_volt_ac(self):
        try:
            return self.get_meas_speed(FUNC_VOLT_AC)
        except:
            raise

    def _set_speed_volt_ac(self, speed):
        try:
            self.set_meas_speed(FUNC_VOLT_AC, speed)
        except:
            raise

    # current dc
    def _meas_curr_dc(self):
        try:
            return self.meas(FUNC_CURR_DC)
        except:
            raise

    def _get_range_curr_dc(self):
        try:
            return self.get_range(FUNC_CURR_DC)
        except:
            raise

    def _set_range_curr_dc(self, range):
        try:
            self.set_range(FUNC_CURR_DC, range)
        except:
            raise

    def _get_ref_curr_dc(self):
        try:
            return self.get_ref(FUNC_CURR_DC)
        except:
            raise

    def _set_ref_curr_dc(self, ref):
        try:
            self.set_ref(FUNC_CURR_DC, ref)
        except:
            raise

    def _get_speed_curr_dc(self):
        try:
            return self.get_meas_speed(FUNC_CURR_DC)
        except:
            raise

    def _set_speed_curr_dc(self, speed):
        try:
            self.set_meas_speed(FUNC_CURR_DC, speed)
        except:
            raise

    # current ac
    def _meas_curr_ac(self):
        try:
            return self.meas(FUNC_CURR_AC)
        except:
            raise

    def _get_range_curr_ac(self):
        try:
            return self.get_range(FUNC_CURR_AC)
        except:
            raise

    def _set_range_curr_ac(self, range):
        try:
            self.set_range(FUNC_CURR_AC, range)
        except:
            raise

    def _get_ref_curr_ac(self):
        try:
            return self.get_ref(FUNC_CURR_AC)
        except:
            raise

    def _set_ref_curr_ac(self, ref):
        try:
            self.set_ref(FUNC_CURR_AC, ref)
        except:
            raise

    def _get_speed_curr_ac(self):
        try:
            return self.get_meas_speed(FUNC_CURR_AC)
        except:
            raise

    def _set_speed_curr_ac(self, speed):
        try:
            self.set_meas_speed(FUNC_CURR_AC, speed)
        except:
            raise

    # resistance
    def _meas_res(self):
        try:
            return self.meas(FUNC_RES)
        except:
            raise

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

    def _get_ref_res(self):
        try:
            return self.get_ref(FUNC_RES)
        except:
            raise

    def _set_ref_res(self, ref):
        try:
            self.set_ref(FUNC_RES, ref)
        except:
            raise

    def _get_speed_res(self):
        try:
            return self.get_meas_speed(FUNC_RES)
        except:
            raise

    def _set_speed_res(self, speed):
        try:
            self.set_meas_speed(FUNC_RES, speed)
        except:
            raise

    # frequency
    def _meas_freq(self):
        try:
            return self.meas(FUNC_FREQ)
        except:
            raise

    def _get_range_freq(self):
        try:
            return self.get_range(FUNC_FREQ)
        except:
            raise

    def _set_range_freq(self, range):
        try:
            self.set_range(FUNC_FREQ, range)
        except:
            raise

    def _get_ref_freq(self):
        try:
            return self.get_ref(FUNC_FREQ)
        except:
            raise

    def _set_ref_freq(self, ref):
        try:
            self.set_ref(FUNC_FREQ, ref)
        except:
            raise

    # period
    def _meas_per(self):
        try:
            return self.meas(FUNC_PER)
        except:
            raise

    def _get_range_per(self):
        try:
            return self.get_range(FUNC_PER)
        except:
            raise

    def _set_range_per(self, range):
        try:
            self.set_range(FUNC_PER, range)
        except:
            raise

    def _get_ref_per(self):
        try:
            return self.get_ref(FUNC_PER)
        except:
            raise

    def _set_ref_per(self, ref):
        try:
            self.set_ref(FUNC_PER, ref)
        except:
            raise

    # select trigger
    def _get_select_trg(self):
        try:
            return self.get_trg()
        except:
            raise

    def _set_select_trg(self, trg):
        try:
            self.set_trg(trg)
        except:
            raise

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

    # diode
    def _meas_diod(self):
        try:
            return self.meas(FUNC_DIOD)
        except:
            raise

    # continuity
    def _meas_cont(self):
        try:
            return self.meas(FUNC_CONT)
        except:
            raise


    '''PROPERTY'''
    # voltage dc
    volt_dc       = property(_meas_volt_dc)
    volt_dc_range = property(_get_range_volt_dc, _set_range_volt_dc)
    volt_dc_ref   = property(_get_ref_volt_dc, _set_ref_volt_dc)
    volt_dc_speed = property(_get_speed_volt_dc, _set_speed_volt_dc)

    # voltage ac
    volt_ac       = property(_meas_volt_ac)
    volt_ac_range = property(_get_range_volt_ac, _set_range_volt_ac)
    volt_ac_ref   = property(_get_ref_volt_ac, _set_ref_volt_ac)
    volt_ac_speed = property(_get_speed_volt_ac, _set_speed_volt_ac)

    # current dc
    curr_dc       = property(_meas_curr_dc)
    curr_dc_range = property(_get_range_curr_dc, _set_range_curr_dc)
    curr_dc_ref   = property(_get_ref_curr_dc, _set_ref_curr_dc)
    curr_dc_speed = property(_get_speed_curr_dc, _set_speed_curr_dc)

    # current ac
    curr_ac       = property(_meas_curr_ac)
    curr_ac_range = property(_get_range_curr_ac, _set_range_curr_ac)
    curr_ac_ref   = property(_get_ref_curr_ac, _set_ref_curr_ac)
    curr_ac_speed = property(_get_speed_curr_ac, _set_speed_curr_ac)

    # resistance
    res       = property(_meas_res)
    res_range = property(_get_range_res, _set_range_res)
    res_ref   = property(_get_ref_res, _set_ref_res)
    res_speed = property(_get_speed_res, _set_speed_res)

    # frequency
    freq       = property(_meas_freq)
    freq_range = property(_get_range_freq, _set_range_freq)
    freq_ref   = property(_get_ref_freq, _set_ref_freq)

    # period
    per       = property(_meas_per)
    per_range = property(_get_range_per, _set_range_per)
    per_ref   = property(_get_ref_per, _set_ref_per)

    # select trigger
    sel_trg = property(_get_select_trg, _set_select_trg)

    # display
    display = property(_get_display, _set_display)

    # diode
    diod = property(_meas_diod)

    # continuity
    cont = property(_meas_cont)