from iasasite import app, mongo, bcrypt, LoginManager
from iasasite.models import Post, User
from datetime import datetime as dt
from flask_login import login_user, logout_user
from flask import session, render_template, request, redirect, url_for, flash
import json

@app.route('/', methods = ['POST', 'GET'])
def index():
	posts = list(mongo.db.posts.find({}))[:6]
	News = json.dumps([Post(e).toJson() for e in posts])
	return render_template('index.html', News=News)

@app.route('/news/<_id>')
def news(_id):
	post = json.dumps(Post(mongo.db.posts.find({'_id': _id})).toJson())
	return render_template('posts.html', post=post)

@app.route('/user/<_id>/')
def user(_id):
	user = json.dumps(User(mongo.db.users.find({'_id': _id})).toJson())
	return render_template('user.html', user=user)

@app.route('/signup/')
def signup():
	if request.method == 'POST' and request.json:
		data = request.json
		user = mongo.db.users.find({'email': data['email']})
		if user and User.validate_login(user['password'], data['password']):
			currentUser = User(user)
			login_user(currentUser)
			flash("Logged in successfully", category='success')
			print("Logged in successfully")
			return redirect('/')
		flash("Wrong username or password", category='error')
		error = 'Wrong username or password'
		return json.dumps({'error': error})
	return render_template('login.html')
