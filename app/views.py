from flask import render_template, flash, redirect
from app import app
from forms import LoginForm

@app.route('/login', methods = ['GET','POST'])
def login():
    user = {'id':'kimminwoo','password':'3265aa'}
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
       if form.email.data == user.email and form.password.data == user.password:
           flash('logged in as' + form.id.data)
           return redirect('/index')
       else:
           flash('Login Failed!!')
    return render_template('login.html' , title = 'Sign In', form = form)

@app.route('/register', methods = ['GET','POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
    if user is not None:
        flash('E mail Alredy exists')
    elif form.password.data != form.valid_password.data:
        flash('Password validation failed')
    else:
        user = User()
        user.email = form.email.data
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()
        return redirect('/login')

    return render_template('register.html', title = 'Register', form = form)
