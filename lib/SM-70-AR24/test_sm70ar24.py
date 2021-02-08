import sm70ar24 as sm
import time

IP_ADD = '172.16.65.115'
PORT = 8462

if __name__ == '__main__':

    volt = sm.FUNC_VOLT
    curr = sm.FUNC_CURR
    pwr  = sm.FUNC_PWR

    try:
        device = sm.SM70AR24(IP_ADD, PORT)
    except Exception as e:
            print(e)

    print('id(): ')
    try:
        print(device.id())
    except Exception as e:
        print(e)

    print('\n-------------------------------\nRESET\n------------------------------\n')

    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    print('set_max_out(volt, 70): ')
    try:
        device.set_max_out(volt, 70)
    except Exception as e:
        print(e)
    time.sleep(1)

    print('get_max_out(volt): ')
    try:
        print(device.get_max_out(volt))
    except Exception as e:
        print(e)

    print('set_max_value(curr, 24): ')
    try:
        device.set_max_out(curr, 24)
    except Exception as e:
        print(e)
    time.sleep(1)

    print('get_max_value(curr): ')
    try:
        print(device.get_max_out(curr))
    except Exception as e:
        print(e)

    print('\n-------------------------------\nVOLTAGE\n------------------------------\n')

    print('set_out(volt, 20): ')
    try:
        device.set_out(volt, 20)
    except Exception as e:
        print(e)
    time.sleep(1)

    print('get_out(volt): ')
    try:
        print(device.get_out(volt))
    except Exception as e:
        print(e)

    print('meas(volt): ')
    try:
        print(device.meas(volt))
    except Exception as e:
        print(e)

    print('\nPROPERTY\n')

    print('volt_out = 24: ')
    try:
        device.volt_out = 20
    except Exception as e:
        print(e)
    time.sleep(1)

    print('volt_out: ')
    try:
        print(device.volt_out)
    except Exception as e:
        print(e)

    print('volt: ')
    try:
        print(device.volt)
    except Exception as e:
        print(e)

    print('\n-------------------------------\nRESET\n------------------------------\n')

    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    print('set_max_out(volt, 70): ')
    try:
        device.set_max_out(volt, 70)
    except Exception as e:
        print(e)
    time.sleep(1)

    print('get_max_out(volt): ')
    try:
        print(device.get_max_out(volt))
    except Exception as e:
        print(e)

    print('set_max_value(curr, 24): ')
    try:
        device.set_max_out(curr, 24)
    except Exception as e:
        print(e)
    time.sleep(1)

    print('get_max_value(curr): ')
    try:
        print(device.get_max_out(curr))
    except Exception as e:
        print(e)

    print('\n-------------------------------\nCURRENT\n------------------------------\n')

    print('set_value(curr, 2): ')
    try:
        device.set_out(curr, 2)
    except Exception as e:
        print(e)
    time.sleep(1)

    print('get_value(curr): ')
    try:
        print(device.get_out(curr))
    except Exception as e:
        print(e)

    print('meas(curr): ')
    try:
        print(device.meas(curr))
    except Exception as e:
        print(e)

    print('\nPROPERTY\n')

    print('curr_out = 1: ')
    try:
        device.curr_out = 1
    except Exception as e:
        print(e)
    time.sleep(1)

    print('curr_out: ')
    try:
        print(device.curr_out)
    except Exception as e:
        print(e)

    print('curr: ')
    try:
        print(device.curr)
    except Exception as e:
        print(e)

    print('\n-------------------------------\nRESET\n------------------------------\n')

    print('rst(): ')
    try:
        device.rst()
    except Exception as e:
        print(e)
    time.sleep(1)

    print('volt_max_out = 70: ')
    try:
        device.volt_max_out = 70
    except Exception as e:
        print(e)
    time.sleep(1)
    
    print('volt_max_out: ')
    try:
        print(device.volt_max_out)
    except Exception as e:
        print(e)

    print('curr_max_out = 24: ')
    try:
        device.curr_max_out = 24
    except Exception as e:
        print(e)
    time.sleep(1)

    print('curr_max_out: ')
    try:
        print(device.curr_max_out)
    except Exception as e:
        print(e)

    print('\n-------------------------------\nPOWER\n------------------------------\n')

    print('volt_out = 24: ')
    try:
        device.volt_out = 20
    except Exception as e:
        print(e)
    time.sleep(1)

    print('meas(pwr): ')
    try:
        print(device.meas(pwr))
    except Exception as e:
        print(e)

    print('\nPROPERTY\n')

    print('pwr: ')
    try:
        print(device.pwr)
    except Exception as e:
        print(e)

    input()