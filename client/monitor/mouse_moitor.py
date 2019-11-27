from pynput import mouse
from counter.mouse_counter import mouse_counter


def on_move(x, y):
    mouse_counter.move_increment()


def on_click(x, y, button, pressed):
    mouse_counter.click_increment()


def on_scroll(x, y, dx, dy):
    mouse_counter.scroll_increment()


def create_mouse_monitor():
    return mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll)
