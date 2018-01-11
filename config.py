import os

# настройки погоды
pyowm_key = '84295771eb6ed9a21ed8e939df427e93'
pyowm_city = 'Tula, Russia'

class Configuration():
	DEBUG = False
	SECRET_KEY = 'my1_1s1e3c5r6e7t_ke2y'
	
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	RECAPTCHA_PUBLIC_KEY = '6LdYQjoUAAAAAOJ6GUgcEsB_zOiExWgr5ydbRdlT'
	RECAPTCHA_PRIVATE_KEY = '6LdYQjoUAAAAALunleE22arR7qfKU4JGhZkE55gb'
	TESTING = False