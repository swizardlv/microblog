"""import flask_wtf instead of flask.ext.wtf"""
from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import data_required


class LoginForm(Form):
    """define class"""
    openid = StringField('openid', validators=[data_required()])
    rememberme = BooleanField('rememberme', default=False)
