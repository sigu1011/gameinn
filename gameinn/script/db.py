from flask_script import Command
from gameinn import db


class InitDB(Command):
    """create database"""

    def run(self):
        db.create_all()
