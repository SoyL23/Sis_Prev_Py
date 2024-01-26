from config.db import db
from flask import Blueprint, make_response, jsonify
from models.point_sell import PointSell

point_sell = Blueprint('point_sell', __name__)