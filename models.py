from flask_login import UserMixin
from app import db

class User(UserMixin, db.Model):
	'''таблица пользователей'''
	
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True)
	email = db.Column(db.String(20), unique=True)
	password = db.Column(db.String(100))
	sex = db.Column(db.String(6))
	appeal = db.Column(db.String(10))
	about = db.Column(db.String(50))
	posts = db.relationship('Post', backref='author', lazy='dynamic')

class Post(db.Model):
	'''таблица постов'''
	
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(50))
	subtitle = db.Column(db.String(50))
	content = db.Column(db.Text)
	date_posted = db.Column(db.DateTime)
	post_author = db.Column(db.String(20), db.ForeignKey('user.username'))