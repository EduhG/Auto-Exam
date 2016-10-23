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


# class NewStudentForm(Form):
#     firstname = StringField("First name", [validators.DataRequired("Please enter your first name.")])
#     middlename = StringField("First name", [validators.DataRequired("Please enter your first name.")])
#     lastname = StringField("First name", [validators.DataRequired("Please enter your first name.")])
#     # gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')])
#     regdate = StringField("First name", [validators.DataRequired("Please enter your first name.")])
#     regnumber = StringField("First name", [validators.DataRequired("Please enter your first name.")])
#     # stream = StringField("First name", [validators.DataRequired("Please enter your first name.")])
#
#     # form = StringField("Email", [validators.DataRequired("Please enter your email address.")])
#     marks = PasswordField('Password', [validators.DataRequired("Please enter a password.")])
#
#     def __init__(self, *args, **kwargs):
#         Form.__init__(self, *args, **kwargs)
#
#     def validate(self):
#         if not Form.validate(self):
#             return False
#
#         user = Student.query.filter_by(regnumber=self.regnumber.data.lower()).first()
#         if user:
#             self.email.errors.append("That reg number is already taken")
#             return False
#         else:
#             return True


class NewStudentForm(Form):
    firstname = StringField("First Name", [validators.InputRequired("Please enter your first name.")])
    middlename = StringField("Middle Name", [validators.InputRequired("Please enter your first name.")])
    lastname = StringField("Last Name", [validators.InputRequired("Please enter your first name.")])
    gender = RadioField('Gender', [validators.InputRequired("Please select gender.")],
                        choices=[('Male', 'Male'), ('Female', 'Female')])
    regdate = StringField("Reg Date", [validators.InputRequired("Please enter your first name.")],
                          render_kw={"placeholder": "Reg Date"})
    regnumber = StringField("Reg Number", [validators.InputRequired("Please enter your first name.")])
    stream = SelectField('Stream', [validators.Length(2, 60, "Choose Stream")], choices=[('', 'Choose Stream')])
    adm_class = SelectField('Form', [validators.Length(2, 60, "Choose Form")], choices=[('', 'Choose Form')])
    marks = PasswordField('Adm Marks', [validators.InputRequired("Please enter a password.")])

    submit = SubmitField("Save Details")

    def __init__(self, *args, **kwargs):
        super(NewStudentForm, self).__init__(*args, **kwargs)

    def validate(self):

        user = Student.query.filter_by(regnumber=str(self.regnumber.data).lower()).first()

        if not user:
            return True
        else:
            new_errors = list(self.cartegory_name.errors)
            new_errors.append("That reg number is already taken")
            self.regnumber.errors = tuple(new_errors)

            return False


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

