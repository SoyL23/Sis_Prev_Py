from config.db import db
from flask import Blueprint, make_response, jsonify
from models.sell import Sell

sell = Blueprint('sell', __name__)