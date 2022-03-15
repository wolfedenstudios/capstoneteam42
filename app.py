from flask import Flask, render_template, url_for
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

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/email')
def sendEmail():
    msg = Message('Testing the email stuff', 
                  sender = 'UALR.Capstone.Team42@gmail.com',
                  recipients = ['UALR.Capstone.Team42@gmail.com'])
    msg.body = "testing email stuff"
    mail.send(msg)
    return 'Message Sent!'

@app.route('/register')
def register():
    form = RegistrationForm
    if form.validate_on_submit():
        #send email to form.email.data
        print('hello world')
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form=LoginForm
    return render_template('login.html', title='Log In', form=form)




