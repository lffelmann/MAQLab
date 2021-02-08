import norma4000 as device
import time

IP = '192.168.0.88'
PORT = 23

if __name__ == '__main__':
    try:
        norma = device.NORMA4000(IP, PORT)
    except Exception as e:
            print(e)

    list_func = ['trms', 'rms', 'mean', 'rmean', 'rmcorr', 'ptp', 'phigh', 'plow', 'har', 'cfac', 'phas',
                    'ffac', 'hcont', 'fcont', 'thd', 'act', 'app', 'reac', 'fact', 'corr', 'eff', 'har',
                    'apphar', 'reachar', 'facthar', 'effhar', 'std', 'ser', 'par', 'serhar', 'parhar']

    list_phase = [1, 2, 3, 12, 13, 23, 31, 123, 130]

    norma.rst()

    try:
        print(norma.id())
    except Exception as e:
                print(e)

    print('watt_meth(2):')
    try:
        norma.watt_meth(2)
    except Exception as e:
            print(e)
    time.sleep(1)

    for i_func in range(0, len(list_func)):
        for i_phase in range(0, len(list_phase)):
            try:
                print('norma.volt(',list_func[i_func],', ',list_phase[i_phase],'):')
                print(norma.volt(list_func[i_func], list_phase[i_phase]))
                print('\n')
            except Exception as e:
                print(e)

    for i_func in range(0, len(list_func)):
        for i_phase in range(0, len(list_phase)):
            try:
                print('norma.curr(',list_func[i_func],', ',list_phase[i_phase],'):')
                print(norma.curr(list_func[i_func], list_phase[i_phase]))
                print('\n')
            except Exception as e:
                print(e)

    for i_func in range(0, len(list_func)):
        for i_phase in range(0, len(list_phase)):
            try:
                print('norma.pwr(',list_func[i_func],', ',list_phase[i_phase],'):')
                print(norma.pwr(list_func[i_func], list_phase[i_phase]))
                print('\n')
            except Exception as e:
                print(e)

    for i_func in range(0, len(list_func)):
        for i_phase in range(0, len(list_phase)):
            try:
                print('norma.phas(',list_func[i_func],', ',list_phase[i_phase],'):')
                print(norma.phas(list_func[i_func], list_phase[i_phase]))
                print('\n')
            except Exception as e:
                print(e)

    for i_func in range(0, len(list_func)):
        for i_phase in range(0, len(list_phase)):
            try:
                print('norma.imp(',list_func[i_func],', ',list_phase[i_phase],'):')
                print(norma.imp(list_func[i_func], list_phase[i_phase]))
                print('\n')
            except Exception as e:
                print(e)

    for i_func in range(0, len(list_func)):
        for i_phase in range(0, len(list_phase)):
            try:
                print('norma.res(',list_func[i_func],', ',list_phase[i_phase],'):')
                print(norma.res(list_func[i_func], list_phase[i_phase]))
                print('\n')
            except Exception as e:
                print(e)

    for i_func in range(0, len(list_func)):
        for i_phase in range(0, len(list_phase)):
            try:
                print('norma.react(',list_func[i_func],', ',list_phase[i_phase],'):')
                print(norma.react(list_func[i_func], list_phase[i_phase]))
                print('\n')
            except Exception as e:
                print(e)

    print('rst():')
    norma.rst()
    print('watt_meth(2):')
    try:
        norma.watt_meth(3)
    except Exception as e:
            print(e)

    time.sleep(1)

    for i_func in range(0, len(list_func)):
        for i_phase in range(0, len(list_phase)):
            try:
                print('norma.volt(',list_func[i_func],', ',list_phase[i_phase],'):')
                print(norma.volt(list_func[i_func], list_phase[i_phase]))
                print('\n')
            except Exception as e:
                print(e)

    for i_func in range(0, len(list_func)):
        for i_phase in range(0, len(list_phase)):
            try:
                print('norma.curr(',list_func[i_func],', ',list_phase[i_phase],'):')
                print(norma.curr(list_func[i_func], list_phase[i_phase]))
                print('\n')
            except Exception as e:
                print(e)

    for i_func in range(0, len(list_func)):
        for i_phase in range(0, len(list_phase)):
            try:
                print('norma.pwr(',list_func[i_func],', ',list_phase[i_phase],'):')
                print(norma.pwr(list_func[i_func], list_phase[i_phase]))
                print('\n')
            except Exception as e:
                print(e)

    for i_func in range(0, len(list_func)):
        for i_phase in range(0, len(list_phase)):
            try:
                print('norma.phas(',list_func[i_func],', ',list_phase[i_phase],'):')
                print(norma.phas(list_func[i_func], list_phase[i_phase]))
                print('\n')
            except Exception as e:
                print(e)

    for i_func in range(0, len(list_func)):
        for i_phase in range(0, len(list_phase)):
            try:
                print('norma.imp(',list_func[i_func],', ',list_phase[i_phase],'):')
                print(norma.imp(list_func[i_func], list_phase[i_phase]))
                print('\n')
            except Exception as e:
                print(e)

    for i_func in range(0, len(list_func)):
        for i_phase in range(0, len(list_phase)):
            try:
                print('norma.res(',list_func[i_func],', ',list_phase[i_phase],'):')
                print(norma.res(list_func[i_func], list_phase[i_phase]))
                print('\n')
            except Exception as e:
                print(e)

    for i_func in range(0, len(list_func)):
        for i_phase in range(0, len(list_phase)):
            try:
                print('norma.react(',list_func[i_func],', ',list_phase[i_phase],'):')
                print(norma.react(list_func[i_func], list_phase[i_phase]))
                print('\n')
            except Exception as e:
                print(e)

    print('close')
    try:
        norma.close()
    except Exception as e:
        print(e)

    input()