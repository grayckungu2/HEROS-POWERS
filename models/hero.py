from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

# Creating a variable for the SQLAlchemy instance
db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    super_name = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship with HeroPower model
    hero_powers = db.relationship("HeroPower", back_populates="hero")

    def __init__(self, name, super_name):
        self.name = name
        self.super_name = super_name

class Power(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship with HeroPower model
    power_heroes = db.relationship("HeroPower", back_populates="power")

    def __init__(self, name, description):
        self.name = name
        self.description = description




from datetime import datetime

from .dbconfig import db

class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    super_name = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship with HeroPower model
    hero_powers = db.relationship("HeroPower", back_populates="hero")

    def __init__(self, name, super_name):
        self.name = name
        self.super_name = super_name

