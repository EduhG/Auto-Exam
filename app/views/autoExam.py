from flask import Blueprint, render_template, request, redirect, url_for, session
from forms import NewStudentForm, Marks, SubjectsForm, ClassesForm
from app.models import Subjects, Forms, Student
from app import db

autoExam_blueprint = Blueprint('autoExam', __name__)


def get_categories():
    subject_list = []
    for subject in db.session.query(Subjects).all():
        subject_list.append((subject.code, subject.name, subject.cartegory))
    return subject_list


def get_forms():
    forms_list = []
    for form in db.session.query(Forms).all():
        forms_list.append((form.code, form.form))
    return forms_list


@autoExam_blueprint.route('/autoexam')
def index():
    return render_template('autoExam/index.html')


@autoExam_blueprint.route('/autoexam/addStudent', methods=['GET', 'POST'])
def addstudent():
    form = NewStudentForm()

    print request.form

    if form.validate_on_submit():
        adm_class = request.form['adm_class']
        stream = request.form['stream']
        gender = request.form['gender']
        firstname = request.form['firstname']
        middlename = request.form['middlename']
        lastname = request.form['lastname']
        regdate = request.form['regdate']
        regnumber = request.form['regnumber']
        marks = request.form['marks']

        if adm_class == '' or stream == '' or firstname == '' or lastname == '' or \
                        regdate == '' or regnumber == '' or marks == '':
            return redirect(url_for('autoExam.addstudent'))

        newstudent = Student(firstname, middlename, lastname, gender, regdate, regnumber, stream, adm_class, marks)
        db.session.add(newstudent)
        db.session.commit()

        return redirect(url_for('autoExam.addstudent'))

    # print 'add student'
    #
    # if request.method == 'POST':
    #     print request.form
    #
    #     form = request.form['form']
    #     stream = request.form['stream']
    #     gender = request.form['gender']
    #
    #     firstname = request.form['firstname']
    #     middlename = request.form['middlename']
    #     lastname = request.form['lastname']
    #     regdate = request.form['regdate']
    #     regnumber = request.form['regnumber']
    #     marks = request.form['marks']
    #
    #     if regform.validate() is False:
    #         return render_template('autoExam/newstudent.html', form=regform, forms=get_forms())
    #     else:
    #         newstudent = Student(regform.firstname, regform.middlename, regform.lastname,
    #                              gender, regform.regdate, regform.regnumber, stream, form, regform.marks)
    #         db.session.add(newstudent)
    #         db.session.commit()
    #
    #         return redirect(url_for('autoExam.addstudent'))
    #
    # elif request.method == 'GET':
    return render_template('autoExam/newstudent.html', form=form, forms=get_forms())


@autoExam_blueprint.route('/autoexam/enterMarks')
def entermarks():
    return render_template('autoExam/entermarks.html', subjects=get_categories())


@autoExam_blueprint.route('/autoexam/reports')
def reports():
    return render_template('autoExam/index.html')


@autoExam_blueprint.route('/autoexam/settings')
def settings():
    return render_template('autoExam/settings.html')


@autoExam_blueprint.route('/autoexam/forms', methods=['GET', 'POST'])
def forms():
    form = ClassesForm()

    if request.method == 'POST':
        if form.validate() is False:
            return render_template('autoExam/forms.html', form=form, forms=get_forms())
        else:
            newclass = Forms(form.code.data, form.name.data)
            db.session.add(newclass)
            db.session.commit()

            return redirect(url_for('autoExam.forms'))

    elif request.method == 'GET':
        return render_template('autoExam/forms.html', form=form, forms=get_forms())


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
