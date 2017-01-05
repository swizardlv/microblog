"""index function"""
from flask import render_template
from app import app
@app.route('/')
@app.route('/index')
def index():
    """index function"""
    user = {'nickname' : 'mike'}
    return render_template("index.html", title='Home', user=user)
