from datetime import datetime
import os
from sqlalchemy import Column, ForeignKey, String, Integer, Date
from flask_sqlalchemy import SQLAlchemy

DATABASE_PATH = os.environ['DATABASE_URL']

db = SQLAlchemy()

'''
setup_db(app) binds a flask application and a SQLAlchemy service
'''

def setup_db(app, database_path=DATABASE_PATH):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
'''

def db_drop_and_create_all():
    db.drop_all()
    db.create_all()

    # Add a dummy actor and movie
    actor = Actor(
        name='John Doe',
        age=27,
        gender='Male'
    )
    movie = Movie(
        title='Return of the Jedi',
        release_date=datetime(2023, 7, 1).date()
    )
    actor.insert()
    movie.insert()

    # Associate actors with movies
    associate_actors_with_movies()

'''
associate_actors_with_movies()
    This function associates actors with movies in the many-to-many relationship
'''

def associate_actors_with_movies():
    # Get the actor with name 'John Doe' and movie with title 'Return of the Jedi'
    actor = Actor.query.filter_by(name='John Doe').first()
    movie = Movie.query.filter_by(title='Return of the Jedi').first()

    # If both actor and movie exist, associate them
    if actor and movie:
        movie.actors.append(actor)
        db.session.commit()

# Association table for the many-to-many relationship
actors_movies = db.Table('actors_movies',
                         Column('actor_id', Integer, ForeignKey('actors.id'), primary_key=True),
                         Column('movie_id', Integer, ForeignKey('movies.id'), primary_key=True)
                         )

'''
Actors Model
'''

class Actor(db.Model):
    __tablename__ = 'actors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)

    # Relationship with movies (many-to-many)
    movies = db.relationship('Movie', secondary=actors_movies, back_populates='actors')

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'movies': [movie.format() for movie in self.movies]
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

'''
Movie Model
'''

class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    release_date = db.Column(db.Date, nullable=False)

    # Relationship with actors (many-to-many)
    actors = db.relationship('Actor', secondary=actors_movies, back_populates='movies')

    def format(self):
         # Get a list of actor names associated with this movie
        actor_names = [actor.name for actor in self.actors]
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date.strftime('%Y-%m-%d'),
            'actors': [actor.name for actor in self.actors]
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
