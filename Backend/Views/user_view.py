from flask import Blueprint, jsonify, request
from models import User
from extentions import db
from flask_jwt_extended import jwt_required, get_jwt_identity

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = [{'id': user.id, 'username': user.username} for user in users]
    return jsonify(user_list), 200

@user_bp.route('/users/profile', methods=['GET'])
@jwt_required()
def get_profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if user:
        user_data = {'id': user.id, 'username': user.username}
        return jsonify(user_data), 200
    return jsonify({"msg": "User not found"}), 404

@user_bp.route('/users/profile', methods=['PUT'])
@jwt_required()
def update_profile():
    user_id = get_jwt_identity()
    data = request.get_json()

    user = User.query.get(user_id)
    if not user:
        return jsonify({"msg": "User not found"}), 404

    new_username = data.get('username')
    new_password = data.get('password')

    if new_username:
        existing_user = User.query.filter_by(username=new_username).first()
        if existing_user:
            return jsonify({"msg": "Username already taken"}), 400
        user.update_username(new_username)

    if new_password:
        user.update_password(new_password)

    db.session.commit()

    return jsonify({"msg": "Profile updated successfully"}), 200

@user_bp.route('/users/profile', methods=['DELETE'])
@jwt_required()
def delete_profile():
    user_id = get_jwt_identity()

    user = User.query.get(user_id)
    if not user:
        return jsonify({"msg": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"msg": "User deleted successfully"}), 200
