from flask import Blueprint, render_template, request, redirect

product = Blueprint('product', __name__)

@product.route('/product/create')
def create_product():
    return render_template('product_create.html')

@product.route('/product/new', methods=['POST'])
def new_product():
    data = request.form
    nombre_producto = data['nombre_producto']
    proveedor = data['proveedor']
    return redirect('/product/create')