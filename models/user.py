from config.db import db
from models.city import City
from models.role import Role

class User(db.Model):

    __tablename__ ='TBL_User'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25))
    last_name = db.Column(db.String(25))
    email_user = db.Column(db.String(50))
    username = db.Column(db.String(15))
    password = db.Column(db.String(66))
    cellphone = db.Column(db.String(12))

    role_id = db.Column(db.Integer, db.ForeignKey('TBL_Role.id'))
    role = db.relationship('Role', backref='users')
    city_id = db.Column(db.Integer, db.ForeignKey('TBL_City.id'))
    city = db.relationship('City', backref='users')

   # def __init__(self,fullname,email,username,password,celular,ciudad):
    def __init__(self, first_name, last_name, email_user, username, password, cellphone, city_id, role_id):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email_user = email_user
        self.username = username
        self.password = password
        self.cellphone = cellphone
        self.city_id = city_id
        self.role_id = role_id


    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email_user': self.email_user,
            'username': self.username,
            'cellphone': self.cellphone,
            'city_id': self.city_id,
            'role_id': self.role_id,
            'role': self.role.to_dict() if self.role else None,  # Incluye la relación role
            'city': self.city.to_dict() if self.city else None  # Incluye la relación city
        }