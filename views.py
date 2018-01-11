from app import app, db, login_manager
from flask import render_template, redirect, url_for, flash, request, session
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from get_weather import get_weather_info
from models import *
from forms import *
import threading
import time

weather = get_weather_info()

def redirect_url(default='index'):
	'''редирект для роута logout'''

	return request.args.get('next') or \
           request.referrer or \
           url_for(default)

def check_login_for_posts_length():
	'''проверка авторизации для строки кол-ва постов Posts'''

	user_posts = []
	if current_user.is_authenticated:
		user_posts = Post.query.filter_by(post_author=current_user.username).all()	
	return user_posts

def login():
	'''проверка данных,логин в сессию'''
	
	form_login = LoginForm()
	# проверка наличия username
	username = User.query.filter_by(username=form_login.username.data).first()
	if username:
		# проверка пароля
		if check_password_hash(username.password, form_login.password.data):
			# логин
			login_user(username, remember=form_login.remember.data)
			return True

		flash('Password incorect', category='flash_message_red')
		return False
		
	flash('Username not found', category='flash_message_red')
	return False

def register():
	'''проверка данных,регистрация'''

	form = RegisterForm()
	# проверка username и email на уникальность в бд
	username = User.query.filter_by(username=form.username.data).first()
	email = User.query.filter_by(email=form.email.data).first()
	if not username:
		if not email:
			# проверка двух password-полей
			if form.password.data == form.confirm_password.data:
				# хеширование пароля и добавление нового пользователя
				hashed_password = generate_password_hash(form.password.data, method='sha256')
				new_user = User(username=form.username.data, email=form.email.data, password=hashed_password,
								sex=form.radios.data, appeal=form.selects.data, about=form.textarea.data)
				db.session.add(new_user)
				db.session.commit()
				flash('User has been created', category='flash_message_green')
				return True

			flash('Passwords are not equal', category='flash_message_red')
			return False

		flash('Email is already in use', category='flash_message_red')
		return False	

	flash('Username is already in use', category='flash_message_red')
	return False

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

@app.before_first_request
def weather_info():
	'''получаем погоду каждые 3 часа'''
	
	def run():
		global weather
		while True:
			weather = get_weather_info()
			time.sleep(10800) # 3 часа
	
	thread = threading.Thread(target=run)
	thread.start()

@app.before_request
def make_session_permanent():
	'''сброс неактивной сессии'''
	
	session.permanent = True
	app.permanent_session_lifetime = timedelta(minutes=40)

@app.errorhandler(404)
def error(error):
	time = datetime.now()
	return render_template('404.html', time=time, weather=weather), 404

@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(redirect_url())

@app.route('/', defaults={'view_form': 'sign_in', 'slice1': 0, 'slice2': 4}, methods=['GET', 'POST'])
@app.route('/<string:view_form>/<int:slice1>/<int:slice2>', methods=['GET', 'POST'])
def index(view_form, slice1, slice2):
	'''главная страница'''
	
	time = datetime.now()
	posts = Post.query.order_by(Post.date_posted.desc()).slice(slice1,slice2)
	all_posts = Post.query.all()
	user_posts = check_login_for_posts_length()
	form_login = LoginForm()
	form_signup = RegisterForm()
	
	if view_form == 'sign_in':
		# корректность заполнения формы
		if form_login.validate_on_submit():
			if login():
				return redirect(url_for('index', view_form='sign_in', slice1=slice1, slice2=slice2))

		return render_template('index.html', view_form=view_form, weather=weather, time=time,
											form_login=form_login, posts=posts, all_posts=all_posts,
											user_posts=user_posts, slice1=slice1, slice2=slice2)
	else:
		if form_signup.validate_on_submit():
			if register():
				return redirect(url_for('index', view_form='sign_in', slice1=slice1, slice2=slice2))
		
		return render_template('index.html', view_form=view_form, weather=weather, time=time,
											form_signup=form_signup, posts=posts, all_posts=all_posts,
											slice1=slice1, slice2=slice2)


@app.route('/post/<int:post_id>', defaults={'view_form': 'sign_in'} ,methods=['GET', 'POST'])
@app.route('/post/<string:view_form>/<int:post_id>', methods=['GET', 'POST'])
def post(post_id, view_form):
	'''страница поста'''
	
	time = datetime.now()
	posts = Post.query.order_by(Post.date_posted.desc()).all()
	post = Post.query.filter_by(id=post_id).one()
	author = User.query.filter_by(username=post.post_author).first()
	user_posts = check_login_for_posts_length()
	form_login = LoginForm()
	form_signup = RegisterForm()
	
	if view_form == 'sign_in':
		if form_login.validate_on_submit():
			if login():
				return redirect(url_for('post', post_id=post.id))
		
		return render_template('post.html', view_form=view_form, form_login=form_login, posts=posts,
								post=post, user_posts=user_posts, weather=weather, time=time, author=author)
	else:
		if form_signup.validate_on_submit():
			if register():
				return redirect(url_for('post', post_id=post.id))
		
		return render_template('post.html', view_form=view_form, form_signup=form_signup, posts=posts,
								post=post, user_posts=user_posts, weather=weather, time=time, author=author)


@app.route('/user_posts/<int:slice1>/<int:slice2>')
@login_required
def user_posts(slice1, slice2):
	'''все посты пользователя'''

	time = datetime.now()
	view_posts = Post.query.filter_by(post_author=current_user.username).order_by(Post.date_posted.desc()).slice(slice1,slice2)
	user_posts = check_login_for_posts_length()
	return render_template('user_posts.html', user=current_user, user_posts=user_posts,time=time,
							weather=weather,view_posts=view_posts,slice1=slice1,slice2=slice2)


@app.route('/add_post/<int:slice1>/<int:slice2>', methods=['GET', 'POST'])
@login_required
def add_post(slice1, slice2):
	'''страница добавления поста'''
	
	time = datetime.now()
	posts = Post.query.order_by(Post.date_posted.desc()).slice(slice1,slice2)
	all_posts = Post.query.all()
	form_blog = BlogPost()
	if form_blog.validate_on_submit():
		# добавление нового поста
		new_post = Post(title=form_blog.title.data,subtitle=form_blog.subtitle.data,content=form_blog.content.data,
						date_posted=datetime.now(),post_author=current_user.username)
		db.session.add(new_post)
		db.session.commit()
		return redirect(url_for('index'))

	return render_template('add_post.html', slice1=slice1, slice2=slice2, weather=weather,
							time=time, form_blog=form_blog, posts=posts, all_posts=all_posts)