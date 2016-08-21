from flask import Blueprint, render_template

autoExam_blueprint = Blueprint('autoExam', __name__)


@autoExam_blueprint.route('/autoexam')
def index():
    return render_template('autoExam/index.html')
