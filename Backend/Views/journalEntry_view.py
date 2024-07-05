from flask import Blueprint, jsonify, request
from models import JournalEntry
from extentions import db

journalEntry_bp = Blueprint('journalEntry_bp', __name__)


@journalEntry_bp.route('/journal_entries', methods=['GET'])
def get_journal_entries():
    return jsonify(JournalEntry.query.all())