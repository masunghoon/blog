# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, g
from app import app
from forms import LoginForm

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