from flask import Blueprint, render_template
from forms import Student, Marks

autoExam_blueprint = Blueprint('autoExam', __name__)


@autoExam_blueprint.route('/autoexam')
def index():
    return render_template('autoExam/index.html')


@autoExam_blueprint.route('/autoexam/addStudent')
def addstudent():
    return render_template('autoExam/newstudent.html')


@autoExam_blueprint.route('/autoexam/enterMarks')
def entermarks():
    return render_template('autoExam/entermarks.html')


@autoExam_blueprint.route('/autoexam/reports')
def reports():
    return render_template('autoExam/index.html')


@autoExam_blueprint.route('/autoexam/settings')
def settings():
    return render_template('autoExam/settings.html')


@autoExam_blueprint.route('/autoexam/forms')
def forms():
    return render_template('autoExam/forms.html')


@autoExam_blueprint.route('/autoexam/subjects')
def subjects():
    return render_template('autoExam/subjects.html')
