from  flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Jsh','name':'Jeonsuhyeon' }
    return  render_template("index.html", title = 'Home', user = user)

