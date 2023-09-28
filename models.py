from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'hero'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, default=None)
    name = db.Column(db.String(255))
    super_name = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    hero_powers = db.relationship("HeroPower", back_populates="hero")

class Power(db.Model):
    __tablename__ = 'power'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True,  default=None)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship with the HeroPower model 
    power_heroes = db.relationship("HeroPower", back_populates="power")

class HeroPower(db.Model):
    __tablename__ = 'hero_power'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, default=None)
    strength = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Foreign key relationship
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'), nullable=False)
    
    power_id = db.Column(db.String(36), db.ForeignKey('power.id'), nullable=False)

    # Relationship  with Hero model 
    hero = db.relationship("Hero", back_populates="hero_powers")
    # Relationship with the Power model
    power = db.relationship("Power", back_populates="power_heroes")
