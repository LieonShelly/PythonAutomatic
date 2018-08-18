import logging

logging.basicConfig(filename ='mylog.md', level = logging.DEBUG, format = ' %(asctime)s - %(levelname)s - %(message)s' )
logging.debug('Start of program')

def boxPrint(symbol, width ,height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character sing.')
    if width <= 2:
        raise Exception('Width must be greater than 2')
    if height <= 2:
        raise Exception('Height must be greater than 2.')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)


def spam():
    bacon()

def bacon():
    raise Exception('This is the error message')

def assetiosn():
    podBayDoorStatus = 'open'
    assert podBayDoorStatus == 'open', 'The pod bay door need to be open'

def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
             stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
    assert 'red' in stoplight.values(), 'Neither light is red!' + str(stoplight)


def factorial(n):
    logging.debug('Start of factorial(%s%%)' % (n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)' % (n))
    logging.disable(logging.DEBUG)
    return total

if __name__ == '__main__':
    for sysm, w, h in (('*', 4, 4), ('0', 20, 5), ('x', 1, 3), ('zz', 3, 3)):
        try: 
            boxPrint(sysm, w, h)
        except Exception as err:
            print('An exceptiom happened: '+ str(err))

