from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'jaehyeong' , 'age':18, 'address':'korea'} # fake user
    return render_template("index.html",
                           title = 'jaehyeong',
                           user = user)