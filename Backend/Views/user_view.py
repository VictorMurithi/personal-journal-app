from flask import Blueprint, jsonify, request
from models import User
from extentions import db

user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/users', methods=['GET'])
def get_users():
    return jsonify(User.query.all())