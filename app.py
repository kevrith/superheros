from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_mail import Mail, Message
from models import db, Hero, Power, HeroPower
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)
mail = Mail(app)


@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Superheroes API"}), 200


# GET /heroes
@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    heroes_list = [hero.to_dict(only=('id', 'name', 'super_name')) for hero in heroes]
    return jsonify(heroes_list), 200


# GET /heroes/:id
@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)

    if not hero:
        return jsonify({"error": "Hero not found"}), 404

    hero_dict = hero.to_dict(only=('id', 'name', 'super_name', 'hero_powers'))

    # Format hero_powers to include nested power data
    formatted_hero_powers = []
    for hp in hero.hero_powers:
        hp_dict = {
            'id': hp.id,
            'hero_id': hp.hero_id,
            'power_id': hp.power_id,
            'strength': hp.strength,
            'power': hp.power.to_dict(only=('id', 'name', 'description'))
        }
        formatted_hero_powers.append(hp_dict)

    hero_dict['hero_powers'] = formatted_hero_powers

    return jsonify(hero_dict), 200


# GET /powers
@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    powers_list = [power.to_dict(only=('id', 'name', 'description')) for power in powers]
    return jsonify(powers_list), 200


# GET /powers/:id
@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)

    if not power:
        return jsonify({"error": "Power not found"}), 404

    return jsonify(power.to_dict(only=('id', 'name', 'description'))), 200


# PATCH /powers/:id
@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)

    if not power:
        return jsonify({"error": "Power not found"}), 404

    data = request.get_json()

    try:
        if 'description' in data:
            power.description = data['description']

        db.session.commit()
        return jsonify(power.to_dict(only=('id', 'name', 'description'))), 200

    except ValueError as e:
        db.session.rollback()
        return jsonify({"errors": [str(e)]}), 400


# POST /hero_powers
@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()

    try:
        # Validate that hero and power exist
        hero = Hero.query.get(data.get('hero_id'))
        power = Power.query.get(data.get('power_id'))

        if not hero or not power:
            return jsonify({"errors": ["Hero or Power not found"]}), 404

        # Create new HeroPower
        new_hero_power = HeroPower(
            strength=data.get('strength'),
            hero_id=data.get('hero_id'),
            power_id=data.get('power_id')
        )

        db.session.add(new_hero_power)
        db.session.commit()

        # Return formatted response
        response = {
            'id': new_hero_power.id,
            'hero_id': new_hero_power.hero_id,
            'power_id': new_hero_power.power_id,
            'strength': new_hero_power.strength,
            'hero': new_hero_power.hero.to_dict(only=('id', 'name', 'super_name')),
            'power': new_hero_power.power.to_dict(only=('id', 'name', 'description'))
        }

        return jsonify(response), 201

    except ValueError as e:
        db.session.rollback()
        return jsonify({"errors": [str(e)]}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": ["validation errors"]}), 400


# Helper route to send test email
@app.route('/send-test-email', methods=['POST'])
def send_test_email():
    try:
        data = request.get_json()
        recipient = data.get('recipient', app.config['MAIL_DEFAULT_SENDER'])

        msg = Message(
            subject='Test Email from Superheroes API',
            recipients=[recipient],
            body='This is a test email from the Flask Superheroes API. Flask-Mail is configured correctly!'
        )

        mail.send(msg)
        return jsonify({"message": f"Test email sent successfully to {recipient}"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(port=5555, debug=True)
