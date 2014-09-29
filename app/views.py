from flask import render_template, flash, redirect
from app import app
from forms import LoginForm

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('ID="' + form.openid.data + '", remember_me= ' + str(form.remember_me.data))
        return redirect('/index')
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