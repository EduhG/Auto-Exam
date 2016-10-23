from werkzeug.security import generate_password_hash, check_password_hash
from . import db


class User(db.Model):
    __tablename__ = 'users'

    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(120), unique=True)
    pwdhash = db.Column(db.String(255))

    def __init__(self, username, email, password):
        self.username = username
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
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.gender = gender
        self.regdate = regdate
        self.regnumber = regnumber
        self.stream = stream
        self.form = form
        self.marks = marks


class Marks(db.Model):
    __tablename__ = 'marks'

    uid = db.Column(db.Integer, primary_key=True)
    regnumber = db.Column(db.String(100))
    fullname = db.Column(db.String(100))
    term = db.Column(db.String(100))
    year = db.Column(db.String(100))
    form = db.Column(db.String(100))
    merit = db.Column(db.String(100))
    code = db.Column(db.String(100))
    subject = db.Column(db.String(100))
    score = db.Column(db.Integer)
    grade = db.Column(db.String(100))

    def __init__(self, regnumber, fullname, term, year, form, merit, subject, score, code, grade):
        self.regnumber = regnumber
        self.fullname = fullname
        self.term = term
        self.year = year
        self.form = form
        self.merit = merit
        self.subject = subject
        self.score = score
        self.code = code
        self.grade = grade


class Forms(db.Model):
    __tablename__ = 'forms'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(100), unique=True)
    form = db.Column(db.String(100))

    def __init__(self, code, form):
        self.code = code.title()
        self.form = form.title()


class Subjects(db.Model):
    __tablename__ = 'subjects'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100))
    cartegory = db.Column(db.String(100))

    def __init__(self, code, name, cartegory):
        self.code = code.title()
        self.name = name.title()
        self.cartegory = cartegory.title()
