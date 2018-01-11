from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
# роут для редиректа
login_manager.login_view = 'index'
# css для флеш сообщений
login_manager.login_message_category = 'flash_message_red'
# флеш сообщение при редиректе
login_manager.login_message = 'You need to login'