from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname' : 'Kim' } # fake user
    posts = [
    {
        'author':{ 'nickname' : 'John' },
        'body' : 'Beautiful day in korea!'
     },
    {
        'author':{ 'nickname': 'susan'},
        'body': 'The Myeongryang movie was so cool!'
    }
    ]

    return render_template("index.html", title = 'Home', user = user, posts = posts)