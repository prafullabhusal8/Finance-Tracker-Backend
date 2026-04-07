from flask import Blueprint, request, jsonify
from models import db, Transaction
from datetime import datetime
from services.summary_service import get_summary

api_bp = Blueprint('api', __name__)


# CREATE

@api_bp.route('/transactions', methods=['POST'])
def create_transaction():
    data = request.json
    try:
        txn = Transaction(
            amount=data['amount'],
            type=data['type'],
            category=data['category'],
            date=datetime.strptime(data['date'], '%Y-%m-%d'),
            notes=data.get('notes')
        )
        db.session.add(txn)
        db.session.commit()
        return jsonify({'message': 'Created'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# READ
@api_bp.route('/transactions', methods=['GET'])
def get_transactions():
    txns = Transaction.query.all()
    result = []
    for t in txns:
        result.append({
            'id': t.id,
            'amount': t.amount,
            'type': t.type,
            'category': t.category,
            'date': str(t.date)
        })
    return jsonify(result)


# UPDATE
@api_bp.route('/transactions/<int:id>', methods=['PUT'])
def update_transaction(id):
    txn = Transaction.query.get(id)
    if not txn:
        return jsonify({'error': 'Not found'}), 404

    data = request.json
    txn.amount = data.get('amount', txn.amount)
    txn.type = data.get('type', txn.type)
    txn.category = data.get('category', txn.category)
    db.session.commit()
    return jsonify({'message': 'Updated'})


# DELETE
@api_bp.route('/transactions/<int:id>', methods=['DELETE'])
def delete_transaction(id):
    txn = Transaction.query.get(id)
    if not txn:
        return jsonify({'error': 'Not found'}), 404

    db.session.delete(txn)
    db.session.commit()
    return jsonify({'message': 'Deleted'})

# SUMMARY
@api_bp.route('/summary', methods=['GET'])
def summary():
    return jsonify(get_summary())
