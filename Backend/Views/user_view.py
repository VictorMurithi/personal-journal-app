from models import *
from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from datetime import datetime

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/user", methods=["GET"])
@jwt_required()
def get_user():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if user:
        return jsonify(
            {
                "username": user.username,
                "email": user.email
            }
        ),200
    else:
        return jsonify({"message": "User not found"}), 404