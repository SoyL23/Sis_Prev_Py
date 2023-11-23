from flask import Blueprint, render_template

demand = Blueprint('demand', __name__)

@demand.route('/demand/create')
def create_cemand():
    return render_template('demand_create.html')