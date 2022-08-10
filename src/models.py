from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    last_name = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    nick_name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(700), unique=True, nullable=False)
    fecha_de_suscripcion = db.Column(db.DateTime)
    activo = db.Column(db.Boolean())
   
    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "nick_name":self.nick_name,
        }

class Characters(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    hair_color = db.Column(db.String(250), nullable=False)
    eyes_color = db.Column(db.String(250), nullable=False)
    mass = db.Column(db.Integer)
    height = db.Column(db.Integer)
    birth_year = db.Column(db.String(250))
    gender = db.Column(db.String(250))
    home_world = db.Column(db.String(250))

    def __repr__(self):
        return '<Characters %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "hair_color":self.hair_color,
            "eyes_color":self.eyes_color,
            "mass":self.mass,
            "height":self.height,
            "birth_year":self.birth_year,
            "gender":self.gender,
            "home_world":self.home_world
        }

class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    diameter = db.Column(db.Integer)
    population = db.Column(db.Integer)
    climate = db.Column(db.String(250), nullable=False)
    rotation_period = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    terrain = db.Column(db.String(250), nullable=False)
    
    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter":self.diameter,
            "population":self.population,
            "climate":self.climate,
            "rotation_period":self.rotation_period,
            "orbital_period":self.orbital_period,
            "terrain":self.terrain
        }
class Vehicles(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    model = db.Column(db.String(250), nullable=False)
    manufacturer = db.Column(db.String(250))
    vehicle_class = db.Column(db.String(250))
    max_atmosphering_speed = db.Column(db.Integer)
    cargo_capacity = db.Column(db.Integer)
    def __repr__(self):
        return '<Vehicles %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model":self.model,
            "manufacturer":self.manufacturer,
            "vehicle_class":self.vehicle_class,
            "max_atmosphering_speed":self.max_atmosphering_speed,
            "cargo_capacity":self.cargo_capacity
        }

class User_planets(db.Model):
    __tablename__ = 'user_planets'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user=db.relationship('User')
    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    planets=db.relationship('Planets')

    def __repr__(self):
        return '<User_planets %r>' % self.user_id

    def serialize(self):
        return {
            "planets":self.planets.serialize()
         }
    def serialize_fav(self):
        return self.planets.serialize()

class User_vehicles(db.Model):
    __tablename__ = 'user_vehicles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user=db.relationship('User')
    vehicles_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
    vehicles=db.relationship('Vehicles')

    def __repr__(self):
        return '<User_vehicles %r>' % self.user_id

    def serialize(self):
        return {
            "vehicles":self.vehicles.serialize()
        }
    def serialize_fav(self):
        return self.vehicles.serialize()
          

class User_characters(db.Model):
    __tablename__ = 'user_characters'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user=db.relationship('User')
    characters_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    characters=db.relationship('Characters')

    def __repr__(self):
        return '<User_characters %r>' % self.user_id

    def serialize(self):
        return {
            "characters":self.characters.serialize()
        }
    def serialize_fav(self):
        return self.characters.serialize()  