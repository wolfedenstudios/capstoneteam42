from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Email, EqualTo, ValidationError, NumberRange
from capstone import db
from capstone.models import accounts

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired("Username must be 5-20 characters"), Length(min=5, max=20)])
    email = StringField('Email', validators=[InputRequired("Please put in an email"),Email("Please put a valid email")])
    accessLevel = StringField('Access Level', validators=[InputRequired("Must not be empty")])
    password = PasswordField('Password', validators=[InputRequired()])
    confirmPassword = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = accounts.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('Username Taken')

    def validate_email(self, email):
        user = accounts.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError('Account with this email already exists, or is currently waiting to be approved')
    
    #This appears to be working but does not give an error message
    def validate_accessLevel(self, accessLevel):
        if ((accessLevel.data != 'ADMIN') and (accessLevel.data != 'ASSISTANT')):
            raise ValidationError('Access Level Must Be ADMIN or ASSISTANT')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(),Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

class teacherForm(FlaskForm):
    lastName = StringField('Last Name', validators=[InputRequired()])
    maxLoad = IntegerField('Max Load', validators=[InputRequired(), NumberRange(min = 1, max = 4)])

class classForm(FlaskForm):
    courseNum = IntegerField('Course Number', validators=[InputRequired()])
    courseTitle = StringField('Course Title', validators=[InputRequired()])
    
