from flask import Blueprint, render_template, request, flash, session, url_for, redirect
from forms import SignupForm, SigninForm
from app.models import User
from app import db


home_blueprint = Blueprint('home', __name__)


@home_blueprint.route('/')
def index():
    return render_template('home/index.html')


@home_blueprint.route('/login')
def login():
    form = SigninForm()

    if 'email' in session:
        return redirect(url_for('profile'))

    if request.method == 'POST':
        if form.validate() is False:
            return render_template('signin.html', form=form)
        else:
            session['email'] = form.email.data
            return redirect(url_for('profile'))

    elif request.method == 'GET':
        return render_template('signin.html', form=form)

    # return render_template('home/login.html')


@home_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if 'email' in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        if form.validate() is False:
            return render_template('home/signup.html', form=form)
        else:
            newuser = User(form.username.data, form.email.data, form.password.data)
            db.session.add(newuser)
            db.session.commit()

            session['email'] = newuser.email
            session['username'] = newuser.username

            return redirect(url_for('autoExam.index'))

    elif request.method == 'GET':
        return render_template('home/signup.html', form=form)


@home_blueprint.route('/logout')
def logout():
    return render_template('home/index.html')
