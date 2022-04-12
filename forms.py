from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired("Username must be 5-20 characters"), Length(min=5, max=20)])
    email = StringField('Email', validators=[InputRequired("Please put in an email"),Email("Please put a valid email")])
    accessLevel = StringField('AccessLevel', validators=[InputRequired("Must not be empty")])
    password = PasswordField('Password', validators=[InputRequired()])
    confirmPassword = PasswordField('confirmPassword', validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(),Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')
