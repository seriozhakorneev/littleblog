import os

# настройки погоды
pyowm_key = ''
pyowm_city = ''

class Configuration():
	DEBUG = False
	SECRET_KEY = ''
	
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	RECAPTCHA_PUBLIC_KEY = ''
	RECAPTCHA_PRIVATE_KEY = ''
	TESTING = False