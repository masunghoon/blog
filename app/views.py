from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'kang'}
    posts = [
        {
            'author': {'nickname': 'john' },
            'body': 'Beautiful day in korea!'
        },
        {
            'author': { 'nickname':'Susan' },
            'body':'The Myeongryang movie was so cool!'
        }
    ]

    return render_template("index.html",
                           title='Home',
                           user = user,
                           posts = posts)
