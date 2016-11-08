from flask import Flask
from flask_pymongo import PyMongo
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask('iasasite')
app.config.from_object('config')
mongo = PyMongo(app)
login_manager = LoginManager()
login_manager.init_app(app)
bcrypt = Bcrypt(app)
app.config.from_envvar('FLASK_TEST_SETTINGS', silent=True)

from iasasite import views, models
