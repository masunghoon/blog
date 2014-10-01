from flask import render_template, flash, redirect
from app import app
from forms import LoginForm

@app.route('/login', methods = ['GET','POST'])
def login():
    user = {'id':'kimtaesun', 'password':'kim4948'}
    form = LoginForm()
    if form.validate_on_submit():
        if form.id.data ==user['id'] and form.password.data == user['password']:
            flash('logged in as ' + form.id.data)
            return redirect('/index')
        else:
            flash('Login Failed!!!!!!')
    return render_template('login.html', title = 'Log In', form =form)
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'Teasunkim'}
    posts = [
        {
                'author': {'nickname': 'sun'},
                'body': 'Beautiful day in korea!'
        },
        {
              'author': {'nickname':'seoul'},
              'body': 'The nyeongrtang movie was so coll!'
        }
        ]
    return render_template("index.html",
                          title = 'home',
                          user = user,
                          posts = posts)
