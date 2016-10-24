from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from forms import NewStudentForm, Marks, SubjectsForm, ClassesForm
from app.models import Subjects, Forms, Student
from sqlalchemy import func
import operator
from app import db
import ast

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


def get_students():
    student_list = []
    for student in db.session.query(Student).all():
        student_list.append((student.uid, student.regnumber, student.firstname, student.middlename, student.lastname,
                             student.form, student.stream))
    return student_list


def rank_subjects():
    qry = db.session.query(func.sum(Marks.score).label("total_score"), Marks.code).filter_by(term='Term 1').filter_by(year='2016').filter_by(form='F1')
    qry = qry.group_by(Marks.code)
    qry_result = []
    new_dict = {}
    for _res in qry.all():
        sub_total = {_res[1]: _res[0]}
        qry_result.append(sub_total)
    for row in qry_result:
        for key, value in row.iteritems():
            new_dict[key] = value
            print key, value
    print new_dict

    rank_results = []
    no = 1
    for subject in sorted(new_dict.items(), key=lambda x: (-x[1], x[0])):
        new_rank = {'rank': no, 'code': subject[0], 'marks': subject[1]}
        no += 1
        rank_results.append(new_rank)
    return rank_results


def rank_classes():
    qry = db.session.query(func.sum(Marks.score).label("total_score"), Marks.form).filter_by(term='Term 1').filter_by(year='2016').filter_by(form='F1')
    qry = qry.group_by(Marks.form)
    qry_result = []
    new_dict = {}
    for _res in qry.all():
        sub_total = {_res[1]: _res[0]}
        qry_result.append(sub_total)
    for row in qry_result:
        for key, value in row.iteritems():
            new_dict[key] = value
            print key, value
    print new_dict

    rank_results = []
    no = 1
    for classes in sorted(new_dict.items(), key=lambda x: (-x[1], x[0])):
        new_rank = {'rank': no, 'form': classes[0], 'marks': classes[1]}
        no += 1
        rank_results.append(new_rank)
    return rank_results


def get_student_name(regnumber):
    for user in db.session.query(Student).filter_by(regnumber=regnumber).all():
        return user.firstname + " " + user.middlename + " " + user.lastname


def rank_students():
    qry = db.session.query(func.sum(Marks.score).label("total_score"), Marks.regnumber)\
        .filter_by(term='Term 1').filter_by(year='2016').filter_by(form='F1')
    qry = qry.group_by(Marks.regnumber)
    qry_result = []
    new_dict = {}
    for _res in qry.all():
        sub_total = {_res[1]: _res[0]}
        qry_result.append(sub_total)
    for row in qry_result:
        for key, value in row.iteritems():
            new_dict[key] = value
            print key, value
    print new_dict

    rank_results = []
    no = 1
    for student in sorted(new_dict.items(), key=lambda x: (-x[1], x[0])):
        new_rank = {'rank': no, 'regnumber': student[0], 'fullname': get_student_name(student[0]), 'marks': student[1]}
        no += 1
        rank_results.append(new_rank)
    return rank_results


@autoExam_blueprint.route('/autoexam/search_student')
def reported_cases_search():
    search_results = []

    student_id = request.args.get('student_id')
    print student_id

    for student in db.session.query(Student).filter(Student.regnumber.like('%'+student_id+'%')).all():
        student_details = {
            'regnumber': student.regnumber,
            'fullname': str(student.firstname) + " " + str(student.middlename) + " " + str(student.lastname),
            'form': student.form,
            'stream': student.stream
        }

        search_results.append(student_details)
        print search_results

    response = jsonify(search_results)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@autoExam_blueprint.route('/autoexam/search_marks')
