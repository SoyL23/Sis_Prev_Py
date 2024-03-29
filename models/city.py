from config.db import db
from models.country import Country

class City(db.Model):
    __tablename__ = 'TBL_City'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    country_id = db.Column(db.Integer, db.ForeignKey('TBL_Country.id'))
    country = db.relationship('Country', backref='citys')

    def __init__(self,name,description,country_id):
        super().__init__()
        self.name = name
        self.description = description
        self.country_id = country_id

    def __repr__(self):
        return f'<{self.name}>'
    
    def to_dict(self):
        return {
            "city": self.name,
            'country': self.country.to_dict() if self.country else None
        }