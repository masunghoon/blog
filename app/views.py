from flask import render_template, flash, redirect
from app import app
from forms import LoginForm

@app.route('/login', methods = ['GET', 'POST'])
def login():
    user = {'id':'tlsehdals222', 'password':'123456'}
    form = LoginForm()
    if form.validate_on_submit():
        if form.id.data == user['id'] and form.password.data == user['password']:
            flash('logged in as ' + form.id.data)
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