def search_marks():
    search_results = []

    regnumber = request.args.get('student_id').replace(" ", "")
    fullname = request.args.get('fullname')
    term = request.args.get('term')
    year = request.args.get('year')
    form = request.args.get('form')
    merit = ''
    score = 0
    grade = ''

    student_marks = db.session.query(Marks).filter_by(regnumber=regnumber)\
        .filter_by(term=term).filter_by(year=year).filter_by(form=form).all()

    if student_marks:
        pass
    else:
        if regnumber == '' or fullname == '' or term == '' or year == '' or form == '':
            return redirect(url_for('autoExam.addstudent'))

        for subject in db.session.query(Subjects).all():
            new_marks = Marks(regnumber, fullname, term, year, form, merit, subject.name, score, subject.code, grade)
            db.session.add(new_marks)

        db.session.commit()

    for marks in db.session.query(Marks).filter_by(regnumber=regnumber) \
            .filter_by(term=term).filter_by(year=year).filter_by(form=form).all():
        found = {'subject': marks.subject, 'score': marks.score, 'code': marks.code, 'grade': marks.grade}

        search_results.append(found)

    return render_template('autoExam/enterMarksSearch.html', search_results=search_results)


@autoExam_blueprint.route('/autoExam/save_marks_data', methods=['GET', 'POST'])
def save_marks_data():
    new_dict = dict(request.form)

    regnumber = new_dict['student_id'][0]
    term = new_dict['term'][0]
    year = new_dict['year'][0]
    form = new_dict['form'][0]
    table_data = new_dict['table_data']

    new_dd = tuple(table_data)[0]
    my_dictt = ast.literal_eval(new_dd.replace('[', '').replace(']', ''))

    for my_ in my_dictt:
        marks = Marks.query.filter_by(regnumber=regnumber)\
            .filter_by(term=term)\
            .filter_by(year=year)\
            .filter_by(form=form) \
            .filter_by(code=my_['Code']) \
            .update(dict(score=int(my_['Marks']), grade=str(my_['Grade'])))

        print marks

        db.session.commit()

    response = jsonify([])
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@autoExam_blueprint.route('/autoexam')
def index():
    return render_template('autoExam/index.html', rank_subjects=rank_subjects(),
                           rank_classes=rank_classes(), rank_students=rank_students())


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


@autoExam_blueprint.route('/autoexam/listStudents')
def list_students():
    return render_template('autoExam/liststudents.html', students=get_students())


@autoExam_blueprint.route('/autoexam/enterMarks')
def entermarks():
    return render_template('autoExam/entermarks.html', subjects=get_categories(), forms=get_forms())


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


@autoExam_blueprint.route('/autoExam/subject_performance_chart')
def subject_performance_chart():
    ranked_subjects = rank_subjects()

    subject_marks = []

    for subject in ranked_subjects:
        print subject['code']
        for subject_name in db.session.query(Subjects).filter_by(code=subject['code']).all():
            print subject_name.name
            details = {'subject_name': subject_name.name, 'subject_marks': subject['marks']}
            subject_marks.append(details)

    response = jsonify(subject_marks)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@autoExam_blueprint.route('/autoExam/annual_performance_chart')
def annual_performance_chart():
    annual_performance = []

    terms = ['Term 1', 'Term 2', 'Term 3']

    for term in terms:
        termly = {'annual_term': term, 'annual_subjects': total_subjects_termly(term, '2016', 'F1')}
        annual_performance.append(termly)

    print annual_performance

    response = jsonify(annual_performance)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


def total_subjects_termly(term, year, form):
    qry = db.session.query(func.sum(Marks.score).label("total_score"), Marks.code)\
        .filter_by(term=term).filter_by(year=year).filter_by(form=form)
    qry = qry.group_by(Marks.code)
    qry_result = []
    new_dict = {}
    for _res in qry.all():
        sub_total = {_res[1]: _res[0]}
        qry_result.append(sub_total)
    for row in qry_result:
        for key, value in row.iteritems():
            new_dict[key] = value
            print key, value
    print 'printed dict', new_dict

    rank_results = []
    for x in new_dict:
        new_rank = {'code': x, 'marks': new_dict[x]}
        rank_results.append(new_rank)

    # rank_results = []
    # no = 1
    # for subject in sorted(new_dict.items(), key=lambda x: (-x[1], x[0])):
    #     new_rank = {'rank': no, 'code': subject[0], 'marks': subject[1]}
    #     no += 1
    #     rank_results.append(new_rank)
    return rank_results
