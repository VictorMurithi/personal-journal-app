from flask import Blueprint, request, jsonify
from models import JournalEntry, db
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime

journal_bp = Blueprint('journal_bp', __name__)

# Add a new journal entry
@journal_bp.route('/journal', methods=['POST'])
@jwt_required()
def add_journal_entry():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"msg": "Request body is missing or invalid"}), 400
        
        title = data.get('title')
        content = data.get('content')
        category = data.get('category')
        date = data.get('date')

        if not title or not content or not category or not date:
            return jsonify({"msg": "Title, content, category, and date are required"}), 400
        
        user_id = get_jwt_identity()
        new_entry = JournalEntry(title=title, content=content, category=category, date=datetime.strptime(date, '%Y-%m-%d'), user_id=user_id)
        db.session.add(new_entry)
        db.session.commit()

        return jsonify({"msg": "Journal entry added successfully"}), 201

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"msg": "An error occurred while processing your request"}), 500

# Edit an existing journal entry
@journal_bp.route('/journal/<int:entry_id>', methods=['PUT'])
@jwt_required()
def edit_journal_entry(entry_id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"msg": "Request body is missing or invalid"}), 400

        title = data.get('title')
        content = data.get('content')
        category = data.get('category')
        date = data.get('date')

        entry = JournalEntry.query.get_or_404(entry_id)
        if entry.user_id != get_jwt_identity():
            return jsonify({"msg": "You are not authorized to edit this entry"}), 403

        if title:
            entry.title = title
        if content:
            entry.content = content
        if category:
            entry.category = category
        if date:
            entry.date = datetime.strptime(date, '%Y-%m-%d')

        db.session.commit()

        return jsonify({"msg": "Journal entry updated successfully"}), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"msg": "An error occurred while processing your request"}), 500

# Delete a journal entry
@journal_bp.route('/journal/<int:entry_id>', methods=['DELETE'])
@jwt_required()
def delete_journal_entry(entry_id):
    try:
        entry = JournalEntry.query.get_or_404(entry_id)
        if entry.user_id != get_jwt_identity():
            return jsonify({"msg": "You are not authorized to delete this entry"}), 403

        db.session.delete(entry)
        db.session.commit()

        return jsonify({"msg": "Journal entry deleted successfully"}), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"msg": "An error occurred while processing your request"}), 500

# View a list of all journal entries
@journal_bp.route('/journal', methods=['GET'])
@jwt_required()
def view_all_journal_entries():
    try:
        user_id = get_jwt_identity()
        entries = JournalEntry.query.filter_by(user_id=user_id).all()
        response_data = [
            {
                "id": entry.id,
                "title": entry.title,
                "content": entry.content,
                "category": entry.category,
                "date": entry.date.strftime('%Y-%m-%d')
            }
            for entry in entries
        ]

        return jsonify(response_data), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"msg": "An error occurred while processing your request"}), 500
