from pynput.keyboard import Key, Controller
import pyscreenshot as ImageGrab
import time

class screenshotBook:

    keyboard = Controller()
    #wait for book to load
    time.sleep(10)
    #screenshot Book
    for i in range(0, 610):
        print(i)
        time.sleep(1)
        im=ImageGrab.grab(bbox=(0,265,1080,1655))
        im.save(f'C:/Users/lcris/Pictures/Screenshots/Essentials_of_Business_Communication_11th_Page {i}.png')
        time.sleep(1)
        #next page
        keyboard.press(Key.right)
        keyboard.release(Key.right)
    print('done')
        
