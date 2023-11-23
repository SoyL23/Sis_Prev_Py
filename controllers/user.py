from flask import Blueprint, render_template, request, redirect
from config.db import db
from models.user import User

user = Blueprint('user', __name__)

@user.route('/login')
def login():
    return render_template('')

@user.route('/user/create')
def user_create():
    return render_template('user_create.html')

@user.route('/user/new', methods=['POST'])
def user_new():
    
    data = request.form

    nombre = data['nombre']
    apellido = data['apellido']
    username = data['username']
    email = data['email']
    password = data['password']
    con_password = data['confirm-password']
    num_celular = data['celular']
    ciudad = data['ciudad']

    fullname = nombre +" "+ apellido

    user_new = User(fullname, username, email, password, num_celular, ciudad)

    db.session.add(user_new)
    db.session.commit()

    return redirect('/user/create')