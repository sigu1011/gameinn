from gameinn import db
from datetime import datetime


class Activity(db.Model):
    __tablename__ = 'activities'
    id = db.Column(db.Integer, primary_key=True)
    alphanumeric_key_count = db.Column(db.Integer)
    special_key_count = db.Column(db.Integer)
    keyboard_activity = db.Column(db.Integer)
    mouse_movement = db.Column(db.Integer)
    mouse_click_count = db.Column(db.Integer)
    mouse_scroll_count = db.Column(db.Integer)
    mouse_activity = db.Column(db.Integer)
    active_app_name = db.Column(db.Text)
    created_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', foreign_keys=user_id)

    def __init__(self, alphanumeric_key_count=None, special_key_count=None, keyboard_activity=None, mouse_movement=None,
                 mouse_click_count=None, mouse_scroll_count=None, mouse_activity=None, active_app_name=None,
                 user_id=None):
        self.alphanumeric_key_count = alphanumeric_key_count
        self.special_key_count = special_key_count
        self.keyboard_activity = keyboard_activity
        self.mouse_movement = mouse_movement
        self.mouse_click_count = mouse_click_count
        self.mouse_scroll_count = mouse_scroll_count
        self.mouse_activity = mouse_activity
        self.active_app_name = active_app_name
        self.created_at = datetime.now()
        self.user_id = user_id

    def __repr__(self):
        return '<Activity keyboard_activity:{} mouse_activity:{} active_app_name:{} user_id:{} >'.format(
            self.keyboard_activity, self.mouse_activity, self.active_app_name, self.user_id)
