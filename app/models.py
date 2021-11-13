from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Estudiante(db.Model):
    carne = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(64), index=True)
    carrera = db.Column(db.String(120), index=True)
    
    def __repr__(self):
        return '<Estudiante {}>'.format(self.nombre)

class Cita(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date)
    hora = db.Column(db.DateTime, index=True)
    carne = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<Cita {}>'.format(self.body)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
