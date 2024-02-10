from flask import Blueprint, request, make_response, jsonify
from models.offer import Offer
from config.db import db
from services.require_content_type import require_content_type

offer = Blueprint('offer', __name__)

@require_content_type('aplication/JSON')
@offer.route('/offer/create', methods = ['GET', 'POST'])
def create_offer():
    if request.method == 'GET':
        try:
            pass
        except Exception as e:
            return make_response(f'Ha ocurrido un error: {e}')
    elif request.method == 'POST':
        new_offer_data = request.get_json()
        try:
            if new_offer_data:
                name = new_offer_data['name']
                description = new_offer_data['description']
                user_id = new_offer_data['user_id']
                product_ids = new_offer_data['product_ids']
                status = new_offer_data['status']

                new_offer = Offer(name=name, description=description, user_id=user_id, status=status)
                for product_id in product_ids:
                    if product_id:
                        new_offer.products.append(product_id)

                with db.session.begin():
                    db.session.add(new_offer)
                    db.session.commit()

                return make_response(f'Se ha Creado la Oferta: {new_offer.name}', 200)
            else: 
                return make_response('No content', 204)
        except Exception as e:
            return make_response(f'Ha ocurrido un error: {e}')
    else: 
        return('Ha ocurrido un error')
    
@require_content_type('aplication/JSON')   
@offer.route('/offer/delete/<id>', methods = ['POST'])
def delete_offer(id):
    if request.method == 'POST':
        offer = Offer.query.get(id)
        try:
            if offer:
                with db.session.begin():
                    db.session.delete(offer)
                    db.session.commit()
                return make_response(f'Oferta Eliminada: {Offer.id}', 200)
            else:
                return make_response('No Content Data', 204)
        except Exception as e:
            return make_response(f'Ha ocurrido un error: {e}')
    else: 
        return make_response('Ha ocurrido un error')
    
@require_content_type('aplication/JSON')   
@offer.route('/offer/update/<id>', methods = ['POST'])
def update_offer(id):
    if request.method == 'POST':
        try:
            updated_offer = request.get_json()
            offer = Offer.query.get(id)
            if offer and update_offer:
                offer.name = updated_offer['name']
                offer.description = updated_offer['description']
                offer.user_id = updated_offer['user_id']
                offer.status = updated_offer['status']
                with db.session.begin():
                    db.session.commit()
                return make_response('Oferta Actualizada', 200)
            else:
                return make_response('No Content Data', 204)

        except Exception as e:
            return make_response(f'Ha ocurrido un error: {e}')
    else: 
        return('Ha ocurrido un error')
    
@require_content_type('aplication/JSON')
@offer.route('/offer/get/<id>')
def get_offer(id):
    offer = Offer.query.get(id)
    if offer:
        return jsonify(offer.to_dict())
    else:
        return make_response('No existe la oferta', 204)

@require_content_type('aplication/JSON')
@offer.route('/offer/get/list')
def get_offers():
    offers = Offer.query.all()
    offer_list = {}
    if offers:
        for offer in offers:
            offer_list[offer.id] = offer.to_dict()
        return jsonify(offer_list)
    else:
        return make_response('No hay ofertas', 204)