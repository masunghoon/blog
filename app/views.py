from flask import render_template, flash, redirect, g

from app import app, lm, db
from forms import LoginForm, RegisterForm
from models import User



@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname' : 'Kim' } # fake user
    posts = [
    {
        'author':{ 'nickname' : 'John' },
        'body' : 'Beautiful day in korea!'
     },
    {
        'author':{ 'nickname': 'susan'},
        'body': 'The Myeongryang movie was so cool!'
    }
    ]
    return render_template("index.html", title = 'Home', user = user, posts = posts)



@app.route('/login', methods = ['GET','POST'])
def login():
    user = {'id':'cnsqja6629', 'password':'75695455'}
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if form.email.data == user.email and form.password.data == user.password:
            flash('logged in as ' + form.email.data)
            return redirect('/index')
        else:
            flash('Login Failes!!!')

    return render_template('login.html', title = 'Sign In', form = form)


@app.route('/register', methods = ['GET','POST'])
def register():
    form = RegisterForm()
    user = User()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None:
            flash('E-mail Already exist')
        elif form.password.data != form.valid_password.data:
            flash('Password validation failed')
        else:
            user = User()
            user.email = form.email.data
            user.password = form.password.data
            db.session.add(user)
            db.session.commit()
            return redirect('/login')

    return render_template('register.html', title = 'Register', form = form)