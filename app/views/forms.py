from flask_wtf import Form
from flask import session
from sqlalchemy import or_
from app import db
from wtforms import SubmitField, validators, ValidationError, PasswordField, StringField, RadioField, SelectField
from app.models import Student, User, Marks, Subjects, Forms


class SignupForm(Form):
    username = StringField('User Name', [validators.DataRequired("Please enter your first name.")],
                           render_kw={"placeholder": "User Name"})
    # username = StringField("First name", [validators.DataRequired("Please enter your first name.")])
    email = StringField("Email", [validators.DataRequired("Please enter your email address."),
                        validators.Email("Please enter your email address.")],
                        render_kw={"placeholder": "Email Address"})
    password = PasswordField('Password', [validators.DataRequired("Please enter a password.")],
                             render_kw={"placeholder": "Password"})
    passwordAgain = PasswordField('Password', [validators.DataRequired("Please enter a password.")],
                                  render_kw={"placeholder": "Re-Enter Password"})

    submit = SubmitField("Sign Up")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        user = User.query.filter_by(email=self.email.data.lower()).first()
        if user:
            self.email.errors.append("That email is already taken")
            return False
        else:
            return True

        user = User.query.filter_by(username=self.username.data.lower()).first()
        if user:
            self.username.errors.append("That username is already taken")
            return False
        else:
            return True


class SigninForm(Form):
    loginid = StringField("Email", [validators.DataRequired("Please enter your login id.")],
                          render_kw={"placeholder": "Username or Email"})
    password = PasswordField('Password', [validators.DataRequired("Please enter a password.")],
                             render_kw={"placeholder": "Password"})
    submit = SubmitField("Sign In")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        user_email = User.query.filter_by(email=self.loginid.data.lower()).first()
        user_name = User.query.filter_by(username=self.loginid.data).first()
        # user = User.query.filter_by(or_(email=self.loginid.data.lower(), username=self.loginid.data)).first()
        if (user_email and user_email.check_password(self.password.data)) or \
                (user_name and user_name.check_password(self.password.data)):
            return True
        else:
            self.loginid.errors.append("Invalid e-mail or password")
            return False


class NewStudentForm(Form):
    firstname = StringField("First name", [validators.DataRequired("Please enter your first name.")])
    middlename = StringField("First name", [validators.DataRequired("Please enter your first name.")])
    lastname = StringField("First name", [validators.DataRequired("Please enter your first name.")])
    # gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')])
    regdate = StringField("First name", [validators.DataRequired("Please enter your first name.")])
    regnumber = StringField("First name", [validators.DataRequired("Please enter your first name.")])
    # stream = StringField("First name", [validators.DataRequired("Please enter your first name.")])

    # form = StringField("Email", [validators.DataRequired("Please enter your email address.")])
    marks = PasswordField('Password', [validators.DataRequired("Please enter a password.")])

    # language = SelectField('Languages', choices = [('cpp', 'C++'), ('py', 'Python')])

    # submit = SubmitField("Create account")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        user = User.query.filter_by(email=self.email.data.lower()).first()
        if user:
            self.email.errors.append("That email is already taken")
            return False
        else:
            return True

        user = User.query.filter_by(username=self.username.data.lower()).first()
        if user:
            self.username.errors.append("That username is already taken")
            return False
        else:
            return True


class SubjectsForm(Form):
    code = StringField("First name", [validators.DataRequired("Please enter subject short code.")])
    name = StringField("First name", [validators.DataRequired("Please enter subject name.")])
    cartegory = SelectField('Languages', choices=[('Languages', 'Languages'),
                                                 ('Mathematics', 'Mathematics'),
                                                 ('Sciences', 'Sciences'),
                                                 ('Humanities', 'Humanities')])

    submit = SubmitField("Save Details")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        subject = Subjects.query.filter_by(code=self.code.data.lower()).first()
        if subject:
            self.email.errors.append("That code is already in use")
            return False
        else:
            return True

        subject = Subjects.query.filter_by(name=self.name.data.lower()).first()
        if subject:
            self.username.errors.append("That subject already exists")
            return False
        else:
            return True


class ClassesForm(Form):
    code = StringField("First name", [validators.DataRequired("Please enter subject short code.")])
    name = StringField("First name", [validators.DataRequired("Please enter subject name.")])

    submit = SubmitField("Save Details")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        form = Forms.query.filter_by(code=self.code.data.lower()).first()
        if form:
            self.code.errors.append("That code is already in use")
            return False
        else:
            return True

