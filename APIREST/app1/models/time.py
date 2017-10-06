from app import db
from app import manager

class Time(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    nome = db.Column(db.String(200))
    data = db.Column(db.DateTime)

db.create_all()
manager.create_api(Time, methods=['GET','POST','DELETE','PUT'])