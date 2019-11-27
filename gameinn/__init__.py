import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('gameinn.config')

db = SQLAlchemy(app)

with open(app.config['SCHEMA_PATH']) as f:
    activity_schema = json.load(f)

from gameinn.views.activities import activity
from gameinn.views.users import user

app.register_blueprint(activity, url_prefix='/user')
app.register_blueprint(user)

from gameinn.views import views
