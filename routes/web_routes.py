from flask import Blueprint, render_template, request, redirect
from models import db, Transaction
from services.summary_service import get_summary
from datetime import datetime
from validators import validate_transaction

web_bp = Blueprint('web', __name__)

@web_bp.route('/')
def home():
    return render_template('index.html')

@web_bp.route('/transactions')
def transactions():
    data = Transaction.query.all()
    return render_template('transactions.html', transactions=data)



"""
@web_bp.route('/add', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        data = request.form
        txn = Transaction(
            amount=data['amount'],
            type=data['type'],
            category=data['category'],
            date=datetime.strptime(data['date'], '%Y-%m-%d')
        )
        db.session.add(txn)
        db.session.commit()
        return redirect('/transactions')

    return render_template('add_transaction.html')
"""

@web_bp.route('/add', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        data = request.form

        # ✅ Validate
        error = validate_transaction(data)    
        if error:
            return render_template('add_transaction.html', error=error)

        try:
            txn = Transaction(
                amount=float(data['amount']),
                type=data['type'],
                category=data['category'],
                date=datetime.strptime(data['date'], '%Y-%m-%d')
            )
            db.session.add(txn)
            db.session.commit()

            return redirect('/transactions')

        except Exception as e:
            return render_template('add_transaction.html', error=str(e))

    return render_template('add_transaction.html')


@web_bp.route('/summary')
def summary_page():
    data = get_summary()
    return render_template('summary.html', summary=data)
