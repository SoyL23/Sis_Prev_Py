from config.db import db

class Country(db.Model):
    __tablename__ = 'TBL_Country'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)

    def __init__(self, name, description):
        super().__init__()
        self.name = name
        self.description = description

    def __repr__(self):
        return f'<{self.name}>'
    
    def to_dict(self):
        return {
            "country": self.name,
            "description": self.description
        }