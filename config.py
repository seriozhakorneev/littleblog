import os

class Configuration():
	DEBUG = False
	SECRET_KEY = os.urandom(24)
	
	SQLALCHEMY_DATABASE_URI = 'mysql://sql11197214:zg2fdsHiMg@sql11.freemysqlhosting.net/sql11197214'
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	RECAPTCHA_PUBLIC_KEY = '6LdYQjoUAAAAAOJ6GUgcEsB_zOiExWgr5ydbRdlT'
	RECAPTCHA_PRIVATE_KEY = '6LdYQjoUAAAAALunleE22arR7qfKU4JGhZkE55gb'
	TESTING = False # чтобы не вводить капчу каждый раз ставить True