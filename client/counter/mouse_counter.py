import threading

__all__ = ['mouse_counter']


class MouseCounter:
    def __init__(self, movement=0, click=0, scroll=0):
        self._movement = movement
        self._click = click
        self._scroll = scroll
        self._lock = threading.RLock()

    def move_increment(self):
        with self._lock:
            self._movement += 1
            return self._movement

    def click_increment(self):
        with self._lock:
            self._click += 1
            return self._click

    def scroll_increment(self):
        with self._lock:
            self._scroll += 1
            return self._scroll

    def reset(self):
        with self._lock:
            self._movement = 0
            self._click = 0
            self._scroll = 0
            return

    @property
    def movement(self):
        with self._lock:
            return self._movement

    @property
    def click(self):
        with self._lock:
            return self._click

    @property
    def scroll(self):
        with self._lock:
            return self._scroll


mouse_counter = MouseCounter()
