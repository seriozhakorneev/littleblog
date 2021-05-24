from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, RadioField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Email, Length


class LoginForm(FlaskForm):
	'''форма логина'''
	username = StringField('Username', 
		validators=[InputRequired('username is required')])

	password = PasswordField('Password', 
		validators=[InputRequired('password is required')])

	recaptcha = RecaptchaField()

	remember = BooleanField('Remember me')

class RegisterForm(FlaskForm):
	'''форма регистрации'''
	
	username = StringField('Name', 
		validators=[InputRequired('username is required'),
		Length(min=4, max=20, message='must be between 4 and 20 characters')])

	email = StringField('Email', 
		validators=[InputRequired('email is required'),
		Email(message='invalid email')])

	password = PasswordField('Password', 
		validators=[InputRequired('password is required'),
		Length(min=4, max=20, message='must be between 4 and 20 characters')])

	confirm_password = PasswordField('Confirm Password', 
		validators=[InputRequired('confirm password is required'),
		Length(min=4, max=20, message='must be between 4 and 20 characters')])

	radios = RadioField('Radios', default='Male', 
		choices=[('Male','Male'),('Female', 'Female')])

	selects = SelectField('Select', choices=[
		('Comrade','Comrade'),
		('Seniore','Seniore'),
		('Messieurs','Messieurs')])

	textarea = TextAreaField('About')

	recaptcha = RecaptchaField()


class BlogPost(FlaskForm):
	'''форма добавления постов'''
	
	title = StringField('Title', 
		validators=[InputRequired('title is required'),
		Length(min=3, max=50, message='must be between 4 and 50 characters')])

	subtitle = TextAreaField('Subtitle')

	content = TextAreaField('Post content', 
		validators=[InputRequired('content is required')])

	recaptcha = RecaptchaField()