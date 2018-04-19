from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, Email, EqualTo, Required


class RegisterForm(FlaskForm):
    username = StringField('username', validators=[Required(), Length(3, 24)])
    email = StringField('email', validators=[Required(), Email()])
    password = PasswordField('password', validators=[Required(), Length(6, 24)])
    repeat_password = PasswordField('password again', validators=[Required(), EqualTo('password')])
    submit = SubmitField('submit')


class LoginForm(FlaskForm):
    email = StringField('email', validators=[Required(), Email()])
    password = PasswordField('password', validators=[Required(), Length(6, 24)])
    remember_me = BooleanField('password again')
    submit = SubmitField('submit')

