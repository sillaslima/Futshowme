from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager


app = Flask(__name__)


#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/test.db'
db = SQLAlchemy(app)
manager = APIManager(app, flask_sqlalchemy_db=db)

#class Usuario(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    nome = db.Column(db.String(100))
#db.create_all()
