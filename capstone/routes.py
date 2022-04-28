from sre_constants import SUCCESS
from flask import render_template, session, url_for, flash, redirect, request
from sqlalchemy import null
from capstone import app
from flask_mail import Message
from capstone.forms import RegistrationForm, LoginForm, classForm, requestForm, resetForm, teacherForm
from capstone import db, get_db_connection, mail
from capstone.models import accounts, instructors, sections, output_schedule
from flask_login import current_user, login_required, login_user, logout_user

@app.route('/')
def home():
    return render_template('home.html', title='Home')

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
                if user.email == 'ROOT_USER':
                    return redirect(url_for('reset'))
                else:
                    return redirect(url_for('home'))

            else:
                flash('Login unsuccessful, account not approved', 'danger')

        else:
            flash('Login unsuccessful, check email and password', 'danger')

    return render_template('login.html', title='Log In', form=form)



@app.route('/add/professor', methods=['GET', 'POST'])
@login_required
def addProf():
    if (current_user.acc_type == 'ADMIN' or current_user.acc_type == 'ROOT'):
        form=teacherForm()

        if form.validate_on_submit():
                lastName = form.lastName.data
                maxLoad = form.maxLoad.data
                disciplines = form.disciplines.data
                profAdd = instructors(LName = lastName, MaxLoad = maxLoad, Disciplines = disciplines)
                db.session.add(profAdd)
                db.session.commit()


        return render_template('addProf.html', title='requests', form=form)

    else:
        flash('you must be admin to access this page', 'danger')
        return redirect(url_for('home'))


@app.route('/add/course', methods=['GET', 'POST'])
@login_required
def addCourse():
    if (current_user.acc_type == 'ADMIN' or current_user.acc_type == 'ROOT'):
        form=classForm()

        if form.validate_on_submit():
            Code = form.Code.data
            Name = form.Name.data
            disciplines = form.disciplines.data
            deptCode = form.deptCode.data

            course = sections(Code = Code, Name = Name, Disciplines = disciplines, DepartmentCode = deptCode)
            db.session.add(course)
            db.session.commit()


        return render_template('addClass.html', title='requests', form=form)

    else:
        flash('you must be admin to access this page', 'danger')
        return redirect(url_for('home'))


@app.route('/instructors')
@login_required
def instructorList():
    if (current_user.acc_type == 'ADMIN' or current_user.acc_type == 'ROOT'):
        instructorList = instructors.query.all()
        return render_template('instructors.html', title='Instructor List', instructorList=instructorList)
    else:
        return redirect(url_for('home'))


@app.route('/courses')
@login_required
def courses():
    if (current_user.acc_type == 'ADMIN' or current_user.acc_type == 'ROOT'):
        courseList = sections.query.all()
        return render_template('sections.html', title='section list', courseList=courseList)
    else:
        return redirect(url_for('home'))

@app.route('/reset', methods=['GET', 'POST'])
@login_required
def reset():
    form=resetForm()
    if form.validate_on_submit():

        if current_user.password == form.currentPassword.data:
            if form.newPassword.data == form.confirmPassword.data:
                current_user.password = form.newPassword.data
                db.session.commit()
            else:
                flash('Password is incorrect or new password does not match confirm password', 'danger')
        return redirect(url_for('home'))
    return render_template('reset.html', title = 'reset password', form=form)


@app.route('/approve', methods=['GET', 'POST'])
@login_required
def approvePage():
    form = requestForm()

    if (current_user.acc_type == 'ROOT'):
        requestedAcc = accounts.query.filter_by(approved = False).first()
        
        if request.method == 'POST':
            if request.form['submit_button'] == 'Approve':
                print('hello')
                requestedAcc.approved = True
                db.session.commit()
                return redirect(url_for('approvePage'))

            elif request.form['submit_button'] == 'Deny':
                db.session.query(accounts).filter(accounts.email == requestedAcc.email ).delete()
                db.session.commit()
                return redirect(url_for('approvePage'))


        
        return render_template('requests.html', title='Approve or Deny Registration', accountList = requestedAcc, form = form)

    

    



@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))    


@app.route('/courses')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM course;')
    books = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', course=course)
