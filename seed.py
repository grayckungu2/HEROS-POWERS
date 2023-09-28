from random import choice as rc
from faker import Faker
from flask import Flask
from models import db, Hero, Power, HeroPower
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

fake = Faker()
db.init_app(app)

# Function to create and add a hero with random data
def create_hero():
    name = fake.first_name()
    supername = fake.first_name()
    created_at = fake.date_time_this_decade()
    updated_at = fake.date_time_this_decade()
    
    hero = Hero(name=name, supername=supername, created_at=created_at, updated_at=updated_at)
    
    return hero

# Function to create and add a power with random data
def create_power():
    name = fake.word()
    description = fake.sentence()
    created_at = fake.date_time_this_decade()
    updated_at = fake.date_time_this_decade()
    
    power = Power(name=name, description=description, created_at=created_at, updated_at=updated_at)
    
    return power

# Function to create and add a HeroPower association with random data
def create_hero_power(hero, power):
    strength = fake.random_int(min=1, max=10)  # You can adjust the range as needed
    
    hero_power = HeroPower(strength=strength, hero=hero, power=power)
    
    return hero_power

# Create and add heroes, powers, and hero-power associations
def seed_database():
    for _ in range(10):  # You can adjust the number of heroes and powers you want to create
        hero = create_hero()
        power = create_power()
        
        db.session.add(hero)
        db.session.add(power)
        
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
        
        hero_power = create_hero_power(hero, power)
        db.session.add(hero_power)
    
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        seed_database()
