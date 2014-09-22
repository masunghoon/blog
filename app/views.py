from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'kilyunseo'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Korea!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Myeongryang movie was so cool!'
        }
            ]
    return render_template("index.html", title = '', user = user, posts = posts)
