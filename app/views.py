# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, g
from flask.ext.login import login_user, logout_user
from app import app, lm, db
from forms import LoginForm, RegisterForm
from models import User

@app.route('/')
@app.route('/index')
def index():
    g.user = { 'nickname': 'Masunghoon' } # fake user
    posts = [ # fake array of posts
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Korea!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Myeongryang movie was so cool!'
        }
    ]
    return render_template("index.html",
        title = 'Home',
        user = g.user,
        posts = posts)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    user = {'id':'masunghoon', 'password':'111111'}
    if form.validate_on_submit():
        if form.id.data == user['id'] and form.password.data == user['password']:
            g.user = user
            flash(form.id.data + 'logged in')
            return redirect('/index')
        else:
            flash('login failed.')
    return render_template('login.html', title = 'Sign In', form = form)


@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    user = User()
    if form.validate_on_submit():
        user.email = form.email.data
        user.password = form.password.data

        db.session.add(user)
        db.session.commit()

    return render_template('register.html', title = 'Register', form = form)



@lm.user_loader
def load_user(id):
    return User.query.get(int(id))