from capstone import db

class accounts(db.Model):
    username = db.Column(db.String(20), unique=True, nullable = False)
    email = db.Column(db.String(100), unique=True, nullable = False, primary_key = True)
    acc_type = db.Column(db.String(10), nullable = False)
    password = db.Column(db.String(), nullable = False)
    approved = db.Column(db.Boolean(), nullable = False, default = False)

    __table_args__ = {'extend_existing': True}

    def __repr__(self):
       return f"User('{self.username}', '{self.email}')"