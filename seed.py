from app import app
from models import db, Hero, Power, HeroPower
import random

def seed_database():
    with app.app_context():
        print("Starting seed...")

        # Delete all existing data
        print("Clearing existing data...")
        HeroPower.query.delete()
        Hero.query.delete()
        Power.query.delete()

        # Create heroes
        print("Creating heroes...")
        heroes_data = [
            {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
            {"name": "Doreen Green", "super_name": "Squirrel Girl"},
            {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
            {"name": "Janet Van Dyne", "super_name": "The Wasp"},
            {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
            {"name": "Carol Danvers", "super_name": "Captain Marvel"},
            {"name": "Jean Grey", "super_name": "Dark Phoenix"},
            {"name": "Ororo Munroe", "super_name": "Storm"},
            {"name": "Kitty Pryde", "super_name": "Shadowcat"},
            {"name": "Elektra Natchios", "super_name": "Elektra"}
        ]

        heroes = []
        for hero_data in heroes_data:
            hero = Hero(**hero_data)
            heroes.append(hero)
            db.session.add(hero)

        # Create powers
        print("Creating powers...")
        powers_data = [
            {
                "name": "super strength",
                "description": "gives the wielder super-human strengths"
            },
            {
                "name": "flight",
                "description": "gives the wielder the ability to fly through the skies at supersonic speed"
            },
            {
                "name": "super human senses",
                "description": "allows the wielder to use her senses at a super-human level"
            },
            {
                "name": "elasticity",
                "description": "can stretch the human body to extreme lengths"
            },
            {
                "name": "telekinesis",
                "description": "allows the wielder to move objects with their mind without physical interaction"
            },
            {
                "name": "telepathy",
                "description": "gives the wielder the ability to read and communicate through thoughts"
            },
            {
                "name": "energy manipulation",
                "description": "allows the wielder to generate and control various forms of energy"
            },
            {
                "name": "weather control",
                "description": "gives the wielder the ability to manipulate and control weather patterns"
            },
            {
                "name": "invisibility",
                "description": "allows the wielder to become invisible to the naked eye at will"
            },
            {
                "name": "martial arts mastery",
                "description": "provides expert-level knowledge and skill in various martial arts forms"
            }
        ]

        powers = []
        for power_data in powers_data:
            power = Power(**power_data)
            powers.append(power)
            db.session.add(power)

        # Commit heroes and powers first
        db.session.commit()

        # Create hero_powers (associations)
        print("Creating hero-power associations...")
        strengths = ["Strong", "Weak", "Average"]

        # Assign 1-3 powers to each hero
        for hero in heroes:
            num_powers = random.randint(1, 3)
            selected_powers = random.sample(powers, num_powers)

            for power in selected_powers:
                hero_power = HeroPower(
                    hero_id=hero.id,
                    power_id=power.id,
                    strength=random.choice(strengths)
                )
                db.session.add(hero_power)

        db.session.commit()

        print("Seed completed successfully!")
        print(f"Created {len(heroes)} heroes")
        print(f"Created {len(powers)} powers")
        print(f"Created {HeroPower.query.count()} hero-power associations")


if __name__ == '__main__':
    seed_database()
