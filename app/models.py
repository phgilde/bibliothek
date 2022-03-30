from app import db
from app import app
from datetime import date


class Book(db.Model):
    isbn = db.Column(db.String(32), primary_key=True)
    is_borrowed = db.Column(db.Boolean)
    borrower_id = db.Column(db.Integer, db.ForeignKey("student.id_"))


class Student(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    books_borrowed = db.relationship("Book", backref="borrower", lazy="dynamic")
    email = db.Column(db.String(32))
    phone_number = db.Column(db.BigInteger)
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    tutor = db.Column(db.String(32))
