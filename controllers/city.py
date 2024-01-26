from config.db import db
from flask import Blueprint, make_response, jsonify
from models.city import City

city = Blueprint('city', __name__)