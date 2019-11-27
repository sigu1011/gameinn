import sys
import re
import subprocess
import logging

from exceptions import UnsupportedException

log = logging.getLogger(__name__)


def is_supported_os():
    if sys.platform == 'linux':
        return True
    else:
        log.error("This platform is not Linux. The application cannot be started.")
        raise UnsupportedException(sys.platform)


def get_active_app_name():
    window_id = subprocess.check_output(["xdotool", "getactivewindow"]).decode("utf-8")
    wm_class = subprocess.check_output(["xprop", "-id", window_id, "WM_CLASS"]).decode("utf-8").strip()
    pattern = r'"(.*)", "(.*)"'
    m = re.search(pattern, wm_class)
    if m:
        # group(2) is WM_CLASS. This is application name.
        return m.group(2)
    else:
        return None
