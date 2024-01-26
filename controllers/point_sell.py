from config.db import db
from flask import Blueprint, make_response, jsonify, request, render_template
from models.point_sell import PointSell
from services.require_content_type import require_content_type

point_sell = Blueprint('point_sell', __name__)

@require_content_type('aplication/JSON')
@point_sell.route('/point_sell/create', methods=['GET', 'POST'])
def create_point_sell():
    if request.method == 'GET':
        try:
            return render_template('create_point_sell')
        except Exception as e:
            return jsonify(f'Ha ocurrido un error: {e}')
    elif request.method == 'POST':
        point_sell_data = request.get_json()
        try:
            if point_sell_data:
                name = point_sell_data['name']
                address = point_sell_data['address']
                phone = point_sell_data['phone']
                email = point_sell_data['email']
                status = point_sell_data['status']
                city_id = point_sell_data['city_id']
                user_id = point_sell_data['user_id']
                cooperative_id = point_sell_data['cooperative_id']

                sell_point = PointSell(name=name,address=address,phone=phone,email=email,
                                       status=status,city_id=city_id, user_id=user_id,
                                        cooperative_id=cooperative_id)
                with db.session.begin():
                    db.session.add(sell_point)
                    db.session.commit()
                    db.session.close()
            else:
                return make_response('Faltan Datos', 400)
        except Exception as e:
            return jsonify(f'Ha ocurrido un error: {e}')
        pass
    pass
#------------------------------------------------------------------------------------Fin

#------------------------------------------------------------------------------------Inicio
@require_content_type('aplication/JSON')
@point_sell.route('/point_sell/delete/<id>', methods=['GET', 'POST'])
def delete_point_sell(id):

    if request.method == 'POST':
        sell_point = PointSell.query.get(id)
        try:
            if sell_point:
                with db.session.begin():
                    db.session.delete(point_sell)
                    db.session.commit()
                    
                return make_response('Punto de Venta Eliminado', 200)
            else:
                return make_response('Punto de Venta no encontrado', 204)
        except Exception as e:
            return jsonify(f'Ha ocurrido un error: {e}')
    else:
        return make_response('Invalid Request', 400)

#------------------------------------------------------------------------------------Fin

#------------------------------------------------------------------------------------Inicio
@require_content_type('aplication/JSON')
@point_sell.route('/point_sell/update/<id>', methods=['GET', 'POST'])
def update_point_sell(id):
    if request.method == 'POST':
        point_sell_data = request.get_json()
        sell_point = PointSell.query.get(id)
        try:
            if point_sell_data:
                sell_point.name = point_sell_data['name']
                sell_point.address = point_sell_data['address']
                sell_point.phone = point_sell_data['phone']
                sell_point.email = point_sell_data['email']
                sell_point.city_id = point_sell_data['city_id']
                sell_point.user_id = point_sell_data['user_id']
                sell_point.cooperative_id = point_sell_data['cooperative_id']
                with db.session.begin():
                    db.session.commit()
                return make_response('Punto de Venta Actualizado', 200)
            else:
                return make_response('Punto de Venta no Encontrado', 204)
        except Exception as e:
            return jsonify(f'Ha ocurrido un error: {e}')
#------------------------------------------------------------------------------------Fin

#------------------------------------------------------------------------------------Inicio
@require_content_type('aplication/JSON')
@point_sell.route('/point_sell/get/<id>', methods=['GET', 'POST'])
def get_point_sell(id):
    if request.method == 'GET':
        sell_point = PointSell.query.get(id)
        try:
            if sell_point:
                return jsonify(sell_point.to_dict())
            else:
                return make_response('Punto de Venta No Encontrado', 204)
        except Exception as e:
            return jsonify(f'Ha ocurrido un error: {e}')

@require_content_type('aplication/JSON')
@point_sell.route('/point_sell/get/list', methods=['GET', 'POST'])
def get_point_sell_list():
    if request.method == 'GET':
        sell_points = PointSell.query.all()
        list_points = {}
        try:
            if sell_points:
                for sell_point in sell_points:
                    list_points[sell_point.id] = sell_point.to_dict()
                return jsonify(list_points)
            else:
                return make_response('No hay puntos de Venta', 204)
        except Exception as e:
            return jsonify(f'Ha ocurrido un error: {e}')
