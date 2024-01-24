from config.db import db
from models.product import Product

class Offer(db.Model):
    __tablename__ = 'TBL_Offer'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(255))
    creation_date = db.Column(db.DateTime, default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('TBL_User.id'))
    user = db.relationship('User', backref=db.backref('offers', lazy='dynamic'))
    products = db.relationship('Product', secondary='offer_products', backref=db.backref('offers', lazy='dynamic'))

    def __init__(self, name, description, user_id):
        super().__init__()
        self.name = name
        self.description = description
        self.user_id = user_id

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'creation_date': self.creation_date,
            'user': self.user.to_dict(),
            'products': [product.to_dict() for product in self.products]
        }

offer_products = db.Table('offer_products',
    db.Column('offer_id', db.Integer, db.ForeignKey('TBL_Offer.id')),
    db.Column('product_id', db.Integer, db.ForeignKey('TBL_Product.id')),
    db.Column('product_value', db.Double())
)
