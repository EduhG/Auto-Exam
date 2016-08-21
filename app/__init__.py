from flask import Flask
from .views.home import home_blueprint
from .views.profile import profile_blueprint

app = Flask(__name__)

app.register_blueprint(home_blueprint)
app.register_blueprint(profile_blueprint)

app.config.from_pyfile('config.py')
