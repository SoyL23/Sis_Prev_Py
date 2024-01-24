from controllers.require_content_type import require_content_type
from models.product import Product
from config.db import db
from flask import Blueprint, make_response, request, jsonify

product = Blueprint('product', __name__)

@require_content_type('Aplication/Json')
@product.route('/product/create', methods=['GET', 'POST'])
def product_create():
    product = request.get_json()
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        try:
            if product != None:
                product_name = product['product_name']
                product_value = product['product_value']
                product_photo = product['product_photo']
                product_description = product['product_description']
                new_product = Product(product_name, product_value,product_photo, product_description)
                print(new_product.product_name)
                db.session.add(new_product)
                db.session.commit() 
                return make_response('Producto Creado', 200)
            else: 
                return make_response('Producto Vacío', 400) 
        except Exception as e:
            return 'Ha ocurrido un error: ' + str(e)
    else:
        return make_response('Metodo HTTP no válido', 415)

@product.route('/product/delete/<id>', methods=['GET'])
def delete_product(id):
    product_deleted = Product.query.get(id)
    if request.method == 'GET':
        try:
            db.session.delete(product_deleted)
            db.session.commit()
            return make_response('Producto Eliminado', 200)
        except Exception as e:
            return 'Ha ocurrido un error: ' + str(e)

@product.route('/product/update/<id>', methods=['GET', 'POST'])
def update_product(id):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        update_product = request.get_json()
        product = Product.query.get(id)
        if update_product != None:
            product.product_name = update_product['product_name']
            product.product_value = update_product['product_value']
            product.product_description = update_product['product_description']
            db.session.commit()
            return make_response('Producto Actualizado', 200)
        

@product.route('/product/get/<id>', methods=['GET', 'POST'])
def get_product(id):
    if request.method == 'GET':
        product = Product.query.get(id)
        if product != None:
            return jsonify(product.to_dict())
        pass
    elif request.method == 'POST':
        pass
    else:
        pass

@product.route('/product/get/list', methods=['GET', 'POST'])
def get_products():
    if request.method == 'GET':
        products = Product.query.all()
        list_products = {}
        for product in products:
            list_products[product.id] = product.to_dict()
        return jsonify(list_products)
        pass
    elif request.method == 'POST':
        pass
    else:
        pass