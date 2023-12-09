from flask import Blueprint, render_template, request, redirect, url_for
from config.db import db
from models.user import User
from validaciones.user import Validar_User

validar = Validar_User()

user = Blueprint('user', __name__)

@user.route('/')
def index():
    return'El servidor esta correcto'

@user.route('/login')
def login():
    return render_template('')

@user.route('/user_update/<id>', methods =['POST', 'GET'])
def user_update(id):
    user = User.query.get(id)
    if request.method == 'POST':
        user.nombre = request.form["nombre"]
        user.apellido = request.form["apellido"]
        user.email = request.form["email"]
        user.username = request.form["username"]
        user.password = request.form["password"]
        user.celular = request.form["celular"]
        user.ciudad = request.form["ciudad"]
        
        db.session.commit()
        return redirect('/user/create')

    return render_template('user_update.html', user=user)

#------------------------------------------------------------------delete
@user.route('/user/delete/<id>') #recibe del href el id y lo pasa a la funcion
def user_delete(id):#aquí la función recibe el id
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    
    return redirect('/user/create')
   # return render_template('user_delete.html')
   # return "se eliminó  el usuario"

#---------------------------------------------------------------------create
@user.route('/user/create')
def user_create():
    users=User.query.all() #esto es como hacer Select * para hacer lista
    return render_template('user_create.html', users=users) # se agrega products para pasar la lista

@user.route('/user/new', methods=['POST']) # al enviar el usuario los datos, se activa el user_new
def user_new():
    data= request.form
    nombre = (nombre := validar.validar_apellido(data['nombre']))
    print(nombre)
    # apellido = data['apellido']
    # email = data['email']
    # username = data['username']
    # password= data['password']
    # celular = data['celular']
    # ciudad = data['ciudad']

    # user_new = User(nombre, apellido, email, username,  password, celular, ciudad)
    # db.session.add(user_new)
    # db.session.commit()

    return redirect('/user/create')