from flask import Blueprint, render_template, request, redirect, url_for, session
from forms import Student, Marks, SubjectsForm
from app.models import Subjects
from app import db

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


def get_categories():
    subject_list = []
    for subject in db.session.query(Subjects).all():
        subject_list.append((subject.code, subject.name, subject.cartegory))
    return subject_list


@autoExam_blueprint.route('/autoexam/subjects', methods=['GET', 'POST'])
def subjects():

    form = SubjectsForm()

    if request.method == 'POST':
        if form.validate() is False:
            return render_template('autoExam/subjects.html', form=form, subjects=get_categories())
        else:
            newsubject = Subjects(form.code.data, form.name.data, form.cartegory.data)
            db.session.add(newsubject)
            db.session.commit()

            return redirect(url_for('autoExam.subjects'))

    elif request.method == 'GET':
        return render_template('autoExam/subjects.html', form=form, subjects=get_categories())
