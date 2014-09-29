from flask import render_template, flash, redirect
from app import app
from forms import LoginForm

@app.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('ID="'+ form.openid.data+ '", remeber_me='+ str(form.remember_me.data))
        return redirect('/index')
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
