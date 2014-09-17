from app import app


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/name')
def name():
    return "Hello, Jaehoon!"