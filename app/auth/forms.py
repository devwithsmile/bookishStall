# auth/forms.py

from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.auth.models import User


def email_exists(form, field):
    email = User.query.filter_by(user_email=field.data).first()
    if email:
        raise ValidationError('Email already Exists')


class RegisterationForm(FlaskForm):
    name = StringField("What's your Name ?", validators=[DataRequired(), Length(3, 15, message= "Name should be between 3 to 15 caracters")])
    email = StringField('Enter your Email', validators=[DataRequired(), Email(), email_exists])
    password = PasswordField("Enter Your Password", validators=[DataRequired(), Length(5)])
    confirm_pass = PasswordField("confirm Password",
                                 validators=[DataRequired(), EqualTo("password", message="password must match")])
    submit = SubmitField('Register')


class Login_Form(FlaskForm):
    email = StringField('Enter your Email', validators=[DataRequired(), Email()])
    password = PasswordField("Enter Your Password", validators=[DataRequired(), Length(5)])
    stay_loggedin = BooleanField('Stay Logged In')
    submit = SubmitField('Register')
