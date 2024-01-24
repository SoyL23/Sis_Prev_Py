from config.db import db

class Country(db.Model):
    __tablename__ = 'TBL_Country'

    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(50), nullable=False)
    country_description = db.Column(db.String(255))

    def __init__(self, country, country_description):
        super().__init__()
        self.country = country
        self.country_description = country_description

    def __repr__(self):
        return f'<{self.country}>'
    
    def to_dict(self):
        return {
            "country": self.country,
        }