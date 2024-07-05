from flask import Blueprint, jsonify, request
from models import JournalEntry
from extentions import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime, timedelta

summary_bp = Blueprint('summary_bp', __name__)

def get_date_range(period):
    end_date = datetime.utcnow()
    if period == 'daily':
        start_date = end_date - timedelta(days=1)
    elif period == 'weekly':
        start_date = end_date - timedelta(weeks=1)
    elif period == 'monthly':
        start_date = end_date - timedelta(days=30)
    else:
        return None, None
    return start_date, end_date

@summary_bp.route('/summary/<period>', methods=['GET'])
@jwt_required()
def get_summary(period):
    user_id = get_jwt_identity()
    start_date, end_date = get_date_range(period)

    if not start_date or not end_date:
        return jsonify({"msg": "Invalid period specified"}), 400

    entries = JournalEntry.query.filter(JournalEntry.user_id == user_id, JournalEntry.date.between(start_date, end_date)).all()
    summary = {
        'total_entries': len(entries),
        'entries': [{'id': entry.id, 'title': entry.title, 'content': entry.content, 'date': entry.date.isoformat(), 'category': entry.category.name} for entry in entries]
    }
    return jsonify(summary), 200
