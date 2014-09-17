from app import  app

@app.route('/')
@app.route('/index')
def index():
    return "Love you Jieun!"

@app.route('/name')
def name():
    return "Hello, Jieun"