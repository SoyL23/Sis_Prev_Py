from config.db import db
from models.city import City
from models.user import User
from models.product import Product
from models.sell import Sell

class PointSell(db.Model):
    __tablename__ ='TBL_Sell_Points'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    
    phone = db.Column(db.String(20))
    email = db.Column(db.String(120))
    status = db.Column(db.Enum('active', 'inactive', 'temporal', name='point_sell_status'), default='active')
    creation_date = db.Column(db.DateTime, default=db.func.now())

    city_id = db.Column(db.Integer, db.ForeignKey('TBL_City.id'), nullable=False)
    city = db.relationship('City', backref='pointsells')

    user_id = db.Column(db.Integer, db.ForeignKey('TBL_User.id'), nullable=False)
    user = db.relationship('User', backref='pointsells')

    cooperative_id = db.Column(db.Integer, db.ForeignKey('TBL_Cooperative.id'))
    cooperative = db.relationship('Cooperative', backref=db.backref('point_sells', lazy='dynamic'))

    products = db.relationship('Product', secondary='point_sell_products', backref=db.backref('point_sells', lazy='dynamic'))
    sells = db.relationship('Sell', backref=db.backref('point_sell', lazy='dynamic'))

    def __init__(self, name, address, city_id, phone=None, email=None, user_id=None, cooperative_id=None):
        super().__init__()
        self.name = name
        self.address = address
        self.city_id = city_id
        self.phone = phone
        self.email = email
        self.user_id = user_id
        self.cooperative_id = cooperative_id

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'city_id': self.city_id,
            'phone': self.phone,
            'email': self.email,
            'status': self.status,
            'creation_date': self.creation_date.isoformat(),
            'user': self.user.to_dict() if self.user else None,
            'sells': [sell.to_dict() for sell in self.sells],
            'cooperative': self.cooperative.to_dict() if self.cooperative else None
        }