from flask_sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(120), unique=True)
    pwdhash = db.Column(db.String(54))

    def __init__(self, username, email, password):
        self.username = username.title()
        self.email = email.lower()
        self.set_password(password)

    def set_password(self, password):
        self.pwdhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)


class Student(db.Model):
    __tablename__ = 'students'

    uid = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100))
    middlename = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    gender = db.Column(db.String(6))
    regdate = db.Column(db.String(20))
    regnumber = db.Column(db.String(10))
    form = db.Column(db.String(20))
    stream = db.Column(db.String(20))
    marks = db.Column(db.Integer)

    def __init__(self, firstname, middlename, lastname, gender, regdate, regnumber, stream, form, marks):
        self.firstname = firstname.title()
        self.middlename = middlename.title()
        self.lastname = lastname.title()
        self.gender = gender.title()
        self.regdate = regdate.title()
        self.regnumber = regnumber.title()
        self.stream = stream.title()
        self.form = form.title()
        self.marks = marks


class Marks(db.Model):
    __tablename__ = 'marks'

    uid = db.Column(db.Integer, primary_key=True)
    regnumber = db.Column(db.String(100))
    fullname = db.Column(db.String(100))
    term = db.Column(db.String(100))
    year = db.Column(db.String(100))
    merit = db.Column(db.String(100))
    subject = db.Column(db.String(100))
    score = db.Column(db.Integer)

    def __init__(self, regnumber, fullname, term, year, merit, subject, score):
        self.regnumber = regnumber.title()
        self.fullname = fullname.title()
        self.term = term.title()
        self.year = year.title()
        self.merit = merit.title()
        self.subject = subject.title()
        self.score = score
