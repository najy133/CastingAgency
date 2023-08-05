import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actor, Movie


class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the casting agency test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = os.getenv('TEST_DATABASE_URL')
        
        # Set up the test database
        setup_db(self.app, self.database_path)


        # Sample actor and movie data for testing
        self.new_actor = {
            'name': 'John Doe',
            'age': 30,
            'gender': 'Male'
        }

        self.new_movie = {
            'title': 'The Great Movie',
            'release_date': '2023-01-01'
        }

        # Add a test actor to the database
        test_actor = Actor(name=self.new_actor['name'], age=self.new_actor['age'], gender=self.new_actor['gender'])
        test_actor.insert()

        # Add a test movie to the database
        test_movie = Movie(title=self.new_movie['title'], release_date=self.new_movie['release_date'])
        test_movie.insert()

        # Define your testing tokens here
        self.casting_assistant_token = os.getenv('TEST_CASTING_ASSISTANT_TOKEN')
        self.casting_director_token = os.getenv('TEST_CASTING_DIRECTOR_TOKEN')

    def tearDown(self):
        """Executed after each test."""
        pass

    """
    Actors
    """

    def test_get_actors(self):
        res = self.client().get('/actors', headers={'Authorization': f'Bearer {self.casting_assistant_token}'})
        data = json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_unauthorized_get_actors(self):
        # Use an invalid or expired token (e.g., 'INVALID_TOKEN') for the test
        res = self.client().get('/actors', headers={'Authorization': 'Bearer INVALID_TOKEN'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401) 
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unauthorized')


    def test_create_actor(self):
        # Define a new actor data
        new_actor_data = {
            'name': 'Jane Doe',
            'age': 25,
            'gender': 'Female'
        }

        # Send a POST request to create a new actor
        res = self.client().post('/actors', json=new_actor_data, headers={'Authorization': f'Bearer {self.casting_director_token}'})
        data = json.loads(res.data)

        # Assert the response
        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actor']))


    def test_create_actor_403_permission_not_allowed(self):
        # Define new actor data
        new_actor_data = {
            'name': 'Unauthorized Actor',
            'age': 30,
            'gender': 'Male'
        }

        # Send a POST request to create a new actor with the assistant token
        res = self.client().post('/actors', json=new_actor_data, headers={'Authorization': f'Bearer {self.casting_assistant_token}'})
        data = json.loads(res.data)
        # Assert the response
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permission not allowed')

    def test_create_actor_400_missing_data(self):
        # Invalid 'name' field in the actor data
        new_actor_data = {
            'age': 25,
            'gender': 'Female'
        }

        # Send a POST request to create a new actor using the director token
        res = self.client().post('/actors', json=new_actor_data, headers={'Authorization': f'Bearer {self.casting_director_token}'})
        data = json.loads(res.data)
        # Assert the response
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)

    def test_update_actor(self):
        # Create a new actor to be updated
        new_actor_data = {
            'name': 'John Doe',
            'age': 30,
            'gender': 'Male'
        }
        res = self.client().post('/actors', json=new_actor_data, headers={'Authorization': f'Bearer {self.casting_director_token}'})
        data = json.loads(res.data)
        actor_id = data['actor']['id']

        # Update the actor's information
        updated_actor_data = {
            'name': 'Updated Name',
            'age': 35,
            'gender': 'Female'
        }
        res = self.client().patch(f'/actors/{actor_id}', json=updated_actor_data, headers={'Authorization': f'Bearer {self.casting_director_token}'})
        data = json.loads(res.data)

        # Assert the response
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    def test_update_404_nonexistent_actor(self):
        # Define data for updating a non-existent actor
        updated_actor_data = {
            'name': 'Updated Name',
            'age': 35,
            'gender': 'Female'
        }
        
        # Use an actor ID that doesn't exist in the database
        non_existent_actor_id = 999
        
        # Send a PATCH request to update the non-existent actor
        res = self.client().patch(f'/actors/{non_existent_actor_id}', json=updated_actor_data, headers={'Authorization': f'Bearer {self.casting_director_token}'})
        data = json.loads(res.data)
        
        # Assert the response
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
     
    def test_update_actor_invalid_permissions(self):
        # Create a new actor to be updated
        new_actor_data = {
            'name': 'John Doe',
            'age': 30,
            'gender': 'Male'
        }
        res = self.client().post('/actors', json=new_actor_data, headers={'Authorization': f'Bearer {self.casting_director_token}'})
        data = json.loads(res.data)
        print(data)
        actor_id = data['actor']['id']  # Get the ID from the actor object in the response

        # Try to update the actor's information using the casting assistant token (should be forbidden)
        updated_actor_data = {
            'name': 'Updated Name',
            'age': 35,
            'gender': 'Female'
        }
        res = self.client().patch(f'/actors/{actor_id}', json=updated_actor_data, headers={'Authorization': f'Bearer {self.casting_assistant_token}'})
        data = json.loads(res.data)

        # Assert the response
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permission not allowed')


    def test_delete_actor(self):
        # Create a new actor to be deleted
        new_actor_data = {
            'name': 'John Doe',
            'age': 30,
            'gender': 'Male'
        }
        res = self.client().post('/actors', json=new_actor_data, headers={'Authorization': f'Bearer {self.casting_director_token}'})
        data = json.loads(res.data)
        actor_id = data['actor']['id']

        # Delete the actor using the executive producer token
        res = self.client().delete(f'/actors/{actor_id}', headers={'Authorization': f'Bearer {self.casting_director_token}'})
        data = json.loads(res.data)

        # Assert the response
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted_actor_id'], actor_id)

    def test_delete_actor_404_not_found(self):
        # Try to delete an actor that doesn't exist
        res = self.client().delete('/actors/999999', headers={'Authorization': f'Bearer {self.casting_director_token}'})
        data = json.loads(res.data)

        # Assert the response
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)


    def test_delete_actor_403_invalid_permissions(self):
        # Create a new actor to be deleted
        new_actor_data = {
            'name': 'John Doe',
            'age': 30,
            'gender': 'Male'
        }
        res = self.client().post('/actors', json=new_actor_data, headers={'Authorization': f'Bearer {self.casting_director_token}'})
        data = json.loads(res.data)
        actor_id = data['actor']['id']

        # Try to delete the actor using the assistant token (should be forbidden)
        res = self.client().delete(f'/actors/{actor_id}', headers={'Authorization': f'Bearer {self.casting_assistant_token}'})
        data = json.loads(res.data)

        # Assert the response
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permission not allowed')


    """
    Movies
    """

    def test_get_movies(self):
        # Send a GET request to retrieve movies using the assistant token
        res = self.client().get('/movies', headers={'Authorization': f'Bearer {self.casting_assistant_token}'})
        data = json.loads(res.data)

        # Assert the response
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['Movies'])


    def test_get_movies_401_invalid_permissions(self):
        # Send a GET request to retrieve movies using the casting assistant token Use an invalid or expired token (e.g., 'INVALID_TOKEN') for the test
        res = self.client().get('/movies', headers={'Authorization': 'Bearer INVALID_TOKEN'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401) 
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unauthorized')


    def test_create_movie(self):
        # Define a new movie data
        new_movie_data = {
            'title': 'The Movie',
            'release_date': '2023-07-19'
        }

        # Send a POST request to create a new movie
        res = self.client().post('/movies', json=new_movie_data, headers={'Authorization': f'Bearer {self.casting_director_token}'})
        data = json.loads(res.data)

        # Assert the response
        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])


    def test_create_movie_403_permission_not_allowed(self):
        # Define new movie data
        new_movie_data = {
            'title': 'Unauthorized Movie',
            'release_date': '2023-07-19'
        }

        # Send a POST request to create a new movie with the casting director token
        res = self.client().post('/movies', json=new_movie_data, headers={'Authorization': f'Bearer {self.casting_assistant_token}'})
        data = json.loads(res.data)
        # Assert the response
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permission not allowed')

    

    def test_create_movie_400_missing_data(self):
        # Invalid 'title' field in the movie data
        new_movie_data = {
            'release_date': '2023-07-19'
        }

        # Send a POST request to create a new movie using the director token
        res = self.client().post('/movies', json=new_movie_data, headers={'Authorization': f'Bearer {self.casting_director_token}'})
        data = json.loads(res.data)
        # Assert the response
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)



    def test_update_movie(self):
        # Create a new movie to be updated
        new_movie_data = {
            'title': 'Test Movie',
            'release_date': '2023-07-19'
        }
        res = self.client().post('/movies', json=new_movie_data, headers={'Authorization': f'Bearer {self.casting_director_token}'})
        data = json.loads(res.data)
        movie_id = data['movie']['id']

        # Update the movie's information
        updated_movie_data = {
            'title': 'Updated Title',
            'release_date': '2023-08-01'
        }
        res = self.client().patch(f'/movies/{movie_id}', json=updated_movie_data, headers={'Authorization': f'Bearer {self.casting_director_token}'})
        data = json.loads(res.data)

        # Assert the response
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_update_movie_invalid_permissions(self):
        # Create a new movie to be updated
        new_movie_data = {
            'title': 'Test Movie',
            'release_date': '2023-07-19'
        }
        res = self.client().post('/movies', json=new_movie_data, headers={'Authorization': f'Bearer {self.casting_director_token}'})
        data = json.loads(res.data)
        movie_id = data['movie']['id']

        # Attempt to update the movie with the assistant token
        updated_movie_data = {
            'title': 'Updated Title',
            'release_date': '2023-08-01'
        }
        res = self.client().patch(f'/movies/{movie_id}', json=updated_movie_data, headers={'Authorization': f'Bearer {self.casting_assistant_token}'})
        data = json.loads(res.data)

        # Assert the response
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permission not allowed')

    def test_update_non_existent_movie(self):
        # Define a new movie data
        new_movie_data = {
            'title': 'The Movie',
            'release_date': '2023-07-19'
        }

        # Send a POST request to create a new movie
        res = self.client().post('/movies', json=new_movie_data, headers={'Authorization': f'Bearer {self.casting_director_token}'})
        data = json.loads(res.data)
        movie_id = data['movie']['id']

        # Delete the movie to make it non-existent
        self.client().delete(f'/movies/{movie_id}', headers={'Authorization': f'Bearer {self.casting_director_token}'})

        # Attempt to update the non-existent movie
        updated_movie_data = {
            'title': 'Updated Movie',
            'release_date': '2023-07-20'
        }
        res = self.client().patch(f'/movies/{movie_id}', json=updated_movie_data, headers={'Authorization': f'Bearer {self.casting_director_token}'})
        data = json.loads(res.data)

        # Assert the response
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_delete_movie(self):
        # Create a new movie to be deleted
        new_movie_data = {
            'title': 'Test Movie',
            'release_date': '2023-07-19'
        }
        res = self.client().post('/movies', json=new_movie_data, headers={'Authorization': f'Bearer {self.casting_director_token}'})
        data = json.loads(res.data)
        movie_id = data['movie']['id']

        # Delete the created movie
        res = self.client().delete(f'/movies/{movie_id}', headers={'Authorization': f'Bearer {self.casting_director_token}'})
        data = json.loads(res.data)

        # Assert the response
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted_movie_id'], movie_id)


    def test_delete_movie_404_not_found(self):
        # Attempt to delete a non-existent movie
        movie_id = 999  # Assuming this ID does not exist in the database
        res = self.client().delete(f'/movies/{movie_id}', headers={'Authorization': f'Bearer {self.casting_director_token}'})
        data = json.loads(res.data)

        # Assert the response
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        
    def test_delete_movie_403_invalid_permissions(self):
    # Create a new movie to be deleted
        new_movie_data = {
            'title': 'Test Movie',
            'release_date': '2023-07-19'
        }
        res = self.client().post('/movies', json=new_movie_data, headers={'Authorization': f'Bearer {self.casting_director_token}'})
        data = json.loads(res.data)
        movie_id = data['movie']['id']

        # Attempt to delete the movie with the assistant token
        res = self.client().delete(f'/movies/{movie_id}', headers={'Authorization': f'Bearer {self.casting_assistant_token}'})
        data = json.loads(res.data)

        # Assert the response
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permission not allowed')
    



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
