import keyboard
import time
from get_best_position import get_best_position
from get_image import get_image

def drop():
    keyboard.write('kd')
    keyboard.send('enter')
    time.sleep(5)
    get_image()
    match get_best_position():
        case 0:
            time.sleep(.25)
            keyboard.write('+:one:')
        case 1:
            time.sleep(.25)
            keyboard.write('+:two:')
        case 2:
            time.sleep(.25)
            keyboard.write('+:three:')
        case 3:
            time.sleep(.25)
            keyboard.write('+:four:')
    
    keyboard.send('enter')
    keyboard.write('klu')

while True:
    time.sleep(2)
    drop()
    time.sleep(900)
