from app import app

@app.route('/')
@app.route('/index')
def index():
    return "hello, world!"

@app.route('/name')
def name():
    return "Hello, dongmin"