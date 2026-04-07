def validate_transaction(data):
    if 'amount' not in data:
        return "Amount is required"

    if float(data['amount']) <= 0:
        return "Amount must be positive"

    if data.get('type') not in ['income', 'expense']:
        return "Invalid transaction type"

    if not data.get('category'):
        return "Category is required"

    if not data.get('date'):
        return "Date is required"

    return None