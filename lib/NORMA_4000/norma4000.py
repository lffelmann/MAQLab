"""
WATT_METHODE:
    2 Wattmeter...2
    3 Wattmeter...3

PHASE:
    L1...1      L1-L2........12
    L2...2      L1-L3 (W2)...13
    L3...3      L2-L3........23
                L3-L1 (W3)...31

    average/total/overall value of 1st 3-phase system.........130
    average/total/overall value of 1st 2-phase system (W2)....130
    average phase to phase value of 1st 3-phase system........123
    average phase to phase value of 1st 2-phase system (W2)...123

FUNC:
volt-func:
    trms.....True RMS Voltage (1,2,3);
             Average True RMS Voltage (130);
             True RMS phase to phase Voltage (12,23,31,13);
             Average True RMS Voltage phase to phase (123);
    rms......RMS Voltage (1,2,3);
             Average RMS Voltage (130);
    mean.....Mean Voltage (1,2,3);
             Average Mean Voltage (130);
             Average Mean phase to phase Voltage (123);
    rmean....Rectified Mean Voltage (1,2,3);
             Average Rectified Mean Voltage (130);
             Rectified Mean phase to phase Voltage (12,23,31,13);
             Average Rectified Mean phase to phase Voltage (123);
    rmcorr...Rectified Mean Voltage Corrected (1,2,3);
             Average Rectified Mean Voltage Corrected (130);
             Rectified Mean phase to phase Voltage Corrected (12,23,31,13);
             Average Rectified Mean phase to phase Voltage Corrected (123);
    ptp......peak to peak Voltage (1,2,3);
    phigh....Highest value within averaging interval (1,2,3);
    plow.....Lowest value within averaging interval (1,2,3);
    har......Voltage Harmonic (1,2,3);
             Average Voltage Harmonic (130);
             phase to phase Voltage Harmonic (12,23,31,13);
             Average phase to phase Voltage Harmonic (123);
    cfac.....Voltage Crest Factor (1,2,3);
    phas.....Voltage Absolute Phase (1,2,3);
             phase to phase Absolute Voltage Phase (12,23,31,13);
    ffac.....Voltage Form Factor (1,2,3);
             phase to phase Voltage Form Factor (12,23,31,13);
    hcont....Voltage Harmonic Content (1,2,3);
             phase to phase Voltage Harmonic Content (12,23,31,13);
    fcont....Voltage Fundamental Content (1,2,3);
             phase to phase Voltage Fundamental Content (12,23,31,13);
    thd......Voltage THD (1,2,3)
             phase to phase Voltage THD (12,23,31,13);

curr-func:
    trms.....True RMS Current (1,2,3);
             Average True RMS Current (130);
    rms......RMS Current (1,2,3);
             Average RMS Current (130);
    mean.....Mean Current (1,2,3);
             Average Mean Current (130);
    rmean....Rectified Mean Current (1,2,3);
             Average Rectified Mean Current (130);
    rmcorr...Rectified Mean Current Corrected (1,2,3);
             Average Rectified Mean Current Corrected (130);
    ptp......peak to peak Current (1,2,3);
    phigh....Highest value within averaging interval (1,2,3);
    plow.....Lowest value within averaging interval (1,2,3);
    har......Current Harmonic (1,2,3);
             Average Current Harmonic (130);
    cfac.....Current Crest Factor (1,2,3);
    phas.....Current Absolute Phase (1,2,3);
    ffac.....Current Form Factor (1,2,3);
    hcont....Current Harmonic Content (1,2,3);
    fcont....Current Fundamental Content (1,2,3);
    thd......Current THD (1,2,3);

pwr-func:
    act.......Active Power (1,2,3);
              Total Active Power (130);
    app.......Apparent Power (1,2,3);
              Total Apparent Power (130);
    reac......Reactive Power (1,2,3);
              Total Reactive Power (130);
    fact......Power Factor (1,2,3);
              Total Power Factor (130);
    corr......Corrected Power (1,2,3);
              Total Corrected Power (130);
    eff.......Total Electrical Efficiency (130);
    har.......Active Power Harmonic (1,2,3);
              Total Active Power Harmonic (130);
    apphar....Apparent Power Harmonic (1,2,3);
              Total Apparent Power Harmonic (130);
    reachar...Reactive Power Harmonic (1,2,3);
              Total Reactive Power Harmonic (130);
    facthar...Power Factor Harmonic (1,2,3);
              Total Power Factor Harmonic (130);
    effhar....Total Electrical Efficiency Harmonic (130);

phas-func:
    std...Phase angle (1,2,3);
          Total Phase Angle (130);
    har...Phase angle Harmonic (1,2,3);
          Total Phase Angle Harmonic (130);

imp-func:
    app......Apparent Impedance (1,2,3);
             Total Apparent Impedance (130);
    apphar...Apparent Impedance Harmonic (1,2,3);
             Total Apparent Impedance Harmonic (130);

res-func:
    ser......Serial Resistance (1,2,3);
             Total Serial Resistance (130);
    par......Parallel Resistance (1,2,3);
             Total Parallel Resistance (130);
    serhar...Serial Resistance Harmonic (1,2,3);
             Total Serial Resistance Harmonic (130);
    parhar...Parallel Resistance Harmonic (1,2,3);
             Total Parallel Resistance Harmonic (130);

react-func:
    ser......Serial Reactance (1,2,3);
             Total Serial Reactance (130);
    par......Parallel Reactance (1,2,3);
             Total Parallel Reactance (130);
    serhar...Serial Reactance Harmonic (1,2,3);
             Total Serial Reactance Harmonic (130);
    parhar...Parallel Reactance Harmonic (1,2,3);
             Total Parallel Reactance Harmonic (130);
"""

