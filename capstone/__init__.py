from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY']='c9086aeae8e7451dd9f38272ee4f315a'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://capstone:password@localhost:5432/capstone_db"
db = SQLAlchemy(app)
db.create_all()
login_manager = LoginManager(app)

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

from capstone import routes
