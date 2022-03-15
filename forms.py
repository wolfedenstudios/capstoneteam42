from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=20)])
    email = StringField('Email', validators=[DataRequired(),Email()])
    accessLevel = StringField('AccessLevel', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmPassword = PasswordField('confirmPassword', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
