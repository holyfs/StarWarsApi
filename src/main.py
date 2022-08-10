"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Characters, Planets, Vehicles, User_characters, User_planets, User_vehicles 
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

#User
#Method GET
@app.route('/users', methods=['GET'])
def get_user():
    user = User.query.all()
    all_users = list(map(lambda user: user.serialize(), user))
    return jsonify(all_users),200
#Method POST
@app.route('/user', methods=['POST'])
def add_user():
    body=request.get_json()
    user = User(
        nick_name = body["nick_name"],
        name=body["name"],
        last_name=body["last_name"],
        password=body["password"],
        email=body["email"]
        )
    db.session.add(user)
    db.session.commit()
    return jsonify(user.serialize()),201 
#Methods by ID (GET, PUT, DELETE)
@app.route('/user/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def single_user(user_id):
    if request.method == 'GET':
        user = User.query.get(user_id)
        if user is None:
           raise APIException("user not found", 404)
        return jsonify(user.serialize()),200
    elif request.method == 'PUT':
        body = request.get_json()
        user = User.query.get(user_id)
        if user is None:
           raise APIException("user not found", 404)
        db.session.commit()        
        return jsonify(user.serialize()),200
    elif request.method == 'DELETE':
        user = User.query.get(user_id)
        if user is None:
           raise APIException("user not found", 404)
        db.session.delete(user)
        db.session.commit()
        return jsonify(user.serialize()),200


#Characters
#Method POST
@app.route('/characters', methods=['POST'])
def add_pleople():
        body = request.get_json()
        people = Characters(
            name=body["name"],
            hair_color=body["hair_color"],
            eyes_color=body["eyes_color"],
            mass=body["mass"],
            height=body["height"],
            birth_year=body["birth_year"],
            gender=body["gender"],
            home_world=body["home_world"])
        db.session.add(people)
        db.session.commit()
        return jsonify(people.serialize()),201   
#Method GET
@app.route('/characters', methods=['GET'])
def get_pleople():
    people = Characters.query.all()
    all_people = list(map(lambda people: people.serialize(), people))
    return jsonify(all_people),200
#Methods by ID (GET, PUT, DELETE)
@app.route('/characters/<int:characters_id>', methods=['GET', 'PUT', 'DELETE'])
def single_character(characters_id):
    if request.method == 'GET':
        people = Characters.query.get(characters_id)
        if people is None:
           raise APIException("character not found", 404)
        return jsonify(people.serialize()),200
    elif request.method == 'PUT':
        body = request.get_json()
        people = Characters.query.get(characters_id)
        if people is None:
           raise APIException("character not found", 404)
        people.name = body["name"]
        people.hair_color = body["hair_color"]
        people.eyes_color= body["eyes_color"]
        people.mass=body["mass"]
        people.height=body["height"]
        people.birth_year=body["birth_year"]
        people.gender=body["gender"]
        people.home_world=body["home_world"]
        db.session.commit()        
        return jsonify(people.serialize()),200
    elif request.method == 'DELETE':
        people = Characters.query.get(characters_id)
        if people is None:
           raise APIException("character not found", 404)
        db.session.delete(people)
        db.session.commit()
        return jsonify(people.serialize()),200

#Planets
#Method POST
@app.route('/planets', methods=['POST'])
def add_planet():
        body = request.get_json()
        planet = Planets(
            name=body["name"],
            diameter=body["diameter"],
            population=body["population"],
            climate=body["climate"],
            rotation_period=body["rotation_period"],
            orbital_period=body["orbital_period"],
            terrain=body["terrain"]
            )
        db.session.add(planet)
        db.session.commit()
        return jsonify(planet.serialize()),201 
#Method GET
@app.route('/planets', methods=['GET'])
def get_planets():
    planet = Planets.query.all()
    all_planets = list(map(lambda planet: planet.serialize(), planet))
    return jsonify(all_planets),200
#Methods by ID (GET, PUT, DELETE)
@app.route('/planets/<int:planets_id>', methods=['GET', 'PUT', 'DELETE'])
def single_planets(planets_id):
    if request.method == 'GET':
        planet = Planets.query.get(planets_id)
        if planet is None:
           raise APIException("planet not found", 404)
        return jsonify(planet.serialize()),200
    elif request.method == 'PUT':
        body = request.get_json()
        planet = Planets.query.get(planets_id)
        if planet is None:
           raise APIException("planet not found", 404)
        planet.climate = body["climate"]
        planet.diameter = body["diameter"]
        planet.name = body["name"]
        planet.orbital_period=body["orbital_period"]
        planet.population=body["population"]
        planet.rotation_period=body["rotation_period"]
        planet.terrain=body["terrain"]
        db.session.commit()        
        return jsonify(planet.serialize()),200
    elif request.method == 'DELETE':
        planet = Planets.query.get(planets_id)
        if planet is None:
           raise APIException("planet not found", 404)
        db.session.delete(planet)
        db.session.commit()
        return jsonify(planet.serialize()),200

#vehicles
#Method POST
@app.route('/vehicles', methods=['POST'])
def add_vehicle():
        body = request.get_json()
        vehicle = Vehicles(
            name=body["name"],
            model=body["model"],
            manufacturer=body["manufacturer"],
            vehicle_class=body["vehicle_class"],
            max_atmosphering_speed=body["max_atmosphering_speed"],
            cargo_capacity=body["cargo_capacity"],
            )
        db.session.add(vehicle)
        db.session.commit()
        return jsonify(vehicle.serialize()),201 
#Method GET
@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    vehicle = Vehicles.query.all()
    all_vehicles = list(map(lambda vehicle: vehicle.serialize(), vehicle))
    return jsonify(all_vehicles),200
#Method by ID (GET, PUT, DELETE)
@app.route('/vehicles/<int:vehicles_id>', methods=['GET', 'PUT', 'DELETE'])
def single_vehicle(vehicles_id):
    if request.method == 'GET':
        vehicle = Vehicles.query.get(vehicles_id)
        if vehicle is None:
           raise APIException("vehicle not found", 404)
        return jsonify(planet.serialize()),200
    elif request.method == 'PUT':
        body = request.get_json()
        vehicle = Vehicles.query.get(vehicles_id)
        if vehicle is None:
           raise APIException("vehicle not found", 404)
        db.session.commit()        
        return jsonify(vehicle.serialize()),200
    elif request.method == 'DELETE':
        vehicle = Vehicles.query.get(vehicles_id)
        if vehicle is None:
           raise APIException("vehicle not found", 404)
        db.session.delete(vehicle)
        db.session.commit()
        return jsonify(vehicle.serialize()),200 

#Favorites
#user_Favorites
#method GET
@app.route('/user/favorites', methods=['GET'])
def get_user_favorites():
    planets=[]
    vehicles=[]
    characters=[]
    body = request.get_json()
    user = body["user_id"]
    user = User.query.filter(User.id==user).first()
    if not user:
       raise APIException("not user found", 400) 
    favorite_planet = User_planets.query.filter(User_planets.user_id==user.id).all()
    if favorite_planet:
        planets=list(map(lambda planet: planet.serialize_fav(), favorite_planet))
    favorite_vehicle = User_vehicles.query.filter(User_vehicles.user_id==user.id).all()
    if favorite_vehicle:
        vechiles=list(map(lambda vehicle: vehicle.serialize_fav(), favorite_vehicle))
    favorite_character = User_characters.query.filter(User_characters.user_id==user.id).all()
    if favorite_character:
        characters=list(map(lambda character: character.serialize_fav(), favorite_character))
    final_list = {
        "planets": planets,
        "vehicles": vehicles,
        "characters": characters
    }
    return jsonify(final_list),200


#user_Favorites_planets_____________________________________________________________________________________________
@app.route('/user/favorite/planet/<int:planets_id>', methods=['POST', 'DELETE'])
def add_user_favorite_planet(planets_id):
    if request.method=='POST':
        body = request.get_json()
        user = body["user_id"]
        user = User.query.filter(User.id==user).first()
        planet = Planets.query.get(planets_id)
        exist_planet= Planets.query.filter(Planets.id==planets_id).first()
        if not exist_planet:
            raise APIException("planet not found", 404)
        favorite_planet = User_planets(
            user_id=user.id,
            planets_id=planet.id
            )
        exist_planet_in_user=User_planets.query.filter(User_planets.planets_id==planets_id).first()
        if exist_planet_in_user:
            raise APIException("the planet already exist in this user", 404)
        else:
            db.session.add(favorite_planet)
            db.session.commit()
            res = {"msg":"Favorite planet added"}   
    if request.method=='DELETE':
        body = request.get_json()
        user = body["user_id"]
        user = User.query.filter(User.id==user).first()
        planet = Planets.query.get(planets_id)
        exist_planet= Planets.query.filter(Planets.id==planets_id).first()
        if not exist_planet:
            raise APIException("planet not found", 404)
        favorite_planet = User_planets.query.filter(User_planets.planets_id==planets_id).first()
        exist_favorite_planet_user= User_planets.query.filter(User_planets.planets_id==planets_id).first()
        if not exist_favorite_planet_user:
            raise APIException("Bad request",500)
        db.session.delete(favorite_planet)
        db.session.commit()
        res = {"msg":"Favorite planet deleted"}
    return jsonify(res),200
#user_Favorites_vehicles_____________________________________________________________________________________________
@app.route('/user/favorite/vehicle/<int:vehicles_id>', methods=['POST', 'DELETE'])
def add_user_favorite_vehicle(vehicles_id):
    if request.method=='POST':
        body = request.get_json()
        user = body["user_id"]
        user = User.query.filter(User.id==user).first()
        vehicle = Vehicles.query.get(vehicles_id)
        exist_vehicle= Vehicles.query.filter(Vehicles.id==vehicles_id).first()
        if not exist_vehicle:
            raise APIException("vehicle not found", 404)
        favorite_vehicle = User_vehicles(
            user_id=user.id,
            vehicles_id=vehicle.id
            )
        exist_vehicle_in_user=User_vehicles.query.filter(User_vehicles.vehicles_id==vehicles_id).first()
        if exist_vehicle_in_user:
            raise APIException("the vehicle already exist in this user", 404)
        else:
            db.session.add(favorite_vehicle)
            db.session.commit()
        res = {"msg":"Favorite vehicle added"}
    if request.method=='DELETE':
        body = request.get_json()
        user = body["user_id"]
        user = User.query.filter(User.id==user).first()
        vehicle = Vehicles.query.get(vehicles_id)
        exist_vehicle= Vehicles.query.filter(Vehicles.id==vehicles_id).first()
        if not exist_vehicle:
            raise APIException("vehicle not found", 404)
        favorite_vehicle = User_vehicles.query.filter(User_vehicles.vehicles_id==vehicles_id).first()
        exist_favorite_vehicle_user= User_vehicles.query.filter(User_vehicles.vehicles_id==vehicles_id).first()
        if not exist_favorite_vehicle_user:
            raise APIException("Bad request",500)
        db.session.delete(favorite_vehicle)
        db.session.commit()
        res = {"msg":"Favorite vehicle deleted"}
    return jsonify(res),200
#user_Favorites_characters_____________________________________________________________________________________________
@app.route('/user/favorite/character/<int:characters_id>', methods=['POST', 'DELETE'])
def add_user_favorite_character(characters_id):
    if request.method=='POST':
        body = request.get_json()
        user = body["user_id"]
        user = User.query.filter(User.id==user).first()
        character = Characters.query.get(characters_id)
        exist_character= Characters.query.filter(Characters.id==characters_id).first()
        if not exist_character:
            raise APIException("character not found", 404)
        favorite_character = User_characters(
            user_id=user.id,
            characters_id=character.id
            )
        exist_character_in_user=User_characters.query.filter(User_characters.characters_id==characters_id).first()
        if exist_character_in_user:
            raise APIException("the character already exist in this user", 404)
        else:
            db.session.add(favorite_character)
            db.session.commit()
        res = {"msg":"Favorite character added"}
    if request.method=='DELETE':
        body = request.get_json()
        user = body["user_id"]
        user = User.query.filter(User.id==user).first()
        character = Characters.query.get(characters_id)
        exist_character= Characters.query.filter(Characters.id==characters_id).first()
        if not exist_character:
            raise APIException("character not found", 404)
        favorite_character = User_characters.query.filter(User_characters.characters_id==characters_id).first()
        exist_favorite_character_user= User_characters.query.filter(User_characters.characters_id==characters_id).first()
        if not exist_favorite_character_user:
            raise APIException("Bad request",500)
        db.session.delete(favorite_character)
        db.session.commit()
        res = {"msg":"Favorite character deleted"}
    return jsonify(res),200


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
