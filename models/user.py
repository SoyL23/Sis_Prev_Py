from config.db import db

class User(db.Model):

    __tablename__ ='TBL_User'

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(50))
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50))
    password = db.Column(db.String(66))
    num_celular = db.Column(db.String(12))
    ciudad = db.Column(db.String(50))

    def __init__(self,fullname,username,email,password,num_celular,ciudad):
        super().__init__()
        self.fullname = fullname
        self.username = username
        self.email = email
        self.password = password
        self.num_celular = num_celular
        self.ciudad = ciudad