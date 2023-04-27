
from app.models.planet import Planet 
from app import db
from flask import Blueprint, jsonify, make_response, request 

planet_bp = Blueprint("planet", __name__, url_prefix="/planet")
@planet_bp.route("", methods=["POST"])
def add_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name = request_body["name"],
        description = request_body["description"],
        order_from_sun = request_body["order_from_sun"]
    )
    db.session.add(new_planet)
    db.session.commit()
    
    return make_response(f"Planet {new_planet} successfuly created", 201)

@planet_bp.route("", methods=["GET"]) 
def get_plants():
    response = []
    planets = Planet.query.all()
    for planet in planets:
        response.append(planet.to_dict())
    return jsonify(response) 
       
# class Planet:
#     def __init__(self, id, name, description, order_from_sun):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.order_from_sun = order_from_sun

# planet1 = Planet(1, "Earth", "weird", 3)
# planet2 = Planet(2, "Mars", "hot", 4)
# planet3 = Planet(3, "Venus", "orange", 5)

# planets = [planet1, planet2, planet3]

# planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

# @planets_bp.route("", methods=["GET"])
# def get_planets():
#     response = []
#     for planet in planets:
#         planet_dict = {
#         "id": planet.id,
#         "name": planet.name,
#         "description": planet.description, 
#         "order_from_sun": planet.order_from_sun }
#         response.append(planet_dict)
#     return jsonify(response), 200

# @planets_bp.route("/<id>", methods=["GET"])
# def get_one_planets(id):
#     try:
#         planet_id = int(id)
#     except ValueError:
#         return jsonify({"msg": f"Invalid id: {id}"}), 400
    
#     for planet in planets:
#         if planet.id == planet_id:
#             return jsonify({
#                 "id": planet.id,
#                 "name": planet.name,
#                 "description": planet.description,
#                 "order from the sun": planet.order_from_sun
#             }), 200
#     return {"msg": f"Error 404: planet with id {planet_id} not found."}, 404
