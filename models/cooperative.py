from config.db import db
from models.product import Product


class Cooperative(db.Model):
    __tablename__ ='TBL_Cooperative'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    phone = db.Column(db.String(15))
    email = db.Column(db.String(120))
    city_id = db.Column(db.Integer, db.ForeignKey('TBL_City.id'))
    city = db.relationship('City', backref='cooperatives')
    products = db.relationship('Product', secondary='cooperative_products',
        backref=db.backref('cooperative', lazy='dynamic'))
    description = db.Column(db.Text)
    status = db.Column(db.Boolean())

    def __init__(self, name, phone, email, city_id, description, status):
        super().__init__()
        self.name = name
        self.phone = phone
        self.email = email
        self.city_id = city_id
        self.description = description
        self.status = status
    def to_dict(self):
        return {
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'city': self.city.to_dict() if self.city else None,
            'city_id': self.city_id,
            'description': self.description,
            'status': self.status
        }

cooperative_products = db.Table('cooperative_products',
    db.Column('cooperative_id', db.Integer, db.ForeignKey('TBL_Cooperative.id')),
    db.Column('product_id', db.Integer, db.ForeignKey('TBL_Product.id')),
    db.PrimaryKeyConstraint('cooperative_id', 'product_id')
)

