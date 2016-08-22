from flask import Blueprint, render_template, request, flash, session, url_for, redirect
from forms import SignupForm

home_blueprint = Blueprint('home', __name__)


@home_blueprint.route('/')
def index():
    return render_template('home/index.html')


@home_blueprint.route('/login')
def login():
    return render_template('home/login.html')


@home_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if 'email' in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        if form.validate() is False:
            return render_template('home/signup.html', form=form)
        else:
            return redirect(url_for('index'))

    elif request.method == 'GET':
        return render_template('home/signup.html', form=form)


@home_blueprint.route('/logout')
def logout():
    return render_template('home/index.html')
