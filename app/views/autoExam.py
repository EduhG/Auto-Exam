from flask import Blueprint, render_template

autoExam_blueprint = Blueprint('autoexam', __name__)


@autoExam_blueprint.route('/')
def index():
    return render_template('autoexam/index.html')
