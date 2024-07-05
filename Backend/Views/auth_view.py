from models import User
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

auth_bp = Blueprint("auth_bp", __name__)


@auth_bp.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"msg": "request body is missing or invalid"}), 400
        
        email = data.get["email"]
        password = data.get["password"]

        if not email or not password:
            return jsonify({"msg": "email and password are required"}), 400
        
        user = User.query.filter_by(email=email).first()
        if not user :
            return jsonify({"msg": "Invalid email or password"}), 404

        if not check_password_hash(user.password_hash, password):
            return jsonify({"msg": "Invalid email or password"}), 404

        access_token = create_access_token(identity=user.id, expires_delta=False)
        
        response_data = {
            "message": "Login successful",
            "access_token": access_token
        }

        return jsonify(response_data), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"msg": "An error occurred while processing your request"}), 500