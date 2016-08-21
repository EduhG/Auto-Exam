from flask import Blueprint, render_template

home_blueprint = Blueprint('home', __name__)


@home_blueprint.route('/')
def index():
    return render_template('home/index.html')


@home_blueprint.route('/login')
def login():
    print 'user loging in'
    return render_template('home/login.html')


@home_blueprint.route('/signup')
def signup():
    return render_template('home/signup.html')
