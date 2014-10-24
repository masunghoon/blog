from flask import render_template, flash, redirect, g
from flask.ext.login import login_user, logout_user
from app import app, lm, db
from forms import LoginForm, RegisterForm
from models import User

@app.route('/login', methods = ['GET', 'POST'])
def login():
    user = {'id':'aaa','password':'123'}
    form = LoginForm()
    if form.validate_on_submit():

        if form.id.data == user['id'] and form.password.data == user['password']:
            flash('logged in as ' + form.id.data)
            return redirect('/index')
        else:
            flash('Login Failed!')
    return render_template('login.html', title = 'Sign in', form = form)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None:
            flash('E-mail Already exists')
        elif form.password.data != form.valid_password.data:
            flash('password validation failed')
        else:
            user = User()
            user.email = form.email.data
            user.password = form.password.data
            db.session.add(user)
            db.session.commit()
            return redirect('/login')

    return render_template('register.html', title = 'Register', form = form)

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'kilyunseo'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Korea!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Myeongryang movie was so cool!'
        }
            ]
    return render_template("index.html", title = '', user = user, posts = posts)