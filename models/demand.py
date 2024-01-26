from config.db import db
from models.user import User
from models.offer import Offer

class Demand(db.Model):
    __tablename__ ='TBL_Demand'
    id = db.Column(db.Integer, primary_key=True)
    
    total = db.Column(db.Double)
    creation_date = db.Column(db.DateTime, default=db.func.now())
    
    offer_id = db.Column(db.Integer, db.ForeignKey('TBL_Offer.id'))
    offer = db.relationship('Offer', backref=db.backref('demands', lazy='dynamic'))
    user_id = db.Column(db.Integer, db.ForeignKey('TBL_User.id'))
    user = db.relationship('User', backref=db.backref('demands', lazy='dynamic'))

    products = db.relationship('Product', secondary='demand_products', backref=db.backref('demands', lazy='dynamic'))

    def __init__(self, offer_id, total, user_id):
        super().__init__()
        self.offer_id = offer_id
        self.total = total
        self.user_id = user_id
        
    def to_dict(self):
        return {
            'id': self.id,
            'offer_id': self.offer_id,
            'total': self.total,
            'user_id': self.user_id,
            'creation_date': self.creation_date.isoformat(),
            'offer': self.offer.to_dict() if self.offer else None,
            'user': self.user.to_dict() if self.user else None,
            'products': [product.to_dict() for product in self.products]
        }

demand_products = db.Table('demand_products',
    db.Column('demand_id', db.Integer, db.ForeignKey('TBL_Demand.id')),
    db.Column('product_id', db.Integer, db.ForeignKey('TBL_Product.id')),
    db.Column('quantity', db.Integer),
    db.PrimaryKeyConstraint('demand_id', 'product_id')
)
