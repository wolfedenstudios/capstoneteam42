import email
from capstone import db, login_manager
from flask_login import UserMixin

db.create_all()

@login_manager.user_loader
def load_user(email):
    return accounts.query.get(email)


class accounts(db.Model, UserMixin):
    username = db.Column(db.String(20), unique=True, nullable = False)
    email = db.Column(db.String(100), unique=True, nullable = False, primary_key = True)
    acc_type = db.Column(db.String(10), nullable = False)
    password = db.Column(db.String(), nullable = False)
    approved = db.Column(db.Boolean(), nullable = False, default = False)

    def get_id(self):
       return (self.email)

    __table_args__ = {'extend_existing': True}

    def __repr__(self):
       return f"User('{self.username}', '{self.email}')"