from models import Transaction, db
from sqlalchemy import func

def get_summary():
    income = db.session.query(func.sum(Transaction.amount)).filter_by(type='income').scalar() or 0
    expense = db.session.query(func.sum(Transaction.amount)).filter_by(type='expense').scalar() or 0
    return {
        'total_income': income,
        'total_expense': expense,
        'balance': income - expense
    }