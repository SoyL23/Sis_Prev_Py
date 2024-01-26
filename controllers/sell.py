from config.db import db
from flask import Blueprint, make_response, jsonify, request
from models.sell import Sell
from services.require_content_type import require_content_type

sell = Blueprint('sell', __name__)

#------------------------------------------------------------------------------------Inicio
@require_content_type('aplication/JSON')
@sell.route('/sell/create', methods=['GET', 'POST'])
def create_sell():
    if request.method == 'GET':
        try:
            pass
        except Exception as e:
            return jsonify(f'Ha ocurrido un error: {e}')
    elif request.method == 'POST':
        sell_data = request.get_json()
        try:
            pass
        except Exception as e:
            return jsonify(f'Ha ocurrido un error: {e}')
        pass
    pass
#------------------------------------------------------------------------------------Fin

#------------------------------------------------------------------------------------Inicio
@require_content_type('aplication/JSON')
@sell.route('/sell/delete/<id>', methods=['GET', 'POST'])
def delete_sell(id):
    if request.method == 'GET':
        try:
            pass
        except Exception as e:
            return jsonify(f'Ha ocurrido un error: {e}')
    elif request.method == 'POST':
        sell_data = request.get_json()
        try:
            pass
        except Exception as e:
            return jsonify(f'Ha ocurrido un error: {e}')
        pass
    pass
#------------------------------------------------------------------------------------Fin

#------------------------------------------------------------------------------------Inicio
@require_content_type('aplication/JSON')
@sell.route('/sell/update/<id>', methods=['GET', 'POST'])
def update_sell(id):
    if request.method == 'GET':
        try:
            pass
        except Exception as e:
            return jsonify(f'Ha ocurrido un error: {e}')
    elif request.method == 'POST':
        sell_data = request.get_json()
        try:
            pass
        except Exception as e:
            return jsonify(f'Ha ocurrido un error: {e}')
        pass
    pass

#------------------------------------------------------------------------------------Fin

#------------------------------------------------------------------------------------Inicio
@require_content_type('aplication/JSON')
@sell.route('/sell/get/<id>', methods=['GET', 'POST'])
def get_sell(id):
    if request.method == 'GET':
        try:
            pass
        except Exception as e:
            return jsonify(f'Ha ocurrido un error: {e}')
    elif request.method == 'POST':
        sell_data = request.get_json()
        try:
            pass
        except Exception as e:
            return jsonify(f'Ha ocurrido un error: {e}')
        pass
    pass

@require_content_type('aplication/JSON')
@sell.route('/sell/get/list', methods=['GET', 'POST'])
def get_sell_list():
    if request.method == 'GET':
        try:
            pass
        except Exception as e:
            return jsonify(f'Ha ocurrido un error: {e}')
    elif request.method == 'POST':
        sell_data = request.get_json()
        try:
            pass
        except Exception as e:
            return jsonify(f'Ha ocurrido un error: {e}')
        pass
    pass