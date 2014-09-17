from app import app

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname':'minwoo!'}
    return render_template("index.html")
