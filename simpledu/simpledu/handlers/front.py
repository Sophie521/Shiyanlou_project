from flask import Blueprint, render_template
from simpledu.models import Course
from simpledu.forms import LoginForm, RegisterForm
from flask import flash,url_for,redirect
from flask_login import login_user
from flask_login import logout_user,login_required
from simpledu.models import User

front = Blueprint('front',__name__)

@front.route('/')
def index():
    courses = Course.query.all()
    return render_template('index.html',courses = courses)

@front.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        login_user(user, form.remember_me.data)
        return redirect(url_for('.index'))
    return render_template('login.html',form=form)

@front.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash('Amazing~! Register success,please log in', 'success')
        return redirect(url_for('.login'))
    return render_template('register.html',form=form)

@front.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have log out', 'success')
    return redirect(url_for('.index'))
