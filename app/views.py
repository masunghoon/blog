from flask import render_template, flash, redirect
from app import app
from forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Guest' } # fake user
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


@app.route('/login', methods = ['GET', 'POST'])
def login():
    user = {'id':'wr8484', 'password':'123456'}
    form = LoginForm()
    if form.validate_on_submit():
        if user['id'] == form.id.data and user['password'] == form.password.data:
            flash('logged in as ' + form.id.data)
            return redirect('/index')
        else:
            flash('login Failed!!!!!')
    return render_template('login.html', title = 'Sign In', form = form)