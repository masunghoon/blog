from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = { 'name': 'dongmin','age':18,'address':'korea'}
    return render_template("index.html", title = 'Home', user = user)