from flask import render_template, flash, redirect
from app import app
from forms import LoginForm

from forms import LoginForm

@app.route('/login', methods = ['GET', 'POST'])
def login():
    user = {'id':'kimjungyeul', 'password':'123456'}
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
    user = { 'nickname': 'Masunghoon' } # fake user
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