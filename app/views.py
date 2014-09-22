from flask import  render_template
from app import app

@app.route('/name')
def name():
    return "Hello, sunwoo!"


@app.route('/')
@app.route('/index')

def index():
    user = {'nickname': 'sunwoolim'}
    posts = [
        {
            'author':{'nickname': 'john'},
             'body': 'beautiful day in Korea!'
        },
        {
            'author':{'nickname':'Susan'},
            'body': 'The Myeongryang movie was so cool!'
        }
    ]
    return render_template("index.html", title = 'home', user = user, posts = posts)

