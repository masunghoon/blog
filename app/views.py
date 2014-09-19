from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'Kimjaehoon', 'age':18, 'address':'Seoul' }# fake user
    return render_template("Index.html", title = 'Home', user = user)

