from flask import Blueprint, jsonify, request
from models import Category
from extentions import db

category_bp = Blueprint('category_bp', __name__)

@category_bp.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    category_list = [{'id': category.id, 'name': category.name} for category in categories]
    return jsonify(category_list), 200

@category_bp.route('/categories', methods=['POST'])
def add_category():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"msg": "Category name is required"}), 400

    category_name = data['name']
    existing_category = Category.query.filter_by(name=category_name).first()
    if existing_category:
        return jsonify({"msg": "Category already exists"}), 400

    new_category = Category(name=category_name)
    db.session.add(new_category)
    db.session.commit()

    return jsonify({"msg": "Category added successfully", "id": new_category.id, "name": new_category.name}), 201

@category_bp.route('/categories/<int:id>', methods=['PUT'])
def update_category(id):
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"msg": "Category name is required"}), 400

    category = Category.query.get(id)
    if not category:
        return jsonify({"msg": "Category not found"}), 404

    category.name = data['name']
    db.session.commit()

    return jsonify({"msg": "Category updated successfully", "id": category.id, "name": category.name}), 200

@category_bp.route('/categories/<int:id>', methods=['DELETE'])
def delete_category(id):
    category = Category.query.get(id)
    if not category:
        return jsonify({"msg": "Category not found"}), 404

    db.session.delete(category)
    db.session.commit()

    return jsonify({"msg": "Category deleted successfully"}), 200
