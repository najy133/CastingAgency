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











