
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

