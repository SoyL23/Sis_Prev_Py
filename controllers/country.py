from config.db import db
from flask import Blueprint, make_response, jsonify
from models.country import Country

country = Blueprint('country', __name__)