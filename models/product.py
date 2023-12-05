from config.db import db

class Product(db.Model):

    __tablename__ ='TBL_Product'

    id = db.Column(db.Integer, primary_key=True)
    producto_nombre = db.Column(db.String(50))
    producto_proveedor = db.Column(db.String(50)) # aqui debe ir una llave foren_key
    producto_foto = db.Column(db.String(50)) # aquí debe ir un tipo de dato file
    producto_caracteristicas = db.Column(db.String(255))
   
    def __init__(self,producto_nombre,producto_proveedor,producto_foto,producto_caracteristicas):
        super().__init__()
        self.producto_nombre = producto_nombre
        self.producto_proveedor = producto_proveedor
        self.producto_foto = producto_foto
        self.producto_caracteristicas = producto_caracteristicas
