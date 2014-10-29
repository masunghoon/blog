# -*- coding: utf-8 -*-
import re

from flask import render_template, flash, redirect, g, url_for, session
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, lm, db
from forms import LoginForm, RegisterForm, EditForm
from models import User
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
    user = g.user
    # user = { 'nickname': 'Masunghoon' } # fake user
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
        user = user,
        posts = posts)


@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        u = User.query.filter_by(email=form.email.data).first()
        if re.match(r"^[a-zA-Z0-9._]+\@[a-zA-Z0-9._]+\.[a-zA-Z]{3,}$", form.email.data) is None:
            flash('Invalid Email address')
        elif u is not None:
            flash('Already Joined Email')
        elif form.password.data != form.valid_password.data:
            flash('Password Validation Failed.')
        else:
            user = User()
            user.email = form.email.data
            user.password = form.password.data

            nickname = form.email.data.split('@')[0]
            if User.query.filter_by(nickname=nickname).first() == None:
                user.nickname = nickname
            else:
                version = 2
                while True:
                    new_nickname = nickname + str(version)
                    if User.query.filter_by(nickname = new_nickname).first() == None:
                        break
                    version += 1
                user.nickname = new_nickname

            db.session.add(user)
            db.session.commit()

            flash(user.email + ' registered successfully.')
            return redirect('/login')

    return render_template('register.html', title = 'Register', form = form)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    # user = {'id':'masunghoon', 'password':'111111'}
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        user = User.query.filter_by(email=form.email.data).first()

        if user is None:
            flash('Unregistered Email')
        elif form.email.data == user.email and form.password.data == user.password:
            remember_me = False
            if 'remember_me' in session:
                remember_me = session['remember_me']
                session.pop('remember_me', None)
            login_user(user, remember = remember_me)
            return redirect('/index')
            flash(user.email + 'logged in')
        else:
            flash('login failed.')
    return render_template('login.html', title = 'Sign In', form = form)
    # return redirect(url_for('index'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/user/<nickname>')
@login_required
def user(nickname):
    user = User.query.filter_by(nickname=nickname).first()
    if user == None:
        flash('User %s not found.' % nickname)
        return redirect(url_for('index'))
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html',
                           user=user,
                           posts=posts)


@app.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    form = EditForm()
    if form.validate_on_submit():
        g.user.nickname = form.nickname.data
        g.user.about_me = form.about_me.data
        db.session.add(g.user)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit'))
    else:
        form.nickname.data = g.user.nickname
        form.about_me.data = g.user.about_me
    return render_template('edit.html', form=form)


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user
    if g.user.is_authenticated():
        g.user.last_seen = datetime.utcnow()
        db.session.add(g.user)
        db.session.commit()