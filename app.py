from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from config import Configuration

app = Flask(__name__)

app.config.from_object(Configuration)

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'index'
login_manager.login_message_category = 'flash_message_red'
login_manager.login_message = 'You need to login'