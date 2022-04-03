from flask import Flask, render_template, url_for, flash, redirect
from flask_mail import Mail, Message
from forms import RegistrationForm, LoginForm
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
    if form.is_submitted():
        print('submitted')
        print(form.errors)

    if form.validate_on_submit():
        print('valid')
        
        print(form.errors)
        flash('Account created for!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form=LoginForm()
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


