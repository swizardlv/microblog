"""index function"""
from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    """login function"""
    form = LoginForm()
    if form.validate_on_submit():
        flash('login requested by "'+form.openid.data+'",rememberme ="'+str(form.rememberme.data)+'"')
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form, providers=app.config['OPENID_PROVIDERS'])
