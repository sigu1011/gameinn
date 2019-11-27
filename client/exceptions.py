class UnsupportedException(Exception):
    def __init__(self, os_name):
        super().__init__()
        self._name = os_name

    def __str__(self):
        return 'This Operating System {0} is not supported.'.format(self._name)
