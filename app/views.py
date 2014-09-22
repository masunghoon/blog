from flask import render_template
from app import app

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
