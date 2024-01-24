from flask import Blueprint, render_template, request, make_response, jsonify
from config.db import db
from models.user import User
from validaciones.user import Validar_User
from controllers.require_content_type import require_content_type
validar = Validar_User()

user = Blueprint('user', __name__)

#------------------------------------------------------------------------------------Inicio Create User
    
@require_content_type('aplication/JSON')
@user.route('/user/create',  methods=['GET', 'POST'])
def user_create():
    
    if request.method == 'GET':
        try:
            return render_template('user_create')
        except Exception as e:
            return 'Ha ocurrido un error: ' + str(e)
    elif request.method == 'POST':
        user_data = request.get_json()
        if user_data:
            try:
                first_name = user_data['first_name']
                last_name = user_data['last_name']
                email = user_data['email']
                username = user_data['username']
                password= user_data['password']
                cellphone = user_data['cellphone']
                city_id = user_data['city_id']
                role_id = user_data['role_id']
                user_new = User(first_name, last_name, email, username,  password, cellphone, city_id,role_id)
                db.session.add(user_new)
                db.session.commit()
                return make_response('Se ha creado el usuario', 200)
            except Exception as e:
                return 'Ha ocurrido un error: ' + str(e)
        else:
            return make_response('Ha ocurrido un error: Hay campos vacíos')
    else:
        make_response('Metodo HTTP Inválido', 415)

#------------------------------------------------------------------------------------Fin Create User
        
#------------------------------------------------------------------------------------Inicio Read User

@require_content_type('aplication/JSON')
@user.route('/user/get/list')
def get_users():
    try:
        user_list = {}
        users = User.query.all()
        if users != None:
            for user in users:
                user_list[user.id] = user.to_dict()
            return jsonify(user_list)
        else:
            return make_response('No hay usuarios')
    except Exception as e:
        return 'Ha ocurrido un error: ' + str(e)
    
@user.route('/user/get/<id>')
def get_user(id):
     user = User.query.get(id)
     return jsonify(user.to_dict())
#------------------------------------------------------------------------------------Fin Read User

#------------------------------------------------------------------------------------Inicio Update User

@require_content_type('aplication/JSON')
@user.route('/user/update/<id>', methods =['POST', 'GET'])
def user_update(id):
    user_updated = request.get_json()
    if request.method == 'POST':
        user = User.query.get(id)
        if user != None:
            user.first_name = user_updated['first_name']
            user.last_name = user_updated["last_name"]
            user.email = user_updated["email"]
            user.username = user_updated["username"]
            user.password = user_updated["password"]
            user.cellphone = user_updated["cellphone"]
            user.city_id = user_updated["city_id"]
            user.role_id = user_updated["role_id"]
            db.session.commit()
            return make_response('Usuario Modificado', 200)
        else: 
            return make_response('Usuario no Encontrado')
    elif request.method == 'GET':
        return 'waiting'
    
#------------------------------------------------------------------------------------Fin Update User

#------------------------------------------------------------------------------------Inicio Delete User
@require_content_type('aplication/JSON')
@user.route('/user/delete/<id>') 
def user_delete(id):
    try:
        user = User.query.get(id)
        if user != None:
            db.session.delete(user)
            db.session.commit()
            return make_response('Usuario eliminado', 200)
        else: 
            return make_response('Usuario no Encontrado')
    except Exception as e:
        return 'Ha ocurrido un error: ' + str(e)
#------------------------------------------------------------------------------------End Delete User