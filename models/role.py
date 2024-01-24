from config.db import db
from models.cooperative import Cooperative

class Role(db.Model):
    __tablename__ ='TBL_Role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)

    cooperative = db.relationship('Cooperative', secondary='role_cooperatives',
        backref=db.backref('roles', lazy='dynamic'))

    def __init__(self, name, description):
        super().__init__()
        self.name = name
        self.description = description

    def __repr__(self):
        return f'{self.name}'

    def to_dict(self):
        return {
            "role": self.name,
            "description": self.description
        }
    
role_cooperatives = db.Table('role_cooperatives',
    db.Column('role_id', db.Integer, db.ForeignKey('TBL_Role.id'), nullable=False),
    db.Column('cooperative_id', db.Integer, db.ForeignKey('TBL_Cooperative.id'), nullable=False, default=None),
    db.PrimaryKeyConstraint('role_id', 'cooperative_id')
)
