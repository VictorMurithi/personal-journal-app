from flask import Blueprint, request, jsonify
from models import User
from flask_jwt_extended import unset_jwt_cookies, jwt_required
from extentions import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"msg": "Request body is missing or invalid"}), 400
        
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"msg": "Username and password are required"}), 400

        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            return jsonify({"msg": "Invalid credentials"}), 401

        # If credentials are valid, generate access token
        access_token = create_access_token(identity=user.id, expires_delta=False)

        response_data = {
            "message": "Login successful",
            "access_token": access_token
        }

        return jsonify(response_data), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"msg": "An error occurred while processing your request"}), 500


@auth_bp.route("/sign-up", methods=["POST"])
def sign_up():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"msg": "request body is missing or invalid"}), 400
        
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"msg": "username and password are required"}), 400
        

        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        access_token = create_access_token(identity=new_user.id, expires_delta=False)
        
        response_data = {
            "message": "Sign-up successful",
            "access_token": access_token
        }

        return jsonify(response_data), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"msg": "An error occurred while processing your request"}), 500

@auth_bp.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    response = jsonify({"success": "Logged out successfully!"})
    unset_jwt_cookies(response)  # Clear JWT cookie
    return response, 201

@auth_bp.route("/forgot-password", methods=["POST"])
def forgot_password():
    new_password = request.get_json().get("new_password")
    email = request.get_json().get("email")

    if not new_password or not email:
        return jsonify({"msg": "new_password and email are required"}), 400

    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({"msg": "User not found"}), 404

    hashed_password = generate_password_hash(new_password)
    user.password = hashed_password
    db.session.commit()

    return jsonify({"msg": "Password reset successful"}), 200
