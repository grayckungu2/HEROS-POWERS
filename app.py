
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def home():
    return 'Welcome to the Superheroes API'

# GET all heroes
@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    # Convert Hero objects to a list of dictionaries
    hero_data = [{"id": hero.id, "name": hero.name, "super_name": hero.super_name} for hero in heroes]
    return jsonify(hero_data), 200


# GET hero by ID
#http://127.0.0.1:5000/heroes/<hero_>

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)

    if not hero:
        return jsonify({"error": "Hero not found"}), 404

    hero_data = {
        "id": hero.id,
        "name": hero.name,
        "super_name": hero.super_name,  
        "created_at": hero.created_at,
        "updated_at": hero.updated_at
    }

    return jsonify(hero_data), 200


# GET all powers
@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    # Convert Power objects to a list of dictionaries
    power_data = [{"id": power.id, "name": power.name, "description": power.description} for power in powers]
    return jsonify(power_data), 200

# GET power by ID
@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)

    if not power:
        return jsonify({"error": "Power not found"}), 404

    power_data = {
        "id": power.id,
        "name": power.name,
        "description": power.description,
        "created_at": power.created_at,
        "updated_at": power.updated_at
    }

    return jsonify(power_data), 200

# PATCH power by ID
@app.route('/powers/<int:id>', methods=['PATCH'])
def patch_power(id):
    power = Power.query.get(id)

    if not power:
        return jsonify({"error": "Power not found"}), 404

    data = request.get_json()
    description = data.get('description')

    if not description:
        return jsonify({"error": "Description is required"}), 400

    power.description = description

    try:
        db.session.commit()
        return jsonify({
            "id": power.id,
            "name": power.name,
            "description": power.description,
            "created_at": power.created_at,
            "updated_at": power.updated_at
        }), 200
    except IntegrityError:
        db.session.rollback()
        return jsonify({"errors": ["Validation errors"]}), 400


# POST Hero power
# url = 'http://127.0.0.1:5000/hero_powers'
@app.route('/hero_powers', methods=['POST'])
def post_hero_power():
    data = request.get_json()
    strength = data.get('strength')
    power_id = data.get('power_id')
    hero_id = data.get('hero_id')

    if not strength or not power_id or not hero_id:
        return jsonify({"error": "Strength, power_id, and hero_id are required"}), 400

    hero = Hero.query.get(hero_id)
    power = Power.query.get(power_id)

    if not hero or not power:
        return jsonify({"error": "Hero or Power not found"}), 404

    hero_power = HeroPower(strength=strength, hero=hero, power=power)

    try:
        db.session.add(hero_power)
        db.session.commit()

        hero_data = {
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name, 
            "powers": [
                {
                    "id": power.id,
                    "name": power.name,
                    "description": power.description
                }
            ]
        }

        return jsonify(hero_data), 200
    except IntegrityError:
        db.session.rollback()
        return jsonify({"errors": ["Validation errors"]}), 400

        