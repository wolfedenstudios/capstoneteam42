from flask import render_template, url_for, flash, redirect
from capstone import app
from flask_mail import Message
from capstone.forms import RegistrationForm, LoginForm
from capstone import db, get_db_connection, mail
from capstone.models import accounts
from flask_login import login_user

@app.route('/')
def hello():
    return render_template('base.html', title='Home', form=form)

@app.route('/email')
def sendEmail():
    msg = Message('Testing the email stuff', 
                  sender = 'UALR.Capstone.Team42@gmail.com',
                  recipients = ['UALR.Capstone.Team42@gmail.com'])
    msg.body = "testing email stuff"
    mail.send(msg)
    return 'Message Sent!'

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    print(form.errors)

    if form.validate_on_submit():
        flash(f'Registration request submitted for {form.username.data}.', 'success')

        #send email

        msg = Message('Registration Request Submitted', 
                  sender = 'UALR.Capstone.Team42@gmail.com',
                  recipients = [f'{form.email.data}'])
        msg.body = "Your registration request has been submitted."
        mail.send(msg)

        #Add to database

        username = form.username.data
        email = form.email.data
        password = form.password.data
        acc_type = form.accessLevel.data

        user = accounts(username = username, email = email, password = password, acc_type = acc_type)
        db.session.add(user)
        db.session.commit()



        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        print('valid')
        #add code to search database for email, check if email exists, and check password

        user = accounts.query.filter_by(email = form.email.data).first()
        if user and (user.password == form.password.data):
            if user.approved == True:
                login_user(user)
                return redirect(url_for('hello'))
            else:
                flash('Login unsuccessful, account not approved', 'danger')

        else:
            flash('Login unsuccessful, check email and password', 'danger')

    return render_template('login.html', title='Log In', form=form)



@app.route('/courses')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM course;')
    books = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', course=course)
