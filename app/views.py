from  flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'name': 'Jeonsuhyeon','age':'18','address':'Korea' }
    return  render_template("index.html", title = 'Home', user = user)

