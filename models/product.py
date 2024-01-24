from config.db import db
import decimal

class Product(db.Model):

    __tablename__ ='TBL_Product'

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(50))
    product_value = db.Column(db.Double())
    product_photo = db.Column(db.LargeBinary(), nullable=True)
    product_description = db.Column(db.String(255))

    def __init__(self,product_name,product_value,product_photo,product_description):
        super().__init__()
        self.product_name = product_name
        self.product_value = product_value
        self.product_photo = product_photo
        self.product_description = product_description

    def to_dict(self):
        return{
            'name': self.product_name,
            'value': self.product_value,
            'description': self.product_description
        }
            