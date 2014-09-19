from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'name':'kimtaesun!','age':18, 'address':'seoul'} #fake user
    return render_template("index.html",
                          title = 'home',
                          user = user)
