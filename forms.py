from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=5, max=20)])
    email = StringField('Email', validators=[InputRequired(),Email()])
    accessLevel = StringField('AccessLevel', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    confirmPassword = PasswordField('confirmPassword', validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(),Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')
