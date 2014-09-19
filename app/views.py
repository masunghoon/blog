from flask import  render_template
from app import app

@app.route('/name')
def name():
    return "Hello, sunwoo!"


@app.route('/')
@app.route('/index')

def index():
    user = {'nickname': 'sunwoolim', 'age' : 18, 'address' : 'yangpyeong'}
    return render_template("index.html", title = 'home', user = user)

