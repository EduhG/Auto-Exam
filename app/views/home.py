from flask import Blueprint, render_template

home_blueprint = Blueprint('home', __name__)


@home_blueprint.route('/')
def index():
    return render_template('home/index.html')


@home_blueprint.route('/login')
def login():
    return render_template('home/login.html')


@home_blueprint.route('/signup')
def signup():
    return render_template('home/signup.html')


@home_blueprint.route('/logout')
def logout():
    return render_template('home/index.html')
