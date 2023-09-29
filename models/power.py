from datetime import datetime
from .dbconfig import db


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

