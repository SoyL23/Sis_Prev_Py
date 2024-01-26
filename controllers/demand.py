from config.db import db
from flask import Blueprint, make_response, jsonify
from models.demand import Demand

demand = Blueprint('demand', __name__)