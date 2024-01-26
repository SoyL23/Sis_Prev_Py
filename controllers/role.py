from config.db import db
from flask import Blueprint, make_response, jsonify
from models.role import Role

role = Blueprint('role', __name__)