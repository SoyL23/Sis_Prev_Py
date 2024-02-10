from config.db import db
from flask import Blueprint, make_response, jsonify, request, render_template
from models.role import Role
from services.require_content_type import require_content_type

role = Blueprint('role', __name__)
#------------------------------------------------------------------------------------Inicio
@require_content_type('aplication/JSON')
@role.route('/role/create', methods=['GET', 'POST'])
def create_role():
    if request.method == 'GET':
        try:
            return render_template('role_create')
        except Exception as e:
            return jsonify(f'Ha ocurrido un error: {e}')
    elif request.method == 'POST':
        role_data = request.get_json()
        try:
            if role_data != None:
                role_name = role_data['name']
                role_description = role_data['description']
                
                new_role = Role(name=role_name, description=role_description)
                with db.session.begin():
                    db.session.add(new_role)
                    db.session.commit()
                    
                return make_response('Se ha creado el rol', 200)
            else:
                return make_response('Invalid Data', 204)
        except Exception as e:
            return jsonify(f'Ha ocurrido un error: {e}')
#------------------------------------------------------------------------------------Fin

#------------------------------------------------------------------------------------Inicio
@require_content_type('aplication/JSON')
@role.route('/role/delete/<id>', methods=['POST'])
def delete_role(id):
    if request.method == 'POST':
        try:
            role = Role.query.get(id)
            if role != None:
                with db.session.begin():
                    db.session.delete(role)
                    db.session.commit()
                    
                return make_response('Se ha eliminado el rol', 200)
            else: 
                return make_response('Rol no Existe', 204)
        except Exception as e:
            return jsonify(f'Ha ocurrido un error: {e}')
    else:
        return make_response('Invalid Request', 415)
#------------------------------------------------------------------------------------Fin

#------------------------------------------------------------------------------------Inicio
@require_content_type('aplication/JSON')
@role.route('/role/update/<id>', methods=['POST'])
def update_role(id):
    if request.method == 'POST':
        role_update = request.get_json()
        role = Role.query.get(id)
        try:
            if role_update != None:
                role.name = role_update['name']
                role.description = role_update['description']
                with db.session.begin():
                    db.session.commit()
                return make_response('Rol actualizado', 200)
            else:
                return make_response('Rol no encontrado', 204)
        except Exception as e:
            return jsonify(f'Ha ocurrido un error: {e}')
    elif request.method == 'GET':
        render_template('role_update')
    else:
        return make_response('Invalid Request', 415)
#------------------------------------------------------------------------------------Fin

#------------------------------------------------------------------------------------Inicio
@require_content_type('aplication/JSON')
@role.route('/role/get/<id>', methods=['GET'])
def get_role(id):
    if request.method == 'GET':
        try:
            role = Role.query.get(id)
            return jsonify(role.to_dict())
        except Exception as e:
            return jsonify(f'Ha ocurrido un error: {e}')

@require_content_type('aplication/JSON')
@role.route('/role/get/list', methods=['GET'])
def get_role_list():
    if request.method == 'GET':
        roles = Role.query.all()
        list_roles = {}
        try:
            if roles:  
                for rol in roles:
                    list_roles[rol.id] = rol.to_dict()
                return jsonify(list_roles)
            else:
                return make_response('No hay Roles', 204)
        except Exception as e:
            return jsonify(f'Ha ocurrido un error: {e}')