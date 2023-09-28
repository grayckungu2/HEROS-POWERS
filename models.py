from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData  
from sqlalchemy.orm import relationship

# metadata with naming convention
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

# Initialize SQLAlchemy 
db = SQLAlchemy(metadata=metadata)

#  Hero model
class Hero(db.Model):
    __tablename__ = 'hero'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    supername = db.Column(db.String(255))
    created_at = db.Column(db.String(255))
    updated_at = db.Column(db.String(255))
#relationship between Hero and HeroPower
    hero_powers = relationship("HeroPower", back_populates="hero")
# Power model
class Power(db.Model):
    __tablename__ = 'power'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    created_at = db.Column(db.String(255))
    updated_at = db.Column(db.String(255))

#relationship between Power and HeroPower
    power_heroes = relationship("HeroPower", back_populates="power")

# HeroPower model
class HeroPower(db.Model):
    __tablename__ = 'hero_power'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.Integer)

    # foreign keys for Hero and Power
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('power.id'), nullable=False)
    

    # relationships between HeroPower, Hero, and Power
    hero = relationship("Hero", back_populates="hero_powers")
    power = relationship("Power", back_populates="power_heroes")
