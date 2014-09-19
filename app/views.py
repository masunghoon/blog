from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'kilyunseo', 'age': 17, 'address': 'ansan'}
    return render_template("index.html", title = 'home', user = user)
