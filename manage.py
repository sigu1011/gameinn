from flask_script import  Manager
from gameinn import app

from gameinn.script.db import InitDB

if __name__ == '__main__':
    manager = Manager(app)
    manager.add_command('init_db', InitDB())
    manager.run()
