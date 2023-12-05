from flask import Blueprint, render_template, request, redirect, url_for #url_for para redireccionar a una función
from config.db import db 
from models.product import Product



product = Blueprint('product', __name__)

@product.route('/login')
def login():
    return render_template('')

#-----------------------------------------------------------------update
#@product.route('/')
@product.route('/product_update/<id>', methods =['POST', 'GET'])
def product_update(id):
    product = Product.query.get(id)
    if request.method == 'POST':
        product.producto_nombre = request.form["producto_nombre"]
        product.producto_proveedor = request.form["producto_proveedor"]
        product.producto_foto = request.form["producto_foto"]
        product.producto_caracteristicas = request.form["producto_caracteristicas"]
        db.session.commit()
        return redirect('/product/create')

    return render_template('product_update.html', product=product)

#------------------------------------------------------------------delete
@product.route('/')
@product.route('/<id>') #recibe del href el id y lo pasa a la funcion
def product_delete(id):#aquí la función recibe el id
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    
    return redirect('/product/create')
   # return render_template('product_delete.html')
   # return "se eliminó  el producto"

#---------------------------------------------------------------------create
@product.route('/product/create')
def product_create():
    products=Product.query.all() #esto es como hacer Select * para hacer lista
    return render_template('product_create.html', products=products) # se agrega products para pasar la lista

@product.route('/product/new', methods=['POST'])
def product_new():
    data = request.form
    producto_nombre = data['producto_nombre']
    producto_proveedor = data['producto_proveedor']
    producto_foto = data['producto_foto']
    producto_caracteristicas = data['producto_caracteristicas']
    
    product_new = Product(producto_nombre, producto_proveedor, producto_foto, producto_caracteristicas)
    db.session.add(product_new)
    db.session.commit()
    return redirect('/product/create')
