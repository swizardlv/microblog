"""index function"""
from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    """index function"""
    user = {'nickname': 'mike'}
    posts = [
        {'author': {'nickname': 'steve'},
         'body': 'i am cool'},
        {'author': {'nickname': 'trump'},
         'body': 'i am rich'}]
    return render_template("index.html", title='Home', user=user, posts=posts)
