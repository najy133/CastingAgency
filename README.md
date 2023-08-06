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

1. Make sure you have a PostgreSQL database running on your machine. You can download and install PostgreSQL from the [official website](https://www.postgresql.org/download/).

2. Create two databases: one for development and another for testing. You can use the following commands (replace `your_database_name` with appropriate names):

    ```bash
    createdb your_database_name
    createdb your_database_name_test
    ```

3. Apply migrations to set up the database schema:

    ```bash
    flask db upgrade
    ```

4. Set up environment variables:
    - Copy the `setup.bat.example` file to `setup.bat` (Windows) or `setup.sh` (macOS/Linux).
    - Open the copied file and fill in your Auth0 configuration and database URLs.

    ```bash
    # Windows
    setup.bat

    # macOS/Linux
    source setup.sh
    ```

5. Run the Flask app:

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














