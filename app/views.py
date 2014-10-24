from flask import render_template, flash, redirect, g
from flask.ext.login import login_user, logout_user
from app import app, db
from forms import LoginForm, RegisterForm
from models import User

@app.route('/login', methods = ['GET', 'POST'])
def login():
    # user = {'id':'tlsehdals222', 'password':'123456'}
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if form.email.data == user.email and form.password.data == user.password:
            g.user = user
            flash(form.email.data + 'logged in')
            return redirect('/index')
        else:
            flash('Login Failed!!!!!')
    return render_template('login.html', title = 'Sign In', form = form)

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'dongmin' }
    posts = [
        {
            'author': { 'nickname':'john' },
            'body': 'Beautiful day in korea!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'the Myeongrayang movie was so cool!'
        }
    ]
    return render_template("index.html",
        title = 'Home',
        user = user,
        posts = posts)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    user = User()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            flash('E-mail Already exist')
        if form.password.data != form.valid_password.data:
            flash('Password validation failed')
        else:
            user = User()
            user.email = form.email.data
            user.password = form.password.data
            db.session.add(user)
            db.session.commit()
            return redirect('/login')

    return render_template('register.html',title = 'Register',form = form)

#
#
# @lm.user_loader
# def load_user(id):
#     return User.query.get(int(id))