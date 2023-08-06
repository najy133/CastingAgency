import datetime
import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Actor, Movie, db_drop_and_create_all
from auth import AuthError, requires_auth


RESPONSES_PER_PAGE = 10 #This will be used in Pagination


def paginate_request(request, selection): #This will paginate to return 10 questions per page
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * RESPONSES_PER_PAGE
    end = start + RESPONSES_PER_PAGE

    responses = [responses.format() for responses in selection]
    current_questions = responses[start:end]

    return current_questions




def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.app_context().push()
    setup_db(app)
    CORS(app)

    '''
    uncomment the following line to initialize the datbase
    !! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
    !! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
    !! Running this funciton will add one
    '''
    # db_drop_and_create_all()

    # Decorator to set Access-Control-Allow
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response
    
    # Register routes
    @app.route('/')
    def home():
        return jsonify({'success': True,
                        'Message': 'Welcome to the Casting Agency project!'
                        }),200
    

    """
    GET REQUESTS
    """

    @app.route("/actors", methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(payload):
        selection = Actor.query.order_by(Actor.id).all()
        current_actors = paginate_request(request, selection)
        actors = Actor.query.all()
        if len(current_actors) == 0:
            abort(404)
        
        return jsonify({
                "success": True,
                "numberOfActors": len(selection),
                "actors": [actor.format() for actor in actors]
            }), 200
    

    @app.route("/movies", methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(payload):

        selection = Movie.query.order_by(Movie.id).all()
        current_movies = paginate_request(request, selection)
        movies = Movie.query.all()
        if len(current_movies) == 0:
            abort(404)
        
        return jsonify({
                "success": True,
                "numberOfMovies": len(selection),
                "Movies": [movie.format() for movie in movies]
            }), 200
    




    """
    POST REQUESTS
    """

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def create_actor(payload):
            
            # Get the data from the request body
            body = request.get_json()

            # Extract the actor attributes from the data
            name = body.get('name', None)
            age = body.get('age', None)
            gender = body.get('gender', None)
            # Ensure all required data is provided 
            if not name or not age or not gender:
                abort(400)
            
            try:
                # Create a new actor object
                new_actor = Actor(name=name, age=age, gender=gender)

                # Insert the new actor into the database
                new_actor.insert()

                return jsonify({
                    'success': True,
                    'actor': new_actor.format()
                }), 201

            except Exception as e:
                print(e)
                abort(500)


    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def create_movie(payload):
        
            # Get the data from the request body
            body = request.get_json()

            # Extract the movie attributes from the data
            title = body.get('title', None)
            release_date = body.get('release_date', None)

            # Ensure all required data is provided
            if not title or not release_date:
                abort(400)

            try:
                # Create a new movie object
                new_movie = Movie(title=title, release_date=release_date)

            # Insert the new movie into the database
                new_movie.insert()

                return jsonify({
                    'success': True,
                    'movie': new_movie.format()
                }), 201

            except Exception as e:
                print(e)
                abort(500)



    """
    PATCH REQUESTS
    """

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_movie(payload, movie_id):
        # Get the movie to be updated
        movie = Movie.query.get(movie_id)

        # Check if the movie exists
        if not movie:
            abort(404)

        # Get the data from the request body
        body = request.get_json()

        try:
            # Update the movie fields if they are provided in the request
            if 'title' in body:
                movie.title = body['title']
            if 'release_date' in body:
                movie.release_date = datetime.datetime.strptime(body['release_date'], '%Y-%m-%d').date()

            # Commit the changes to the database
            movie.update()

            return jsonify({
                'success': True,
                'movie': movie.format()
            }), 200

        except Exception as e:
            print(e)
            abort(500)


    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def update_actor(payload, actor_id):

        # Check if the actor exists
        actor = Actor.query.get(actor_id)
        if not actor:
            abort(404)

        # Get the data from the request body
        body = request.get_json()    

        try:
            
            # Update the actor attributes individually if they exist in the request body
            if 'name' in body:
                actor.name = body['name']
            if 'age' in body:
                actor.age = body['age']
            if 'gender' in body:
                actor.gender = body['gender']

            # Update the actor in the database
            actor.update()

            # Link actors to movies if movie_ids are provided in the request body
            if 'movie_ids' in body:
                movie_ids = body['movie_ids']
                movies = Movie.query.filter(Movie.id.in_(movie_ids)).all()
                actor.movies = movies

            # Commit the changes to the database
            actor.update()

            return jsonify({
                'success': True,
                'actor': actor.format()
            }), 200

        except Exception as e:
            print(e)
            abort(500)




    """
    DELETE REQUESTS
    """

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(payload, actor_id):
    
        # Check if the actor with the given ID exists in the database
        actor = Actor.query.get(actor_id)
        if not actor:
            abort(404)  

        try:
            # Delete the actor from the database
            actor.delete()

            return jsonify({
                'success': True,
                'deleted_actor_id': actor_id
            }), 200

        except Exception as e:
            print(e)
            abort(500)


    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(payload, movie_id):
        
        # Check if the movie with the given ID exists in the database
        movie = Movie.query.get(movie_id)
        if not movie:
            abort(404)

        try:
        
            # Delete the movie from the database
            movie.delete()

            return jsonify({
                'success': True,
                'deleted_movie_id': movie_id
            }), 200

        except Exception as e:
            print(e)
            abort(500)


    '''
    Error Handling
    '''

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422


    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'Bad Request'
        }), 400


    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            'success': False,
            'error': 401,
            'message': 'Unauthorized'
        }), 401


    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            'success': False,
            'error': 403,
            'message': 'Permission not allowed'
        }), 403


    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Not Found'
        }), 404


    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': 'Method Not Allowed'
        }), 405



    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)





