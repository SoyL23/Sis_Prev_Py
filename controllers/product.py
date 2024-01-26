from services.require_content_type import require_content_type
from models.product import Product
from config.db import db
from flask import Blueprint, make_response, request, jsonify

product = Blueprint('product', __name__)

@require_content_type('Aplication/Json')
@product.route('/product/create', methods=['GET', 'POST'])
def product_create():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        try:
            product = request.get_json()
            if product != None:
                name = product['name']
                variety = product['variety']
                value = product['value']
                photo = product['photo']
                description = product['description']
                new_product = Product(name=name,variety=variety, value=value,photo=photo, description=description)
                with db.session.begin():
                    db.session.add(new_product)
                    db.session.commit() 
                    db.session.close()
                return make_response('Producto Creado', 200)
            else: 
                return make_response('Producto Vacío', 400) 
        except Exception as e:
            return 'Ha ocurrido un error: ' + str(e)
    else:
        return make_response('Invalid Request', 400)
    
@require_content_type('aplication/JSON')
@product.route('/product/delete/<id>', methods=['POST'])
def delete_product(id):
    product_deleted = Product.query.get(id)
    if request.method == 'POST':
        try:
            with db.session.begin():
                db.session.delete(product_deleted)
                db.session.commit()
                db.session.close()
            return make_response('Producto Eliminado', 200)
        except Exception as e:
            return 'Ha ocurrido un error: ' + str(e)
    else:
        return make_response('Invalid Request', 400)
        
@require_content_type('aplication/JSON')
@product.route('/product/update/<id>', methods=['GET', 'POST'])
def update_product(id):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        update_product = request.get_json()
        product = Product.query.get(id)
        if update_product != None:

            product.name = update_product['name']
            product.variety = update_product['variety']
            product.value = update_product['value']
            product.description = update_product['description']

            with db.session.begin():
                db.session.commit()
                db.session.close()

            return make_response('Producto Actualizado', 200)
    else:
        return make_response('Invalid Request', 400)
        
@require_content_type('aplication/JSON')
@product.route('/product/get/<id>', methods=['GET'])
def get_product(id):
    if request.method == 'GET':
        product = Product.query.get(id)
        if product != None:
            return jsonify(product.to_dict())
    else:
        return make_response('Invalid Request', 400)
    
@require_content_type('aplication/JSON')
@product.route('/product/get/list', methods=['GET'])
def get_products():
    if request.method == 'GET':
        products = Product.query.all()
        list_products = {}
        for product in products:
            list_products[product.id] = product.to_dict()
        return jsonify(list_products)
    else:
        return make_response('Invalid Request', 400)