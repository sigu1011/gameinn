from pynput import keyboard
from counter.key_counter import key_counter


def on_press(key):
    try:
        # judge the type of key pressed
        pressed_key = key.char
        # pressed alphanumeric key
        key_counter.alphanumeric_increment()
    except AttributeError:
        # pressed special key
        key_counter.special_increment()


def on_release(key):
    pass


def create_key_monitor():
    return keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
