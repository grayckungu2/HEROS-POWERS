from faker import Faker
from models.hero import Hero, db
from models.power import Power
from models.heropower import HeroPower
from sqlalchemy.exc import IntegrityError
from app import app, db

fake = Faker()

# Function to create and add a hero with random data
def create_hero():
    name = fake.first_name()
    super_name = fake.first_name()
    created_at = fake.date_time_this_decade()
    updated_at = fake.date_time_this_decade()

    hero = Hero(name=name, super_name=super_name, created_at=created_at, updated_at=updated_at)

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
    strength = fake.random_int(min=1, max=10)  

    hero_power = HeroPower(strength=strength, hero=hero, power=power)

    return hero_power

# Function to create and seed the database
def seed_database():
    for _ in range(10):  
        hero = create_hero()
        power = create_power()

        hero_power = create_hero_power(hero, power)
        db.session.add(hero_power)

    try:
        db.session.commit()
        print("Database seeded successfully!")
    except IntegrityError as e:
        db.session.rollback()
        print(f"IntegrityError: {str(e)}")
        print("Rolling back changes to the database.")

if __name__ == '__main__':
    with app.app_context():
        seed_database()
