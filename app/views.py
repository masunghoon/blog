from datetime import datetime

import re
from flask import render_template, flash, redirect, g, session, url_for
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, lm, db
from app.forms import LoginForm, RegisterForm, EditForm
from models import User
@app.route('/login', methods = ['GET', 'POST'])
def login():
    # user = {'id':'tlsehdals222', 'password':'123456'}
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
            flash('Login Failed!!!!!')
    return render_template('login.html', title = 'Sign In', form = form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/')
@app.route('/index')
def index():
    user = g.user
   # user = { 'nickname': 'dongmin' }
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
@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if re.match(r"^[a-zA-Z0-9._]+\@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}$", form.email.data) is None:
            flash('Invalid Email address')
        elif user is not None:
            flash('already Joined Email')
        elif form.password.data != form.valid_password.data:
            flash('Password validation failed')
        else:
            user = User()
            user.email = form.email.data
            user.password = form.password.data

            nick = form.email.data.split('@')[0]
            if User.query.filter_by(nickname=nick).first() == None:
                user.nickname = nick
            else:
                version = 1
                while True:
                    new_nickname = nick + str(version)
                    if User.query.filter_by(nickname = new_nickname).first() == None:
                        break
                    version += 1
                user.nickname = new_nickname

            db.session.add(user)
            db.session.commit()

            flash(user.email + ' registered successfully.')
            return redirect('/login')

    return render_template('register.html',title = 'Register',form = form)

@app.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    form = EditForm(g.user.nickname)
    if form.validate_on_submit():
        g.user.nickname = form.nickname.data
        g.user.about_me = form.about_me.data
        db.session.add(g.user)
        db.session.commit()
        flash('Your changes have been saves.')
        return redirect(url_for('edit'))
    else:
        form.nickname.data = g.user.nickname
        form.about_me.data = g.user.about_me
    return render_template('edit.html', form=form)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500



#
#
# @lm.user_loader
# def load_user(id):
#     return User.query.get(int(id))