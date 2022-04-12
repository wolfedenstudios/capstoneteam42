from flask import Flask, render_template, url_for, flash, redirect
from flask_mail import Mail, Message
from forms import RegistrationForm, LoginForm
import psycopg2

app = Flask(__name__)
app.config['SECRET_KEY']='c9086aeae8e7451dd9f38272ee4f315a'

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'UALR.Capstone.Team42@gmail.com'
app.config['MAIL_PASSWORD'] = 'ualrcs42'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='capstone_db',
                            user='capstone',
                            password='password')
    return conn

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

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO accounts (username, email, password, acc_type)' 'VALUES (%s, %s, %s, %s)', (username, email, password, acc_type))

        conn.commit()
        cur.close()
        conn.close()




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

if __name__ == "__main__":
    app.run()


