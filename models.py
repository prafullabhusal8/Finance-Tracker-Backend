
# =========================
# models.py
# =========================
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    role = db.Column(db.String(20))

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(10))
    category = db.Column(db.String(50))
    date = db.Column(db.Date, default=datetime.utcnow)
    notes = db.Column(db.String(200))
