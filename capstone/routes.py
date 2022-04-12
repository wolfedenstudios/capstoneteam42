from flask import render_template, url_for, flash, redirect
from capstone import app
from flask_mail import Message
from capstone.forms import RegistrationForm, LoginForm
from capstone import db, get_db_connection, mail
from capstone.models import accounts

@app.route('/')
def hello():
    return 'Hello, World! App is working.'

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

@app.route('/login')
def login():
    form=LoginForm()
    if form.validate_on_submit():
        print('valid')
        #add code to search database for email, check if email exists, and check password
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM accounts WHERE email={form.email.data}')

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
