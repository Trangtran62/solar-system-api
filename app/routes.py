
from app.models.planet import Planet 
from app import db
from flask import Blueprint, jsonify, make_response, request, abort 

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
def get_planets():
    response = []
    name_query = request.args.get("name")
    
    if name_query:
        planets = Planet.query.filter_by(name=name_query.capitalize())
    else:
        planets = Planet.query.all()
        
    for planet in planets:
        response.append(planet.to_dict())
    return jsonify(response), 200 

def validate_id(planet_id):
    try:
        planet_id =int(planet_id)
    except:
        abort(make_response({"message": f"planet {planet_id} invalid"}, 400))
    planet = Planet.query.get_or_404(planet_id)
    
    return planet

@planet_bp.route("/<planet_id>", methods=["GET"]) 
def get_one_planet(planet_id):
    planet = validate_id(planet_id)
    return planet.to_dict()

@planet_bp.route("/<planet_id>", methods=["PUT"]) 
def update_one_planet(planet_id):
    planet = validate_id(planet_id)
    request_body = request.get_json()
    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.order_from_sun = request_body["order_from_sun"]
    
    db.session.commit()
    return {"message": f"planet {planet_id} updated"}

@planet_bp.route("/<planet_id>", methods=["DELETE"])
def delete_one_planet(planet_id):
    planet = validate_id(planet_id)
    db.session.delete(planet)
    db.session.commit()
    return {"message": f"planet {planet_id} deleted"}


