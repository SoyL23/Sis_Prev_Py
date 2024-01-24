from flask import Blueprint, request, make_response, jsonify
from models.offer import Offer
from config.db import db
offer = Blueprint('offer', __name__)

@offer.route('/offer/create', methods = ['GET', 'POST'])
def create_offer():
    new_offer_data = request.get_json()
    if request.method == 'GET':
        try:
            pass
        except Exception as e:
            return make_response(f'Ha ocurrido un error: {e}', 400)
    elif request.method == 'POST':
        try:
            name = new_offer_data['name']
            description = new_offer_data['description']
            user_id = new_offer_data['user_id']
            product_ids = new_offer_data['product_ids']
            
            new_offer = Offer(name=name, description=description, user_id=user_id)

            for product_id in product_ids:
                if product_id:
                    new_offer.products.append(product_id)
            db.session.add(new_offer)
            db.session.commit()
            return make_response(f'Se ha Creado la Oferta: {new_offer.name}', 200)
        except Exception as e:
            return make_response(f'Ha ocurrido un error: {e}', 400)
    else: 
        return('Ha ocurrido un error')
    
@offer.route('/offer/delete/<id>', methods = ['GET', 'POST'])
def delete_offer(id):
    if request.method == 'GET':
        try:
            offer = Offer.query.get(id)
            if offer:
                db.session.delete(offer)
                db.session.commit()
                return make_response(f'Oferta Eliminada: {Offer.id}')
        except Exception as e:
            return make_response(f'Ha ocurrido un error: {e}', 400)
    elif request.method == 'POST':
        try:
            pass
        except Exception as e:
            return make_response(f'Ha ocurrido un error: {e}', 400)
    else: 
        return('Ha ocurrido un error')
    
@offer.route('/offer/update/<id>', methods = ['GET', 'POST'])
def update_offer(id):
    if request.method == 'GET':
        try:
            pass
        except Exception as e:
            return make_response(f'Ha ocurrido un error: {e}', 400)
    elif request.method == 'POST':
        try:
            pass
        except Exception as e:
            return make_response(f'Ha ocurrido un error: {e}', 400)
    else: 
        return('Ha ocurrido un error')