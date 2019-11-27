import sys
import logging
import logging.handlers
import logging.config

# setting root logger
_root_logger = logging.getLogger('')
_root_logger.setLevel(logging.DEBUG)

# create log formatter
_simpleFormatter = logging.Formatter(
    fmt='%(levelname)-8s %(asctime)s [%(module)s %(funcName)s %(lineno)-4s] %(message)s'
)

# setting console handler
_consoleHandler = logging.StreamHandler(sys.stdout)
_consoleHandler.setLevel(logging.DEBUG)
_consoleHandler.setFormatter(_simpleFormatter)

_root_logger.addHandler(_consoleHandler)

# setting file handler
_fileHandler = logging.handlers.RotatingFileHandler(
    filename='gameinn_client.log', maxBytes=1000000, backupCount=3, encoding='utf-8'
)
_fileHandler.setLevel(logging.INFO)
_fileHandler.setFormatter(_simpleFormatter)

_root_logger.addHandler(_fileHandler)