import socket
import time

BUFFER = 1024

DEFAULT_PORT = 23

class NORMA4000:
    # wattmeter method 0...not set
    watt_methode = 0

    # measurement method continuous False...not set
    cont_measurement = False

    # lists functions
    list_volt_curr_func = ['trms', 'rms', 'mean', 'rmean', 'rmcorr', 'ptp', 'phigh', 'plow', 'har', 'cfac', 'phas',
                           'ffac', 'hcont', 'fcont', 'thd']
    list_pow_func = ['act', 'app', 'reac', 'fact', 'corr', 'eff', 'har', 'apphar', 'reachar', 'facthar', 'effhar']
    list_phas_func = ['std', 'har']
    list_imp_func = ['app', 'apphar']
    list_res_react_func = ['ser', 'par', 'serhar', 'parhar']

    # lists phase
    list_volt_phase = [1, 2, 3, 12, 13, 23, 31, 130, 123]
    list_curr_pow_phas_imp_res_react_phase = [1, 2, 3, 130]

    # lists phase functions
    list_130_phasefunc = [130]
    list_1_2_3_130_phasefunc = [1, 2, 3, 130]
    list_1_2_3_phasefunc = [1, 2, 3]
    list_1_2_3_123_130_phasefunc = [1, 2, 3, 123, 130]
    list_1_2_3_12_13_23_31_phasefunc = [1, 2, 3, 12, 13, 23, 31]
    list_all_phasefunc = [1, 2, 3, 12, 13, 23, 31, 130, 123]


    '''CONNECTION + INITIAL'''
    # initial NORMA4000, establish connection
    def __init__(self, ip_add, port=DEFAULT_PORT):
        try:
            pass
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
                return data.strip('\t\n\r ')
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
            self.watt_methode = 0
            self.cont_measurement = False
        except:
            raise

    '''SET MEASUREMENT METHOD ON CONTINUOUS'''
    def cont_meas(self):
        try:
            msg = bytearray('INIT:CONT ON\r\n', 'utf-8')
            self.send_msg(msg, False)
            self.cont_measurement = True
        except:
            self.cont_measurement = False
            raise

    '''SET WATTMETER METHOD'''
    def watt_meth(self, methode):
        try:
            methode = float(methode)
            if methode == 2:
                methode_array = '"2W"'
                self.watt_methode = 2
            elif methode == 3:
                methode_array = '"3W"'
                self.watt_methode = 3
            else:
                raise Exception('Error: Unknown Wattmeter Methode')

            msg = bytearray('ROUTe:SYSTem' + methode_array + '\r\n', 'utf-8')
            self.send_msg(msg, False)
        except:
            raise

    # ---------------------------------------------------------
    # MEASUREMENT
    # ---------------------------------------------------------

    '''VOLTAGE'''
    def volt(self, func, phase):
        try:
            if not self.check_watt_meth():                                                                      # check if wattmeter method is selected
                raise Exception('Error: No wattmeter method selected')
            if not self.check_func('volt', func):                                                               # check if func is available
                raise Exception('Error: Function is not available')
            if not self.check_phase('volt', phase):                                                             # check if phase is available
                raise Exception('Error: Phase is not available')
            if not self.check_phase_watt(phase):                                                                # check if phase and wattmeter method match
                raise Exception('Error: Phase and wattmeter method dont match')
            if not self.check_phase_func('volt', phase, func):                                                  # check if phase and function match
                raise Exception('Error: Phase and function dont match')
            if not self.check_cont_meas():                                                                      # if measurement method is not continuous -> set measurement method on continuous
                self.cont_meas()
                time.sleep(1)

            array_func = self.convert_func(func)                                                                # convert func to array for msg
            array_phase = self.convert_phase(phase)                                                             # convert phase to array for msg

            msg = bytearray('DATA? "VOLT' + str(array_phase) + str(array_func) + '"\r\n','utf-8')               # get voltage and return voltage
            data = self.send_msg(msg, True)
            return float(data)
        except:
            raise

    '''CURRENT'''
    def curr(self, func, phase):
        try:
            if not self.check_watt_meth():                                      # check if wattmeter method is selected
                raise Exception('Error: No wattmeter method selected')
            if not self.check_func('curr', func):                               # check if func is available
                raise Exception('Error: Function is not available')
            if not self.check_phase('curr', phase):                             # check if phase is available
                raise Exception('Error: Phase is not available')
            if not self.check_phase_func('curr', phase, func):                  # check if phase and function match
                raise Exception('Error: Phase and function dont match')
            if not self.check_cont_meas():                                      # if measurement method is not continuous -> set measurement method on continuous
                self.cont_meas()
                time.sleep(1)

            array_func = self.convert_func(func)                                # convert func to array for msg
            array_phase = self.convert_phase(phase)                             # convert phase to array for msg

            msg = bytearray('DATA? "CURR' + str(array_phase) + str(array_func) + '"\r\n', 'utf-8')     # get current and return current
            data = self.send_msg(msg, True)
            return float(data)
        except:
            raise

    '''POWER'''
    def pwr(self, func, phase):
        try:
            if not self.check_watt_meth():                                      # check if wattmeter method is selected
                raise Exception('Error: No wattmeter method selected')
            if not self.check_func('pow', func):                                # check if func is available
                raise Exception('Error: Function is not available')
            if not self.check_phase('pow', phase):                              # check if phase is available
                raise Exception('Error: Phase is not available')
            if not self.check_phase_func('pow', phase, func):                   # check if phase and function match
                raise Exception('Error: Phase and function dont match')
            if not self.check_cont_meas():                                      # if measurement method is not continuous -> set measurement method on continuous
                self.cont_meas()
                time.sleep(1)

            array_func = self.convert_func(func)                                # convert func to array for msg
            array_phase = self.convert_phase(phase)                             # convert phase to array for msg

            msg = bytearray('DATA? "POW' + str(array_phase) + str(array_func) + '"\r\n', 'utf-8')     # get power and return power
            data = self.send_msg(msg, True)
            return float(data)
        except:
            raise

    '''PHASE'''
    def phas(self, func, phase):
        try:
            if not self.check_watt_meth():                                      # check if wattmeter method is selected
                raise Exception('Error: No wattmeter method selected')
            if not self.check_func('phas', func):                               # check if func is available
                raise Exception('Error: Function is not available')
            if not self.check_phase('phas', phase):                             # check if phase is available
                raise Exception('Error: Phase is not available')
            if not self.check_cont_meas():                                      # if measurement method is not continuous -> set measurement method on continuous
                self.cont_meas()
                time.sleep(1)

            array_func = self.convert_func(func)                                # convert func to array for msg
            array_phase = self.convert_phase(phase)                             # convert phase to array for msg

            msg = bytearray('DATA? "PHAS' + str(array_phase) + str(array_func) + '"\r\n', 'utf-8')     # get phase and return phase
            data = self.send_msg(msg, True)
            return float(data)
        except:
            raise

    '''IMPEDANCE'''
    def imp(self, func, phase):
        try:
            if not self.check_watt_meth():                                      # check if wattmeter method is selected
                raise Exception('Error: No wattmeter method selected')
            if not self.check_func('imp', func):                                # check if func is available
                raise Exception('Error: Function is not available')
            if not self.check_phase('imp', phase):                              # check if phase is available
                raise Exception('Error: Phase is not available')
            if not self.check_cont_meas():                                      # if measurement method is not continuous -> set measurement method on continuous
                self.cont_meas()
                time.sleep(1)

            array_func = self.convert_func(func)                                # convert func to array for msg
            array_phase = self.convert_phase(phase)                             # convert phase to array for msg

            msg = bytearray('DATA? "IMP' + str(array_phase) + str(array_func) + '"\r\n', 'utf-8')     # get impedance and return impedance
            data = self.send_msg(msg, True)
            return float(data)
        except:
            raise

    '''RESISTANCE'''
    def res(self, func, phase):
        try:
            if not self.check_watt_meth():                                      # check if wattmeter method is selected
                raise Exception('Error: No wattmeter method selected')
            if not self.check_func('res', func):                                # check if func is available
                raise Exception('Error: Function is not available')
            if not self.check_phase('res', phase):                              # check if phase is available
                raise Exception('Error: Phase is not available')
            if not self.check_cont_meas():                                      # if measurement method is not continuous -> set measurement method on continuous
                self.cont_meas()
                time.sleep(1)

            array_func = self.convert_func(func)                                # convert func to array for msg
            array_phase = self.convert_phase(phase)                             # convert phase to array for msg

            msg = bytearray('DATA? "RES' + str(array_phase) + str(array_func) + '"\r\n', 'utf-8')     # get resistance and return resistance
            data = self.send_msg(msg, True)
            return float(data)
        except:
            raise

    '''REACTANCE'''
    def react(self, func, phase):
        try:
            if not self.check_watt_meth():                                      # check if wattmeter method is selected
                raise Exception('Error: No wattmeter method selected')
            if not self.check_func('react', func):                              # check if func is available
                raise Exception('Error: Function is not available')
            if not self.check_phase('react', phase):                            # check if phase is available
                raise Exception('Error: Phase is not available')
            if not self.check_cont_meas():                                      # if measurement method is not continuous -> set measurement method on continuous
                self.cont_meas()
                time.sleep(1)

            array_func = self.convert_func(func)                                # convert func to array for msg
            array_phase = self.convert_phase(phase)                             # convert phase to array for msg

            msg = bytearray('DATA? "REACT' + str(array_phase) + str(array_func) + '"\r\n', 'utf-8')     # get reactance and return reactance
            data = self.send_msg(msg, True)
            return float(data)
        except:
            raise

    # ---------------------------------------------------------
    # CHECK + CONVERT
    # ---------------------------------------------------------

    '''CHECK'''
    # check if func exist
    def check_func(self, mode, func):
        try:
            list_func = []
            func_available = False
            if mode == 'volt' or mode == 'curr':
                list_func = self.list_volt_curr_func
            elif mode == 'pow':
                list_func = self.list_pow_func
            elif mode == 'phas':
                list_func = self.list_phas_func
            elif mode == 'imp':
                list_func = self.list_imp_func
            elif mode == 'res' or mode == 'react':
                list_func = self.list_res_react_func
            for i in range(0, len(list_func)):
                if func == list_func[i]:
                    func_available = True
                    break
            return func_available
        except:
            return False

    # check if wattmeter method selected
    def check_watt_meth(self):
        try:
            if self.watt_methode == 0:
                return False
            else:
                return True
        except:
            return False

    # check if phase exist
    def check_phase(self, mode, phase):
        try:
            phase = float(phase)
            list_phase = []
            phase_exist = False
            if mode == 'volt':
                list_phase = self.list_volt_phase
            elif mode == 'curr' or mode == 'pow' or mode == 'phas' or mode == 'imp' or mode == 'res' or mode == 'react':
                list_phase = self.list_curr_pow_phas_imp_res_react_phase
            for i in range(0, len(list_phase)):
                if phase == list_phase[i]:
                    phase_exist = True
                    break
            return phase_exist
        except:
            return False

    # check if phase and wattmeter method match
    def check_phase_watt(self, phase):
        try:
            phase = float(phase)
            phase_watt_match = True
            if (self.watt_methode == 2 and phase == 31) or (self.watt_methode == 3 and phase == 13):
                phase_watt_match = False
            return phase_watt_match
        except:
            return False

    # check if phase and func match
    def check_phase_func(self, mode, phase, func):
        try:
            phase = float(phase)
            list_phase = []
            phase_func_match = False
            if mode == 'curr':
                if func == 'trms' or func == 'rms' or func == 'mean' or func == 'rmean' or func == 'rmcorr' or func == 'har':
                    list_phase = self.list_1_2_3_130_phasefunc
                else:
                    list_phase = self.list_1_2_3_phasefunc
            if mode == 'volt':
                if func == 'ptp' or func == 'phigh' or func == 'plow' or func == 'cfac':
                    list_phase = self.list_1_2_3_phasefunc
                elif func == 'rms':
                    list_phase = self.list_1_2_3_130_phasefunc
                elif func == 'trms' or func == 'rmean' or func == 'rmcorr' or func == 'har':
                    list_phase = self.list_all_phasefunc
                elif func == 'phas' or func == 'ffac' or func == 'hcont' or func == 'fcont' or func == 'thd':
                    list_phase = self.list_1_2_3_12_13_23_31_phasefunc
                else:
                    list_phase = self.list_1_2_3_123_130_phasefunc
            if mode == 'pow':
                if func == 'eff' or func == 'effhar':
                    list_phase = self.list_130_phasefunc
                else:
                    list_phase = self.list_1_2_3_130_phasefunc
            for i in range(0, len(list_phase)):
                if phase == list_phase[i]:
                    phase_func_match = True
                    break
            return phase_func_match
        except:
            return False

    # check if measurement method is continue
    def check_cont_meas(self):
        try:
            return self.cont_measurement
        except:
            return False

    '''CONVERT'''
    # convert func to array
    def convert_func(self, func):
        try:
            array_func = ''
            if func == 'trms':
                array_func = ':DC'
            elif func == 'rms':
                array_func = ':AC'
            elif func == 'mean':
                array_func = ':MEAN'
            elif func == 'rmean':
                array_func = ':RMEAN'
            elif func == 'rmcorr':
                array_func = ':RMCORR'
            elif func == 'ptp':
                array_func = ':PTP'
            elif func == 'phigh':
                array_func = ':PHIGH'
            elif func == 'plow':
                array_func = ':PLOW'
            elif func == 'har':
                array_func = ':HAR'
            elif func == 'cfac':
                array_func = ':CFAC'
            elif func == 'phas':
                array_func = ':PHAS'
            elif func == 'ffac':
                array_func = ':FFAC'
            elif func == 'hcont':
                array_func = ':HCONT'
            elif func == 'fcont':
                array_func = ':FCONT'
            elif func == 'thd':
                array_func = ':THD'
            elif func == 'act':
                array_func = ':ACT'
            elif func == 'app':
                array_func = ':APP'
            elif func == 'reac':
                array_func = ':REAC'
            elif func == 'fact':
                array_func = ':FACT'
            elif func == 'corr':
                array_func = ':CORR'
            elif func == 'eff':
                array_func = ':EFF'
            elif func == 'apphar':
                array_func = ':APP:HAR'
            elif func == 'reachar':
                array_func = ':REAC:HAR'
            elif func == 'facthar':
                array_func = ':FACT:HAR'
            elif func == 'effhar':
                array_func = ':EFF:HAR'
            elif func == 'std':
                array_func = ''
            elif func == 'ser':
                array_func = ':SER'
            elif func == 'par':
                array_func = ':PAR'
            elif func == 'serhar':
                array_func = ':SER:HAR'
            elif func == 'parhar':
                array_func = ':PAR:HAR'
            return array_func
        except:
            raise Exception('Error: Could not convert function')

    # convert phase to array
    def convert_phase(self, phase):
        try:
            phase = int(phase)
            if phase == 130:
                phase = ''
            else:
                phase = str(phase)
            return phase
        except:
            raise Exception('Error: Could not convert phase')