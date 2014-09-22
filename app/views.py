from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'name':'Jin Shang Hao', 'age' : 18, 'address' : 'Anyang'} # fake user
    posts = [
        {
            'author': {'nickname': 'John' },
            'body': 'Beautiful day in Korea!'
        },
        {
            'author': {'nickname': 'Susan' },
            'body': 'The Myeonryang movie was so cool!'
        }
    ]
    return render_template("index.html",
         title = 'Home',
         user = user,
         posts = posts)