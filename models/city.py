from config.db import db
from models.country import Country

class City(db.Model):
    __tablename__ = 'TBL_City'

    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50), nullable=False)
    city_description = db.Column(db.String(255))
    country_id = db.Column(db.Integer, db.ForeignKey('TBL_Country.id'))
    country = db.relationship('Country', backref='citys')

    def __init__(self, city, city_description, country_id):
        super().__init__()
        self.city = city
        self.city_description = city_description
        self.country_id = country_id

    def __repr__(self):
        return f'<{self.city}>'
    
    def to_dict(self):
        return {
            "city": self.city,
            'country': self.country.to_dict() if self.country else None
        }