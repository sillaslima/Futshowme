from app import db
from app import manager

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Integer, primary_key=True)
    nascimento = db.Column(db.DateTime)
    cpf = db.Column(db.Integer, unique=True)
    email = db.Column(db.String(50), unique=True)
    time_id = db.Column(db.Integer, db.ForeignKey('time.id'))
    time = db.relationship('Time')
db.create_all()
manager.create_api(Cliente, methods=['GET','POST','DELETE','PUT'])