from config.db import db
from models.demand import Demand
from models.offer import Offer
from models.user import User
from models.point_sell import PointSell

class Sell(db.Model):
    __tablename__ ='TBL_Sell'
    id = db.Column(db.Integer, primary_key=True)
    demand_id = db.Column(db.Integer, db.ForeignKey('Demand.id'))
    offer_id = db.Column(db.Integer, db.ForeignKey('Offer.id'))
    total = db.Column(db.Double)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    creation_date = db.Column(db.DateTime, default=db.func.now())

    point_sell_id = db.Column(db.Integer, db.ForeignKey('PointSell.id'))
    point_sell = db.relationship('PointSell', backref=db.backref('sells', lazy='dynamic'))
    demand = db.relationship('Demand', backref=db.backref('sells', lazy='dynamic'))
    offer = db.relationship('Offer', backref=db.backref('sells', lazy='dynamic'))
    user = db.relationship('User', backref=db.backref('sells', lazy='dynamic'))

    def __init__(self, demand_id, offer_id, total, user_id):
        super().__init__()
        self.demand_id = demand_id
        self.offer_id = offer_id
        self.total = total
        self.user_id = user_id
    def to_dict(self):
        return {
            'id': self.id,
            'demand_id': self.demand_id,
            'offer_id': self.offer_id,
            'total': self.total,
            'user_id': self.user_id,
            'creation_date': self.creation_date.isoformat(),
            'demand': self.demand.to_dict() if self.demand else None,
            'offer': self.offer.to_dict() if self.offer else None,
            'user': self.user.to_dict() if self.user else None,
            'PointOfSell': self.point_sell.to_dict() if self.point_sell else None
        }