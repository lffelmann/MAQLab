import bk2831e as bk
import time

PORT = 'COM3'

if __name__ == '__main__':

    voltac = bk.FUNC_VOLT_AC
    voltdc = bk.FUNC_VOLT_DC
    currac = bk.FUNC_CURR_AC
    currdc = bk.FUNC_CURR_DC
    res    = bk.FUNC_RES
    freq   = bk.FUNC_FREQ
    per    = bk.FUNC_PER
    diod   = bk.FUNC_DIOD
    cont   = bk.FUNC_CONT

    auto = bk.AUTO
    maxi = bk.MAX
    mini = bk.MIN
    defa = bk.DEF
    acq  = bk.ACQ
    off  = bk.OFF
    on   = bk.ON

    imm = bk.IMM
    bus = bk.BUS
    man = bk.MAN

    fas = bk.FAST
    med = bk.MED
    slo = bk.SLOW

    state_display = [off, on]
    state_trigger = [man, bus, imm]
    list_range = [-20, 0, 0.2, 2, 20, 200, 750, 1000, 1010, 20e6, defa, mini, maxi, auto]
    list_ref = [-1010, -757.5, -20, 0, 1, 20, 757.5, 1010, 1.0e6, 20e6, defa, mini, maxi, off, acq]
    list_speed = [fas, med, slo, maxi, mini, defa]


    try:
        device = bk.BK2831E(PORT)
    except Exception as e:
            print(e)

    print('id(): ')
    try:
        print(device.id())
    except Exception as e:
        print(e)


    print('\n-------------------------------\nDISPLAY\n------------------------------\n')

    for i in range(0, len(state_display)):

        print('set_display(' + state_display[i] + '): ')
        try:
            device.set_display(state_display[i])
        except Exception as e:
            print(e)
        time.sleep(1)

        print('get_display(): ')
        try:
            print(device.get_display())
        except Exception as e:
            print(e)
        
    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    print('\nPROPERTY\n')

    for i in range(0, len(state_display)):

        print('display = ' + state_display[i] + ': ')
        try:
            device.display = state_display[i]
        except Exception as e:
            print(e)
        time.sleep(1)

        print('display: ')
        try:
            print(device.display)
        except Exception as e:
            print(e)

    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    print('\n-------------------------------\nTRIGGER\n------------------------------\n')
    
    for i in range(0, len(state_trigger)):

        print('set_trg(' + state_trigger[i] + '): ')
        try:
            device.set_trg(state_trigger[i])
        except Exception as e:
            print(e)
        time.sleep(1)

        print('get_trg(): ')
        try:
            print(device.get_trg())
        except Exception as e:
            print(e)

        print('trg(): ')
        try:
            device.trg()
        except Exception as e:
            print(e)
        time.sleep(1)

    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    print('\nPROPERTY\n')
    
    for i in range(0, len(state_trigger)):
        
        print('sel_trg = ' + state_trigger[i] + ': ')
        try:
            device.sel_trg = state_trigger[i]
        except Exception as e:
            print(e)
        time.sleep(1)

        print('sel_trg: ')
        try:
            print(device.sel_trg)
        except Exception as e:
            print(e)
        
        print('trg(): ')
        try:
            device.trg()
        except Exception as e:
            print(e)
        time.sleep(1)

    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    print('\n-------------------------------\nVOLTAGE AC\n------------------------------\n')

    # range
    for i in range(0, len(list_range)):

        print('set_range(voltac, ' + str(list_range[i]) + '): ')
        try:
            device.set_range(voltac, list_range[i])
        except Exception as e:
            print(e)
        time.sleep(1)
        
        print('get_range(voltac): ')
        try:
            print(device.get_range(voltac))
        except Exception as e:
            print(e)
    
    print('rst(): ')
    try:    
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    #reference
    for i in range(0, len(list_ref)):

        print('set_ref(voltac, ' + str(list_ref[i]) + '): ')
        try:
            device.set_ref(voltac, list_ref[i])
        except Exception as e:
            print(e)
        time.sleep(1)

        print('get_ref(voltac): ')
        try:
            print(device.get_ref(voltac))
        except Exception as e:
            print(e)

    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    # measurement speed
    for i in range(0, len(list_speed)):

        print('set_meas_speed(voltac, ' + str(list_speed[i]) + '): ')
        try:
            device.set_meas_speed(voltac, list_speed[i])
        except Exception as e:
            print(e)
        time.sleep(1)

        print('get_meas_speed(voltac): ')
        try:
            print(device.get_meas_speed(voltac))
        except Exception as e:
            print(e)

    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    # measure
    print('meas(voltac): ')
    try:
        print(device.meas(voltac))
    except Exception as e:
        print(e)
        
    print('rst(): ')
    try:
        device.rst()  
    except Exception as e:
        print(e)
    time.sleep(1)

    print('\nPROPERTY\n')

    # range
    for i in range(0, len(list_range)):

        print('volt_ac_range = ' + str(list_range[i]) + ': ')
        try:
            device.volt_ac_range = list_range[i]
        except Exception as e:
            print(e)
        time.sleep(1)

        print('volt_ac_range: ')
        try:
            print(device.volt_ac_range)
        except Exception as e:
            print(e)
    
    print('rst(): ')
    try: 
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    #reference
    for i in range(0, len(list_ref)):
        
        print('volt_ac_ref = ' + str(list_ref[i]) + '): ')
        try:
            device.volt_ac_ref = list_ref[i]
        except Exception as e:
            print(e)
        time.sleep(1)

        print('volt_ac_ref: ')
        try:
            print(device.volt_ac_ref)
        except Exception as e:
            print(e)

    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    # measurement speed
    for i in range(0, len(list_speed)):
        
        print('volt_ac_speed = ' + str(list_speed[i]) + ': ')
        try:
            device.volt_ac_speed = list_speed[i]
        except Exception as e:
            print(e)
        time.sleep(1)

        print('volt_ac_speed: ')
        try:
            print(device.volt_ac_speed)
        except Exception as e:
            print(e)

    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    # measure
    print('volt_ac: ')
    try:
        print(device.volt_ac)
    except Exception as e:
        print(e)
        
    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    print('\n-------------------------------\nVOLTAGE DC\n------------------------------\n')

    # range
    for i in range(0, len(list_range)):

        print('set_range(voltdc, ' + str(list_range[i]) + '): ')
        try:
            device.set_range(voltdc, list_range[i])
        except Exception as e:
            print(e)
        time.sleep(1)
        
        print('get_range(voltdc): ')
        try:
            print(device.get_range(voltdc))
        except Exception as e:
            print(e)
    
    print('rst(): ')
    try:    
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    #reference
    for i in range(0, len(list_ref)):

        print('set_ref(voltdc, ' + str(list_ref[i]) + '): ')
        try:
            device.set_ref(voltdc, list_ref[i])
        except Exception as e:
            print(e)
        time.sleep(1)

        print('get_ref(voltdc): ')
        try:
            print(device.get_ref(voltdc))
        except Exception as e:
            print(e)

    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    # measurement speed
    for i in range(0, len(list_speed)):

        print('set_meas_speed(voltdc, ' + str(list_speed[i]) + '): ')
        try:
            device.set_meas_speed(voltdc, list_speed[i])
        except Exception as e:
            print(e)
        time.sleep(1)

        print('get_meas_speed(voltdc): ')
        try:
            print(device.get_meas_speed(voltdc))
        except Exception as e:
            print(e)

    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    # measure
    print('meas(voltdc): ')
    try:
        print(device.meas(voltdc))
    except Exception as e:
        print(e)
        
    print('rst(): ')
    try:
        device.rst()  
    except Exception as e:
        print(e)
    time.sleep(1)

    print('\nPROPERTY\n')

    # range
    for i in range(0, len(list_range)):

        print('volt_dc_range = ' + str(list_range[i]) + ': ')
        try:
            device.volt_dc_range = list_range[i]
        except Exception as e:
            print(e)
        time.sleep(1)

        print('volt_dc_range: ')
        try:
            print(device.volt_dc_range)
        except Exception as e:
            print(e)
    
    print('rst(): ')
    try: 
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    #reference
    for i in range(0, len(list_ref)):
        
        print('volt_dc_ref = ' + str(list_ref[i]) + '): ')
        try:
            device.volt_dc_ref = list_ref[i]
        except Exception as e:
            print(e)
        time.sleep(1)

        print('volt_dc_ref: ')
        try:
            print(device.volt_dc_ref)
        except Exception as e:
            print(e)

    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    # measurement speed
    for i in range(0, len(list_speed)):
        
        print('volt_dc_speed = ' + str(list_speed[i]) + ': ')
        try:
            device.volt_dc_speed = list_speed[i]
        except Exception as e:
            print(e)
        time.sleep(1)

        print('volt_dc_speed: ')
        try:
            print(device.volt_dc_speed)
        except Exception as e:
            print(e)

    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    # measure
    print('volt_dc: ')
    try:
        print(device.volt_dc)
    except Exception as e:
        print(e)
        
    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    print('\n-------------------------------\nCURRENT AC\n------------------------------\n')

    # range
    for i in range(0, len(list_range)):

        print('set_range(currac, ' + str(list_range[i]) + '): ')
        try:
            device.set_range(currac, list_range[i])
        except Exception as e:
            print(e)
        time.sleep(1)
        
        print('get_range(currac): ')
        try:
            print(device.get_range(currac))
        except Exception as e:
            print(e)
    
    print('rst(): ')
    try:    
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    #reference
    for i in range(0, len(list_ref)):

        print('set_ref(currac, ' + str(list_ref[i]) + '): ')
        try:
            device.set_ref(currac, list_ref[i])
        except Exception as e:
            print(e)
        time.sleep(1)

        print('get_ref(currac): ')
        try:
            print(device.get_ref(currac))
        except Exception as e:
            print(e)

    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    # measurement speed
    for i in range(0, len(list_speed)):

        print('set_meas_speed(currac, ' + str(list_speed[i]) + '): ')
        try:
            device.set_meas_speed(currac, list_speed[i])
        except Exception as e:
            print(e)
        time.sleep(1)

        print('get_meas_speed(currac): ')
        try:
            print(device.get_meas_speed(currac))
        except Exception as e:
            print(e)

    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    # measure
    print('meas(currac): ')
    try:
        print(device.meas(currac))
    except Exception as e:
        print(e)
        
    print('rst(): ')
    try:
        device.rst()  
    except Exception as e:
        print(e)
    time.sleep(1)

    print('\nPROPERTY\n')

    # range
    for i in range(0, len(list_range)):

        print('curr_ac_range = ' + str(list_range[i]) + ': ')
        try:
            device.curr_ac_range = list_range[i]
        except Exception as e:
            print(e)
        time.sleep(1)

        print('curr_ac_range: ')
        try:
            print(device.curr_ac_range)
        except Exception as e:
            print(e)
    
    print('rst(): ')
    try: 
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    #reference
    for i in range(0, len(list_ref)):
        
        print('curr_ac_ref = ' + str(list_ref[i]) + '): ')
        try:
            device.curr_ac_ref = list_ref[i]
        except Exception as e:
            print(e)
        time.sleep(1)

        print('curr_ac_ref: ')
        try:
            print(device.curr_ac_ref)
        except Exception as e:
            print(e)

    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    # measurement speed
    for i in range(0, len(list_speed)):
        
        print('curr_ac_speed = ' + str(list_speed[i]) + ': ')
        try:
            device.curr_ac_speed = list_speed[i]
        except Exception as e:
            print(e)
        time.sleep(1)

        print('curr_ac_speed: ')
        try:
            print(device.curr_ac_speed)
        except Exception as e:
            print(e)

    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    # measure
    print('curr_ac: ')
    try:
        print(device.curr_ac)
    except Exception as e:
        print(e)
        
    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    print('\n-------------------------------\nCURRENT DC\n------------------------------\n')

    # range
    for i in range(0, len(list_range)):

        print('set_range(currdc, ' + str(list_range[i]) + '): ')
        try:
            device.set_range(currdc, list_range[i])
        except Exception as e:
            print(e)
        time.sleep(1)
        
        print('get_range(currdc): ')
        try:
            print(device.get_range(currdc))
        except Exception as e:
            print(e)
    
    print('rst(): ')
    try:    
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    #reference
    for i in range(0, len(list_ref)):

        print('set_ref(currdc, ' + str(list_ref[i]) + '): ')
        try:
            device.set_ref(currdc, list_ref[i])
        except Exception as e:
            print(e)
        time.sleep(1)

        print('get_ref(currdc): ')
        try:
            print(device.get_ref(currdc))
        except Exception as e:
            print(e)

    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    # measurement speed
    for i in range(0, len(list_speed)):

        print('set_meas_speed(currdc, ' + str(list_speed[i]) + '): ')
        try:
            device.set_meas_speed(currdc, list_speed[i])
        except Exception as e:
            print(e)
        time.sleep(1)

        print('get_meas_speed(currdc): ')
        try:
            print(device.get_meas_speed(currdc))
        except Exception as e:
            print(e)

    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    # measure
    print('meas(currdc): ')
    try:
        print(device.meas(currdc))
    except Exception as e:
        print(e)
        
    print('rst(): ')
    try:
        device.rst()  
    except Exception as e:
        print(e)
    time.sleep(1)

    print('\nPROPERTY\n')

    # range
    for i in range(0, len(list_range)):

        print('curr_dc_range = ' + str(list_range[i]) + ': ')
        try:
            device.curr_dc_range = list_range[i]
        except Exception as e:
            print(e)
        time.sleep(1)

        print('curr_dc_range: ')
        try:
            print(device.curr_dc_range)
        except Exception as e:
            print(e)
    
    print('rst(): ')
    try: 
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    #reference
    for i in range(0, len(list_ref)):
        
        print('curr_dc_ref = ' + str(list_ref[i]) + '): ')
        try:
            device.curr_dc_ref = list_ref[i]
        except Exception as e:
            print(e)
        time.sleep(1)

        print('curr_dc_ref: ')
        try:
            print(device.curr_dc_ref)
        except Exception as e:
            print(e)

    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    # measurement speed
    for i in range(0, len(list_speed)):
        
        print('curr_dc_speed = ' + str(list_speed[i]) + ': ')
        try:
            device.curr_dc_speed = list_speed[i]
        except Exception as e:
            print(e)
        time.sleep(1)

        print('curr_dc_speed: ')
        try:
            print(device.curr_dc_speed)
        except Exception as e:
            print(e)

    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    # measure
    print('curr_dc: ')
    try:
        print(device.curr_dc)
    except Exception as e:
        print(e)
        
    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    print('\n-------------------------------\nRESISTANCE\n------------------------------\n')

    # range
    for i in range(0, len(list_range)):

        print('set_range(res, ' + str(list_range[i]) + '): ')
        try:
            device.set_range(res, list_range[i])
        except Exception as e:
            print(e)
        time.sleep(1)
        
        print('get_range(res): ')
        try:
            print(device.get_range(res))
        except Exception as e:
            print(e)
    
    print('rst(): ')
    try:    
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    #reference
    for i in range(0, len(list_ref)):

        print('set_ref(res, ' + str(list_ref[i]) + '): ')
        try:
            device.set_ref(res, list_ref[i])
        except Exception as e:
            print(e)
        time.sleep(1)

        print('get_ref(res): ')
        try:
            print(device.get_ref(res))
        except Exception as e:
            print(e)

    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    # measurement speed
    for i in range(0, len(list_speed)):

        print('set_meas_speed(res, ' + str(list_speed[i]) + '): ')
        try:
            device.set_meas_speed(res, list_speed[i])
        except Exception as e:
            print(e)
        time.sleep(1)

        print('get_meas_speed(res): ')
        try:
            print(device.get_meas_speed(res))
        except Exception as e:
            print(e)

    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    # measure
    print('meas(res): ')
    try:
        print(device.meas(res))
    except Exception as e:
        print(e)
        
    print('rst(): ')
    try:
        device.rst()  
    except Exception as e:
        print(e)
    time.sleep(1)

    print('\nPROPERTY\n')

    # range
    for i in range(0, len(list_range)):

        print('res_range = ' + str(list_range[i]) + ': ')
        try:
            device.res_range = list_range[i]
        except Exception as e:
            print(e)
        time.sleep(1)

        print('res_range: ')
        try:
            print(device.res_range)
        except Exception as e:
            print(e)
    
    print('rst(): ')
    try: 
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    #reference
    for i in range(0, len(list_ref)):
        
        print('res_ref = ' + str(list_ref[i]) + '): ')
        try:
            device.res_ref = list_ref[i]
        except Exception as e:
            print(e)
        time.sleep(1)

        print('res_ref: ')
        try:
            print(device.res_ref)
        except Exception as e:
            print(e)

    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    # measurement speed
    for i in range(0, len(list_speed)):
        
        print('res_speed = ' + str(list_speed[i]) + ': ')
        try:
            device.res_speed = list_speed[i]
        except Exception as e:
            print(e)
        time.sleep(1)

        print('res_speed: ')
        try:
            print(device.res_speed)
        except Exception as e:
            print(e)

    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    # measure
    print('res: ')
    try:
        print(device.res)
    except Exception as e:
        print(e)
        
    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    print('\n-------------------------------\nFREQUENCY\n------------------------------\n')

    # range
    for i in range(0, len(list_range)):

        print('set_range(freq, ' + str(list_range[i]) + '): ')
        try:
            device.set_range(freq, list_range[i])
        except Exception as e:
            print(e)
        time.sleep(1)
        
        print('get_range(freq): ')
        try:
            print(device.get_range(freq))
        except Exception as e:
            print(e)
    
    print('rst(): ')
    try:    
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    #reference
    for i in range(0, len(list_ref)):

        print('set_ref(freq, ' + str(list_ref[i]) + '): ')
        try:
            device.set_ref(freq, list_ref[i])
        except Exception as e:
            print(e)
        time.sleep(1)

        print('get_ref(freq: ')
        try:
            print(device.get_ref(freq))
        except Exception as e:
            print(e)

    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    # measure
    print('meas(freq): ')
    try:
        print(device.meas(freq))
    except Exception as e:
        print(e)
        
    print('rst(): ')
    try:
        device.rst()  
    except Exception as e:
        print(e)
    time.sleep(1)

    print('\nPROPERTY\n')

    # range
    for i in range(0, len(list_range)):

        print('freq_range = ' + str(list_range[i]) + ': ')
        try:
            device.freq_range = list_range[i]
        except Exception as e:
            print(e)
        time.sleep(1)

        print('freq_range: ')
        try:
            print(device.freq_range)
        except Exception as e:
            print(e)
    
    print('rst(): ')
    try: 
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    #reference
    for i in range(0, len(list_ref)):
        
        print('freq_ref = ' + str(list_ref[i]) + '): ')
        try:
            device.freq_ref = list_ref[i]
        except Exception as e:
            print(e)
        time.sleep(1)

        print('freq_ref: ')
        try:
            print(device.freq_ref)
        except Exception as e:
            print(e)

    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    # measure
    print('freq: ')
    try:
        print(device.freq)
    except Exception as e:
        print(e)
        
    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    print('\n-------------------------------\nPERIODE\n------------------------------\n')

    # range
    for i in range(0, len(list_range)):

        print('set_range(per, ' + str(list_range[i]) + '): ')
        try:
            device.set_range(per, list_range[i])
        except Exception as e:
            print(e)
        time.sleep(1)
        
        print('get_range(per): ')
        try:
            print(device.get_range(per))
        except Exception as e:
            print(e)
    
    print('rst(): ')
    try:    
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    #reference
    for i in range(0, len(list_ref)):

        print('set_ref(per, ' + str(list_ref[i]) + '): ')
        try:
            device.set_ref(per, list_ref[i])
        except Exception as e:
            print(e)
        time.sleep(1)

        print('get_ref(per: ')
        try:
            print(device.get_ref(per))
        except Exception as e:
            print(e)

    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    # measure
    print('meas(per): ')
    try:
        print(device.meas(per))
    except Exception as e:
        print(e)
        
    print('rst(): ')
    try:
        device.rst()  
    except Exception as e:
        print(e)
    time.sleep(1)

    print('\nPROPERTY\n')

    # range
    for i in range(0, len(list_range)):

        print('per_range = ' + str(list_range[i]) + ': ')
        try:
            device.per_range = list_range[i]
        except Exception as e:
            print(e)
        time.sleep(1)

        print('per_range: ')
        try:
            print(device.per_range)
        except Exception as e:
            print(e)
    
    print('rst(): ')
    try: 
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    #reference
    for i in range(0, len(list_ref)):
        
        print('per_ref = ' + str(list_ref[i]) + '): ')
        try:
            device.per_ref = list_ref[i]
        except Exception as e:
            print(e)
        time.sleep(1)

        print('per_ref: ')
        try:
            print(device.per_ref)
        except Exception as e:
            print(e)

    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    # measure
    print('per: ')
    try:
        print(device.per)
    except Exception as e:
        print(e)
        
    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    print('\n-------------------------------\nDIODE\n------------------------------\n')

    # measure
    print('meas(diod): ')
    try:
        print(device.meas(diod))
    except Exception as e:
        print(e)
        
    print('rst(): ')
    try:
        device.rst()  
    except Exception as e:
        print(e)
    time.sleep(1)

    print('\nPROPERTY\n')

    # measure
    print('diod: ')
    try:
        print(device.diod)
    except Exception as e:
        print(e)
        
    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    print('\n-------------------------------\nCONTINUITY\n------------------------------\n')

    # measure
    print('meas(cont): ')
    try:
        print(device.meas(cont))
    except Exception as e:
        print(e)
        
    print('rst(): ')
    try:
        device.rst()  
    except Exception as e:
        print(e)
    time.sleep(1)

    print('\nPROPERTY\n')

    # measure
    print('cont: ')
    try:
        print(device.cont)
    except Exception as e:
        print(e)
        
    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    #close connection
    print('close()')
    try:
        device.close()
    except Exception as e:
        print(e)

    input()












































































