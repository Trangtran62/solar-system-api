from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, order_from_sun):
        self.id = id
        self.name = name
        self.description = description
        self.order_from_sun = order_from_sun

planet1 = Planet(1, "Earth", "weird", 3)
planet2 = Planet(2, "Mars", "hot", 4)
planet3 = Planet(3, "Venus", "orange", 5)

planets = [planet1, planet2, planet3]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def get_planets():
    response = []
    for planet in planets:
        planet_dict = {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description, 
        "order_from_sun": planet.order_from_sun }

        response.append(planet_dict)

    return jsonify(response), 200
