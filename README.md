<<<<<<< HEAD
# CastingAgency
The Flask Casting Agency API is a RESTful web service that manages actors and movies for a casting agency. It provides various endpoints to perform CRUD operations on actors and movies, as well as role-based authentication and authorization using Auth0.

There are 2 roles that have been created using Auth0, the bearer tokens for each role has been provided in the setup.bat file:

Casting Assistant: Can view the actors and movies only
Casting Director: Can view, create, update, and delete actors and movies


## Table of Contents
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Running the App](#running-the-app)
    - [Running Tests](#running-tests)
    - [Models](#models)
    - [Endpoints](#endpoints)

## Getting Started

### Prerequisites
- Python 3.7 or later
- PostgreSQL database
- Auth0 account for JWT-based authentication


### Installation
1. Clone this repository to your local machine: 
```
git clonehttps://github.com/najy133/CastingAgency.git
```

2. Change into project directory
```
cd your-repo-name
```

3. Create a virtual environment (recommended):
```
python -m venv venv
```

4. Activate the virtual environment: 
    - On Windows:
    ```
        venv\Scripts\activate
    ```

    - On macOS and Linux:
    ``` 
        source venv/bin/activate
    ```

5. Install the required Python packages:
```
pip install -r requirements.txt
```

### Running the App

1. Set up environment variables:
    - Copy the `setup.bat.example` file to `setup.bat` (Windows) or `setup.sh` (macOS/Linux).
    - Open the copied file and fill in your Auth0 configuration and database URLs.

    ```bash
    # Windows
    setup.bat

    # macOS/Linux
    source setup.sh
    ```

2. Run the Flask app:

    ```bash
    python app.py 
    ```

    The app will be accessible at `http://localhost:5000/`. You can interact with the app using a web browser or API tools like Postman.

### Running Tests

1. With the virtual environment activated, run the following command to execute the test suite:

    ```bash
    python test_app.py
    ```

---


## Models

### Actor

- Represents an actor in the casting agency.
- Attributes:
  - `id` (integer, primary key): Unique identifier for the actor.
  - `name` (string): Name of the actor.
  - `age` (integer): Age of the actor.
  - `gender` (string): Gender of the actor.

### Movie

- Represents a movie managed by the casting agency.
- Attributes:
  - `id` (integer, primary key): Unique identifier for the movie.
  - `title` (string): Title of the movie.
  - `release_date` (date): Release date of the movie.



## Endpoints

### Base URL

The API is hosted live using Heroku at the following base URL:

https://casting-agency-deployment-zrkj.onrender.com


### Error Handling

The API returns errors in JSON format, with the following structure:

```json
{
    "success": false,
    "error": 400,
    "message": "Bad Request"
}
```

## Available Endpoints

### GET /actors

- Retrieves a list of actors.
- Requires the `get:actors` permission.
- Returns a list of actor objects.

### GET /movies

- Retrieves a list of movies.
- Requires the `get:movies` permission.
- Returns a list of movie objects.

### POST /actors

- Creates a new actor.
- Requires the `post:actors` permission.
- Returns the created actor object.

### POST /movies

- Creates a new movie.
- Requires the `post:movies` permission.
- Returns the created movie object.

### PATCH /actors/<int:actor_id>

- Updates an existing actor.
- Requires the `patch:actors` permission.
- Returns the updated actor object.

### PATCH /movies/<int:movie_id>

- Updates an existing movie.
- Requires the `patch:movies` permission.
- Returns the updated movie object.

### DELETE /actors/<int:actor_id>

- Deletes an existing actor.
- Requires the `delete:actors` permission.
- Returns a success message.

### DELETE /movies/<int:movie_id>

- Deletes an existing movie.
- Requires the `delete:movies` permission.
- Returns a success message.












=======
# CastingAgency
The Flask Casting Agency API is a RESTful web service that manages actors and movies for a casting agency. It provides various endpoints to perform CRUD operations on actors and movies, as well as role-based authentication and authorization using Auth0.

There are 2 roles:

Casting Assistant: Can view the actors and movies only
Casting Director: Can view, create, update, and delete actors and movies


## Table of Contents
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Running the App](#running-the-app)
    - [Running Tests](#running-tests)
    - [Models](#models)
    - [Endpoints](#endpoints)

## Getting Started

### Prerequisites
- Python 3.7 or later
- PostgreSQL database
- Auth0 account for JWT-based authentication


### Installation
1. Clone this repository to your local machine: 
```
git clonehttps://github.com/najy133/CastingAgency.git
```

2. Change into project directory
```
cd your-repo-name
```

3. Create a virtual environment (recommended):
```
python -m venv venv
```

4. Activate the virtual environment: 
    - On Windows:
    ```
        venv\Scripts\activate
    ```

    - On macOS and Linux:
    ``` 
        source venv/bin/activate
    ```

5. Install the required Python packages:
```
pip install -r requirements.txt
```

### Running the App

1. Set up environment variables:
    - Copy the `setup.bat.example` file to `setup.bat` (Windows) or `setup.sh` (macOS/Linux).
    - Open the copied file and fill in your Auth0 configuration and database URLs.

    ```bash
    # Windows
    setup.bat

    # macOS/Linux
    source setup.sh
    ```

2. Run the Flask app:

    ```bash
    python app.py 
    ```

    The app will be accessible at `http://localhost:5000/`. You can interact with the app using a web browser or API tools like Postman.

### Running Tests

1. With the virtual environment activated, run the following command to execute the test suite:

    ```bash
    python test_app.py
    ```

---


## Models

### Actor

- Represents an actor in the casting agency.
- Attributes:
  - `id` (integer, primary key): Unique identifier for the actor.
  - `name` (string): Name of the actor.
  - `age` (integer): Age of the actor.
  - `gender` (string): Gender of the actor.

### Movie

- Represents a movie managed by the casting agency.
- Attributes:
  - `id` (integer, primary key): Unique identifier for the movie.
  - `title` (string): Title of the movie.
  - `release_date` (date): Release date of the movie.



## Endpoints

### Base URL

The API is hosted live using Heroku at the following base URL:

https://casting-agency-deployment-zrkj.onrender.com


### Error Handling

The API returns errors in JSON format, with the following structure:

```json
{
    "success": false,
    "error": 400,
    "message": "Bad Request"
}
```

## Available Endpoints

### GET /actors

- Retrieves a list of actors.
- Requires the `get:actors` permission.
- Returns a list of actor objects.

### GET /movies

- Retrieves a list of movies.
- Requires the `get:movies` permission.
- Returns a list of movie objects.

### POST /actors

- Creates a new actor.
- Requires the `post:actors` permission.
- Returns the created actor object.

### POST /movies

- Creates a new movie.
- Requires the `post:movies` permission.
- Returns the created movie object.

### PATCH /actors/<int:actor_id>

- Updates an existing actor.
- Requires the `patch:actors` permission.
- Returns the updated actor object.

### PATCH /movies/<int:movie_id>

- Updates an existing movie.
- Requires the `patch:movies` permission.
- Returns the updated movie object.

### DELETE /actors/<int:actor_id>

- Deletes an existing actor.
- Requires the `delete:actors` permission.
- Returns a success message.

### DELETE /movies/<int:movie_id>

- Deletes an existing movie.
- Requires the `delete:movies` permission.
- Returns a success message.












>>>>>>> 0af1abb06e5deeef6e489dcd470ad4548f607dae
