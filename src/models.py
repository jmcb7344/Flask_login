from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) 
    nombre = db.Column(db.String(100))
    email = db.Column(db.String(100))
    username = db.Column(db.String(100))
    password = db.Column(db.Text)

    def __str__(self) -> str:
        return f'Id: {self.id}: {self.nombre}, {self.email}, {self.username}'
