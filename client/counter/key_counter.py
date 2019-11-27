import threading

__all__ = ['key_counter']


class KeyCounter:
    def __init__(self, alphanumeric=0, special=0):
        self._alphanumeric = alphanumeric
        self._special = special
        self._lock = threading.RLock()

    def alphanumeric_increment(self):
        with self._lock:
            self._alphanumeric += 1
            return self._alphanumeric

    def special_increment(self):
        with self._lock:
            self._special += 1
            return self._special

    def reset(self):
        with self._lock:
            self._alphanumeric = 0
            self._special = 0
            return

    @property
    def alphanumeric(self):
        with self._lock:
            return self._alphanumeric

    @property
    def special(self):
        with self._lock:
            return self._special


key_counter = KeyCounter()
