import os

class Configuration():
	DEBUG = False
	SECRET_KEY = os.urandom(24)
	
	SQLALCHEMY_DATABASE_URI = 'mysql://sql11197214:zg2fdsHiMg@sql11.freemysqlhosting.net/sql11197214'
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	RECAPTCHA_PUBLIC_KEY = '6LfWbjcUAAAAAEB9807KCCe-nxl8NystpF3U1Kn4'
	RECAPTCHA_PRIVATE_KEY = '6LfWbjcUAAAAANk8w5UP-76KOgiJ6bK-RaVqDtSE'
	TESTING = False # чтобы не вводить капчу каждый раз ставить True