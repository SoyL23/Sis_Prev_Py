from flask import Blueprint, send_from_directory, render_template

home = Blueprint('home', __name__)

@home.route('/')
def index():
    return('El servidor esta activo')
