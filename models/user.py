from config.db import db

class User(db.Model):

    __tablename__ ='TBL_User'

    id = db.Column(db.Integer, primary_key=True)
   # fullname = db.Column(db.String(50))
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    email = db.Column(db.String(50))
    #username = db.Column(db.String(15), unique=True)
    username = db.Column(db.String(15))
    password = db.Column(db.String(66))
    celular = db.Column(db.String(12))
    ciudad = db.Column(db.String(50))

   # def __init__(self,fullname,email,username,password,celular,ciudad):
    def __init__(self,nombre, apellido, email, username, password, celular,ciudad):
        super().__init__()
        #        self.fullname = fullname
        self.nombre = nombre
        self.apellido= apellido
        self.email = email
        self.username = username
        self.password = password
        self.celular = celular
        self.ciudad = ciudad