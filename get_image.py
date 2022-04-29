import time
import mouse
from tkinter import Tk
import subprocess

def get_image():
    mouse.move(2200, 1100)
    mouse.click('right')
    time.sleep(.1)
    mouse.move(2300, 1315)
    mouse.click()
    link = Tk().clipboard_get()
    bash = f"curl {link} -o images/card.png"
    subprocess.run(bash) 
    
    
#get_image()
