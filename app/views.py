from flask import  render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'saewoong'}
    return render_template("index.html", title = 'home', user = user)

