from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	posts = [{'author': {'username': 'BotenAqua'}, 'body': 'What a nice site!'},
		{'author': {'username': 'NotAqua'}, 'body': "Don't eat yellow sand..."}]

	return render_template('index.html', user = 'Aqua', posts = posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
		return redirect('/index')
	return render_template('login.html', title='Sign In', form=form)
