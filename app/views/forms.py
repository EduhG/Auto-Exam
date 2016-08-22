from flask_wtf import Form
from wtforms import SubmitField, validators, ValidationError, PasswordField, StringField
from app.models import Student, User, Marks


class SignupForm(Form):
    username = StringField("First name", [validators.DataRequired("Please enter your first name.")])
    email = StringField("Email", [validators.DataRequired("Please enter your email address."),
                        validators.Email("Please enter your email address.")])
    password = PasswordField('Password', [validators.DataRequired("Please enter a password.")])

    submit = SubmitField("Create account")

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
