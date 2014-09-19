from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'name': 'heesung','age':18, 'address':'korea'}# fake user
    return render_template("index.html", title = 'Home', user = user)
