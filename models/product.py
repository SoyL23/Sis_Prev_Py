from config.db import db
import decimal

class Product(db.Model):

    __tablename__ ='TBL_Product'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    variety = db.Column(db.String(50))
    value = db.Column(db.Double())
    photo = db.Column(db.LargeBinary(), nullable=True)
    description = db.Column(db.String(255))

    def __init__(self,name,variety,value,photo,description):
        super().__init__()
        self.name = name
        self.variety = variety
        self.value = value
        self.photo = photo
        self.description = description

    def to_dict(self):
        return{
            'name': self.name,
            'variety': self.variety,
            'value': self.value,
            'photo': self.photo,
            'description': self.description
        }
            