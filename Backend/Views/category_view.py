from flask import Blueprint, jsonify, request
from models import Category
from extentions import db

category_bp = Blueprint('category_bp', __name__)


@category_bp.route('/categories', methods=['GET'])
def get_categories():
    return jsonify(Category.query.all())